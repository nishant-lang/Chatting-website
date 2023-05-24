
from userprofile import views
from django.urls import path
from userprofile.views import Message, ProfilePicAPi, UserBlogPostAPi,BlogApi,UpdateBlog


urlpatterns = [

    path('',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('dashbord/',views.dashbord,name="dashbord"),
    path('logout/',views.logout,name="logout"),
    path('post1/',views.message_post,name="post"),
    path('send/',views.send_message,name="send"),
    path('inbox/',views.inbox,name="inbox"),
    path('profile/',views.profile,name="profile"), 
    path('chat/',views.chating_page,name="chat"),

    path('message/<int:chatting_with_user>',Message.as_view(),name='Message'), 
    
    path('blog_post/',UserBlogPostAPi.as_view(),name='blog_post'), 
    path('user_profile/',ProfilePicAPi.as_view(),name='profilepic'), 
    path('blog_delete/<int:pk>',views.blog_delete, name='blog_delete'), 
    path('blog_update/<int:pk>',BlogApi.as_view(), name='blog_update'),
    path('updated_blog/',UpdateBlog.as_view(), name='blog_update'),
    path('download_file/',views.download_file, name='download_file'),
   
    
]