from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import ProductSerializers
from .models import Product


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_product(request):
    data=request.data 
    data['seller']=request.user.id 
    serializer=ProductSerializers(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_product(request):
    product=Product.objects.filter(seller=request.user.id)
    serializer=ProductSerializers(product, many=True)
    return Response(serializer.data)