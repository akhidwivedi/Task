from rest_framework import status
from rest_framework.decorators import api_view,authentication_classes, permission_classes
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from .resources  import ProductResource
from tablib import Dataset
from django.contrib import messages
from django.shortcuts import render
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from profile.customauth import  CustomAuthentication
from profile.custompermission import MyPermission
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from profile.models import  CustomUser

# Create your views here.
@api_view(['GET', 'POST'])
@authentication_classes([CustomAuthentication])
@permission_classes([MyPermission])
def product_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([CustomAuthentication])
@permission_classes([MyPermission])
def product_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






def  validate_user(id,token):
    try:
        log_user =  get_object_or_404(CustomUser,pk=id)
        if log_user.user_otp  == token:
            return True
        return  False
    except CustomUser.DoesNotExist:
        return False



def simple_upload(request,id,token):
    if   validate_user(id,token):
        if request.method == 'POST':
            product_resource = ProductResource()
            dataset = Dataset()
            new_product = request.FILES['myfile']
            if not new_product.name.endswith('xlsx'):
                messages.info(request,'upload.html')
                return render(request, 'upload.html')
            imported_data = dataset.load(new_product.read(),format='xlsx')
            for data in imported_data:
                product_value = Product(data[0],data[1],data [2],data[3],data[4],data[5],data[6]  
                )
                product_value.save()
            return HttpResponse("data is uploaded succesfully")
        return render(request, 'upload.html')
    return HttpResponse("User is not Authenticated, please register the user")