from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'
        # fields=['id',username','email','password','firstname']
        
        # extra_kwargs{
        #     'email':{'requried':True}
        # }