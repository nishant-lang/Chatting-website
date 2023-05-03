from rest_framework import serializers
from userprofile.models import BlogPost


class Blogseralizer(serializers.ModelSerializer):
    class Meta:
        model=BlogPost
        fields=['blog','user_blog']