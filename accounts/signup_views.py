from django.shortcuts import render,redirect
# from . models import UserInfo
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage

# Create your views here.

def signupEmailSend(email_receiver, username):
    mail_subject = "Welcome to Airbnb"
    message = '''Welcome to Airbnb. 
                Here you get the coolest stays with ultimate offers\n. 
                Below are the details of your account:
                Email: {}
                Username: {}'''.format(email_receiver, username)
    email = EmailMessage(mail_subject, message, to= [email_receiver])
    email.send()

def signup(request):
    if request.method == "POST":
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        user = User.objects.create(first_name=firstname,last_name=lastname,username=username,email=email,password=password)
        if user is not None:
            user.save()
            user.set_password(password)
            user.save()
            messages.success(request,"Account created")
            # signupEmailSend(email, username)
            return redirect('/')
        else:
            messages.info(request,"Something went wrong")
            return render(request, '/accounts/signup.html')

    return render(request, './accounts/signup.html')