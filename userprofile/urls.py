
from userprofile import views
# from userprofile.views import views
from django.urls import path
from django.conf import settings
from userprofile.views import Message


urlpatterns = [

    path('',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('dashbord/',views.dashbord,name="logedin"),
    path('logout/',views.logout,name="logout"),
    path('post1/',views.post,name="post"),
    path('send/',views.send_message,name="send"),
    path('inbox/',views.inbox,name="inbox"),
    path('profile/',views.profile,name="profile"),  
    path('chat/<int:chatting_with_user>',views.chat,name="chat"),
    path('message/<int:chatting_with_user>',Message.as_view(),name='Message'), 
   
]