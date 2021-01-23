from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response 
from .models import Post, Like, View
from .serializers import PostSerializer, LikeSerializer, CommentSerializer, PostDetailSerializer
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
            serializer.save(author=request.user)
            data = {
                'message':'New Post created succesfully'
            }
            return Response(data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([AllowAny]) 
def post_get(request,slug):
    post = get_object_or_404(Post,slug = slug)
    view_qs = View.objects.filter(user=request.user.id, post=post)
    if view_qs:
        pass
    else:
        serializer = PostDetailSerializer(data = request.data)
        request.data['user'] =request.user.id
        request.data['post'] = post.id
        if serializer.is_valid():
            serializer.save(user = request.user.id, post = post)
    if request.method == 'GET':  
        serializer = PostDetailSerializer(post)
        return Response(serializer.data)


        



@api_view(['PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated]) 

def post_update_delete(request,slug):
    post=get_object_or_404(Post, slug=slug)
    if post.author.id == request.user.id:
        if request.method == 'PUT':
            request.data['author'] = request.user.id
            serializer = PostSerializer(post, data=request.data)
            
            if serializer.is_valid():
                
                serializer.save(author=request.user)
                data={
                    "message": "Post updated successfully!"
                }
                return Response(data)  
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'DELETE':
            post.delete()
            data={
                    "message": "Post deleted successfully!"
                }
            return Response(data, status=status.HTTP_204_NO_CONTENT)
    else:
        data= {
            "message":"You are not authorized"
        }
        return Response(data, status= status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def comment_view(request, slug):
    post = get_object_or_404(Post, slug=slug)
    serializer = CommentSerializer(data=request.data)
    if request.method == 'POST': 
        if serializer.is_valid():
            serializer.save(user=request.user, post= post)
           
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return  Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

        

@api_view(["POST"])
def like_view(request, slug):
    post = get_object_or_404(Post, slug=slug)
    
    if request.method == "POST":
        like_qs = Like.objects.filter(user=request.user, post=post)
        if like_qs:
            like_qs.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            serializer = LikeSerializer(data=request.data)
            request.data["user"] = request.user.id
            request.data["post"] = post.id
            if serializer.is_valid():
                serializer.save(user= request.user, post=post)
                return Response(status=status.HTTP_201_CREATED)
        return  Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)