
from django.contrib import messages
from django.shortcuts import render,redirect
from userprofile.models import User,UserMessages,Chat_messages,ProfilePic,BlogPost
from django.contrib.auth.models import auth
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import generics
import pytz
import django


# User registrations

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

# User login

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
       
# Logedin page

def dashbord(request): 

    current_user=request.user

    if request.method=="POST": 
        
        return render(request,'logedin.html') 

    else:    
    
       csrf_token=django.middleware.csrf.get_token(request)
       return render(request,'logedin.html',{'current_user':current_user,'csrf_token':csrf_token}) 

# Logout page

def logout(request):
        auth.logout(request)
        messages.info(request,'You are logout')
        return redirect('/')

# All user list functon

def message_post(request):
    users=User.objects.all()        
    currentuser=request.user.email 

    return render(request,"post1.html",{'users':users,'currentuser':currentuser})

# send message function

def send_message(request):
    if request.method =='POST':
        postuser=request.POST['postuser']
        message=request.POST['message']
        currentuser=request.user
        
        post=UserMessages.objects.model(to_user=postuser,message=message,user=currentuser)
        post.save()

        messages.info(request,'Your message has been sent')
        return render(request,"logedin.html")

# Inbox messages

def inbox(request):
    context={}

    current_user_email=request.user.email
    recived_messages=UserMessages.objects.filter(to_user=current_user_email).all() 
    context['recived_messages']=recived_messages

    return render(request,"inbox.html",context)
    

#profile

def profile(request):
    return render(request,"profile.html")

# Chatting function

def chat(request,chatting_with_user):
    context={}
    users=User.objects.all()
    img=ProfilePic.objects.filter(user_pic=chatting_with_user).last()

    
    chatmessages=Chat_messages.objects.filter((Q(sender=request.user)|Q(receiver=request.user))&((Q(sender=chatting_with_user)|Q(receiver=chatting_with_user))))

    csrf_token=django.middleware.csrf.get_token(request)
    currentuser=User.objects.get(id=request.user.id)
    reciveremail=User.objects.get(id=chatting_with_user)

    context['chatting_with_user']=chatting_with_user
    context['chatmessages']=chatmessages
    context['csrf_token']=csrf_token
    context['sender']=currentuser
    context['users']=users
    context['reciveremail']=reciveremail
    context['img']=img

    return render(request,"chat.html",context)


# Message Api

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

# User blogPost api

class UserBlogPostAPi(generics.GenericAPIView):

    def post(self,request):
        
        current_user=request.user
        blog=request.data['blog_typing']

        blogs=BlogPost.objects.model(user_blog=current_user,blog=blog)
        blogs.save()
        blog_id=blogs.id
      
        # tz_IN = pytz.timezone('Asia/Kolkata')
        # time = post.on_time.astimezone(tz_IN)

        return Response({
            'user_email':current_user.email,
            'blog':str(blog),
            'blog_id':blog_id
            # 'time':time.strftime("%m/%d/%Y, %I:%M %p")
        })


    def get(self,request):
        
        current_user=request.user
       
        blogs=BlogPost.objects.filter(user_blog=current_user).all()
     
        blog_content=[{
            'blog_id':blog.id,
            'blogs':blog.blog
        } for blog in blogs]
        
        return Response({
            'blog_user':(current_user.email),
            'all_blogs':blog_content,
            'message':'success'
           })


# Api for the profile pic

class ProfilePicAPi(generics.GenericAPIView):
  

    def get(self,request):
        current_user=request.user
    
        img=ProfilePic.objects.filter(user_pic=current_user).last()
        
        return Response({
            'img':str(img.pic),
            "message":"get method success"    
        })  
        

    def post(self,request):
        
        current_user=request.user
        file=request.FILES.get("file")

        user=ProfilePic.objects.model(user_pic=current_user,pic=file)
        user.save()
    
        return Response({

            'user_pic':current_user.email,
            'profile_pic':str(file),      # geting error without chenging the file to the str
            "message":"success"    
        }) 
        


# Extracting the current post 
class BlogApi(generics.GenericAPIView):

    def get(self,request,pk=None):    
        _id=pk
        obj=BlogPost.objects.filter(id=_id).first()

        return Response({
            'id':_id,
            'obj':obj.blog,
            'message':'success'   
        })


class UpdateBlog(generics.GenericAPIView):

    def post(self,request):
        blog_id = request.data['blog_id']
        blog = request.data['blog']
        get_blog = BlogPost.objects.filter(id=blog_id).first()
        get_blog.blog = blog
        get_blog.save()
    
        return Response( {
            "msg" : "success"
        })


# Blog delete function

def blog_delete(request,pk=None):
   
    Blog_to_delete=BlogPost.objects.filter(id=pk).first()
    
    Blog_to_delete.delete()
        
    messages.info(request,'Your message has been deleted')
    return redirect('/dashbord/')
    


