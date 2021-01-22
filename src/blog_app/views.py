from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response 
from .models import Post
from .serializers import PostSerializer
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny

# Create your views here.



@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([AllowAny])
def post_list(request):
    if request.method == 'GET':
        post = Post.objects.all()
        post = post.filter(status = 'p')
        serializer = PostSerializer(post,many = True)
        return Response(serializer.data)
 
 
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])   
def post_create(request):  
    if request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        request.data['author'] = request.user.id
        if serializer.is_valid():
            serializer.save()
            data = {
                'message':'New Post created succesfully'
            }
            return Response(data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    
@api_view(['GET','DELETE','PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated]) 
def post_get_update_delete(request,id):
    post = get_object_or_404(Post,id = id)
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PostSerializer(post,data = request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'message':'This Post updated succesfully'
            }
            return Response(data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)