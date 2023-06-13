
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager



# Create your models here.

class UserProfileManager(BaseUserManager):

    """Manager for the user"""   

    def create_user(self,email,username,full_name,gender,city,state,cardnumber,cvc,password=None):
        """Create new user"""
        if not email:
            raise ValueError('User must have the email')

        email=self.normalize_email(email)    
        user=self.model(email=email,username=username,full_name=full_name,gender=gender,city=city,state=state,cardnumber=cardnumber,cvc=cvc
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self,username,email,password=None):
        """Create aa new super user super user"""
        if not email:
            raise ValueError('User must have the email')
        email=self.normalize_email(email)
        user=self.model(email=email,username=username)
        user.set_password(password)
        user.is_superuser=True
        user.is_staff=True
        user.set_password(password)
        user.save(using=self._db)
        return user

                
class User(AbstractBaseUser,PermissionsMixin):
    
    """data base model for the user """

    username=models.CharField(max_length=50,unique=True,null=True)
    email=models.EmailField(max_length=50,unique=True)
    full_name=models.CharField(max_length=50,null=True)
    gender=models.CharField(max_length=10,null=True)
    city=models.CharField(max_length=50,null=True)
    state=models.CharField(max_length=50,null=True)
    cardnumber=models.CharField(unique=True,null=True,max_length=19)
    cvc=models.CharField(unique=True,null=True,max_length=6)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    

    objects=UserProfileManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']

    def get_full_name(self):
        """Retrive full name of the user"""
        return self.name
        
    def __str__(self):
        return self.email


class UserMessages(models.Model):
    user=models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    to_user=models.CharField(max_length=50,null=True)
    message=models.CharField(max_length=500,null=True)
    at_time=models.DateTimeField(auto_now_add=True)



class Chat_messages(models.Model):

    sender=models.ForeignKey(User,on_delete=models.CASCADE,related_name='sender_messages')
    receiver=models.ForeignKey(User,on_delete=models.CASCADE,related_name='receiver_messages')
    user_chat=models.CharField(max_length=500,null=True)
    at_time=models.DateTimeField(auto_now_add=True)


class ProfilePic(models.Model):
    user_pic=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_profile_pic',null=True)
    pic=models.ImageField(null=True,blank=True)
    
 
class BlogPost(models.Model):
    user_blog=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_blog_post',null=True)
    blog=models.CharField(max_length=100,null=True)
    on_time=models.DateTimeField(auto_now_add=True,null=True)
    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.blog
    

class School(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Student(models.Model):
    school=models.ForeignKey(School,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.EmailField(null=True)
    mobile=models.CharField(max_length=10)

    def __str__(self):
        return self.email









