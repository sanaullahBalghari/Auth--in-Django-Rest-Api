from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import UserSerializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def example_view(request, format=None):
    user=request.user
    print(user.username)
    print('*'*10)
    content = {
        'status': 'request was permitted'
    }
    return Response(content)

@api_view(['POST', 'GET'])
def register_user(request):
    data=request.data 
    print(data)
    if 'password' in data:
        data['password']=make_password(data['password'])

    serializer=UserSerializers(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
