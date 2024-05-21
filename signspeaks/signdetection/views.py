from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import EmailMultiAlternatives
from django.template import Context
from django.contrib import messages
from django.contrib.auth import logout as auth_logout

# from .forms import NewUserForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .models import *
import uuid
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist

#password reset
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from .forms import PasswordResetRequestForm, SetNewPasswordForm
from django.urls import reverse


# views.py
from django.shortcuts import render, redirect
from django.http import StreamingHttpResponse, JsonResponse
from django.views.decorators import gzip
from keras.models import model_from_json
import numpy as np
import cv2
import threading
import os
from django.conf import settings

# Update the paths to your model files using BASE_DIR
MODEL_JSON_PATH = os.path.join(settings.BASE_DIR, 'signdetection', 'ASLsign.json')
MODEL_WEIGHTS_PATH = os.path.join(settings.BASE_DIR, 'signdetection', 'ASLsign.h5')

# Load model architecture from JSON file
with open(MODEL_JSON_PATH, "r") as json_file:
    model_json = json_file.read()

# Load model from JSON
model = model_from_json(model_json)

# Load weights into the model
model.load_weights(MODEL_WEIGHTS_PATH)

# Label list
label = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'blank']

# Helper function to extract features
def extract_features(image):
    feature = np.array(image)
    feature = feature.reshape(1, 48, 48, 1)
    return feature / 255.0

# Video camera class for capturing frames
class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        _, frame = self.video.read()
        return frame

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()

# Generator function for streaming video
def gen(camera):
    while True:
        frame = camera.get_frame()
        cv2.rectangle(frame, (0, 40), (300, 300), (0, 165, 255), 1)
        cropframe = frame[40:300, 0:300]
        cropframe = cv2.cvtColor(cropframe, cv2.COLOR_BGR2GRAY)
        cropframe = cv2.resize(cropframe, (48, 48))
        cropframe = extract_features(cropframe)
        pred = model.predict(cropframe)
        prediction_label = label[pred.argmax()]
        cv2.rectangle(frame, (0, 0), (300, 40), (0, 165, 255), -1)
        if prediction_label == 'blank':
            cv2.putText(frame, " ", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        else:
            accu = "{:.2f}".format(np.max(pred) * 100)
            cv2.putText(frame, f'{prediction_label}  {accu}%', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        _, jpeg = cv2.imencode('.jpg', frame)
        frame = jpeg.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@gzip.gzip_page
def video_feed(request):
    try:
        return StreamingHttpResponse(gen(VideoCamera()), content_type="multipart/x-mixed-replace; boundary=frame")
    except Exception as e:
        print(f"Error: {e}")
        return JsonResponse({'error': str(e)})

# sign recognition template
def recognition(request):
    return render(request, 'recognition.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            if User.objects.filter(username = username).first():
                messages.success(request, 'Username is taken.')
                return redirect('/register')

            if User.objects.filter(email = email).first():
                messages.success(request, 'Email is taken.')
                return redirect('/register')
            
            user_obj = User(username = username , email = email)
            user_obj.set_password(password)
            user_obj.save()


            auth_token = str(uuid.uuid4())
            profile_obj = Profile.objects.create(user = user_obj , auth_token = auth_token)
            profile_obj.save()
            
            send_mail_after_registration(email , auth_token)
            print("Redirecting to /token") 
            return redirect('/token')
        except Exception as e:
            print(e)
            
    return render(request , 'users/register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username = username).first()
        if user_obj is None:
            messages.success(request, 'User not found.')
            return redirect('/login')
        
        
        profile_obj = Profile.objects.filter(user = user_obj ).first()

        if not profile_obj.is_verified:
            messages.success(request, 'Profile is not verified check your mail.')
            return redirect('/login')

        user = authenticate(username = username , password = password)
        if user is None:
            messages.success(request, 'Wrong password.')
            return redirect('/login')
        
        login(request , user)
        return redirect('/')

    return render(request , 'users/login.html')
	
User = get_user_model()
#forgot password
def forgot_password(request):
    if request.method == "POST":
        form = PasswordResetRequestForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = User.objects.get(email=email)
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            password_reset_url = request.build_absolute_uri(
                reverse('reset_password', args=[uid, token])
            )
            message = render_to_string('users/password_reset_email.html', {
                'user': user,
                'password_reset_url': password_reset_url,
            })
            send_mail(
                'Password Reset Request',
                message,
                'speakssign@gmail.com',
                [user.email],
                fail_silently=False,
            )
            return redirect('password_reset_done')
    else:
        form = PasswordResetRequestForm()
    return render(request, 'users/forgot_password.html', {'form': form})
    
#reset passsword
def reset_password(request, uidb64, token):
    if request.method == "POST":
        form = SetNewPasswordForm(request.POST)
        if form.is_valid():
            try:
                uid = force_str(urlsafe_base64_decode(uidb64))
                user = User.objects.get(pk=uid)
            except (TypeError, ValueError, OverflowError, User.DoesNotExist):
                user = None

            if user is not None and default_token_generator.check_token(user, token):
                new_password = form.cleaned_data['new_password']
                user.set_password(new_password)
                user.save()
                return redirect('login')
    else:
        form = SetNewPasswordForm()
    return render(request, 'users/reset_password.html', {'form': form})

def password_reset_done(request):
    return render(request,'users/password_reset_done.html')

def homepage(request):
    return render(request,'homepage.html')

def aboutus(request):
    return render(request,'aboutus.html')

def contactus(request):
    return render(request,'contactus.html')

def success(request):
    return render(request , 'users/success.html')

def token_send(request):
    return render(request , 'users/token_send.html')

# email verification 
def send_mail_after_registration(email , token):
    subject = 'Your accounts need to be verified'
    message = f'Hi paste the link to verify your account http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message , email_from ,recipient_list )

def verify(request , auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token = auth_token).first()
    

        if profile_obj:
            if profile_obj.is_verified:
                #message
                messages.success(request, 'Your account is already verified.')
                return redirect('/login')

            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request, 'Your account has been verified.')
            return redirect('/login')
        else:
            #message
            messages.success(request, 'Invalid verification link.')
            return redirect('/')

    except Exception as e:
        print(e)
        return redirect('/')


@login_required
def update_profile(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = request.user
        user.username = username
        user.email = email

        if password:
            user.set_password(password)
        
        user.save()

        messages.success(request, 'Profile updated successfully')
        return redirect('login')

    return render(request, 'users/update_profile.html')