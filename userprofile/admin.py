from django.contrib import admin
from .models import User,ProfilePic,BlogPost,Chat_messages,School,Student

# Register your models here.
admin.site.register(User)
admin.site.register(ProfilePic)
admin.site.register(BlogPost)
admin.site.register(Chat_messages)
admin.site.register(School)
admin.site.register(Student)

