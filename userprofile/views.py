

from multiprocessing import context
from django.contrib import messages
from django.shortcuts import render,redirect
from userprofile.models import User,UserMessages,Chat_messages
from django.contrib.auth import get_user_model
from django.contrib.auth.models import auth
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
import django
import pytz


# Create your views here.

def register(request):
    if request.method =='POST':
        email=request.POST['email']
        username=request.POST['username']
        full_name=request.POST['full_name']
        gender=request.POST['gender']
        state=request.POST['state']
        cardnumber=request.POST['cardnumber']
        cvc=request.POST['cvc']
        city=request.POST['city']
        password=request.POST['password']
        password2=request.POST['password2']
        

        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email allready taken')
                return redirect('/')
               
            else:
                user=User.objects.create_user(email=email,username=username,full_name=full_name,gender=gender,state=state,cardnumber=cardnumber,cvc=cvc,city=city,password=password)
                user.save()
                messages.info(request,'User created sucessfully')
                return redirect('login/')        
        else:
            messages.info(request,'Password not matching') 
            return redirect("register")
            
    return render(request,'register.html')


def login(request):
    if request.method =='POST':
        email=request.POST['email']
        password=request.POST['password']

        user=auth.authenticate(email=email,password=password)

        if user is not None:
            auth.login(request,user)
            messages.info(request,'You are Logedin')
            
            return redirect('/dashbord/')
        else:
            messages.info(request,'invalid credentials') 
            return render(request,"login.html")

    else:
        return render(request,"login.html")
       

def dashbord(request):   
    return render(request,'logedin.html')


def logout(request):
        auth.logout(request)
        messages.info(request,'You are logout')
        return redirect('/')


def post(request):
    users=User.objects.all()        
    currentuser=request.user.email  
    return render(request,"post1.html",{'users':users,'currentuser':currentuser})


def send_message(request):
    if request.method =='POST':
        postuser=request.POST['postuser']
        message=request.POST['message']
        currentuser=request.user
        
        post=UserMessages.objects.model(to_user=postuser,message=message,user=currentuser)
        post.save()

        messages.info(request,'Your message has been sent')
        return render(request,"logedin.html")



def inbox(request):
    context={}

    current_user_email=request.user.email
    recived_messages=UserMessages.objects.filter(to_user=current_user_email).all() 
    context['recived_messages']=recived_messages

    return render(request,"inbox.html",context)
    

def profile(request):
    return render(request,"profile.html")


def chat(request,chatting_with_user):
    context={}
    users=User.objects.all()
    

    chatmessages=Chat_messages.objects.filter((Q(sender=request.user)|Q(receiver=request.user))&((Q(sender=chatting_with_user)|Q(receiver=chatting_with_user))))

    csrf_token=django.middleware.csrf.get_token(request)
    currentuser=User.objects.filter(id=request.user.id).first()

    context['chatting_with_user']=chatting_with_user
    context['chatmessages']=chatmessages
    context['csrf_token']=csrf_token
    context['sender']=currentuser
    context['users']=users

    return render(request,"chat.html",context)



class Message(generics.GenericAPIView):
     
    def post(self,request,chatting_with_user):

       reciveddata=request.data['msg']
       currentuser=User.objects.filter(id=request.user.id).first()
       receiver=User.objects.filter(id=chatting_with_user).first()
      
       post=Chat_messages.objects.model(receiver=receiver,sender=currentuser,user_chat=reciveddata) 
       post.save()

       tz_IN = pytz.timezone('Asia/Kolkata')
       time = post.at_time.astimezone(tz_IN)

       return Response({

            "message" :reciveddata,
            "reciever" :receiver.email,
            "sender" :currentuser.email,
            "time" :time.strftime("%m/%d/%Y, %I:%M %p")
        })


