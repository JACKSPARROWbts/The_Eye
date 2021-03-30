from django.shortcuts import render
from .serializers import PostSerializer
from .models import Upload
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
@permission_classes([AllowAny])
# Create your views here.
class PostView(APIView):
    parser_class=(MultiPartParser,FormParser)
    def get(self,request,*args,**kwargs):
        posts=Upload.objects.all()
        serializer=PostSerializer(posts,many=True)
        return Response(serializer.data)
    def post(self,request,*args,**kwargs):
        post_serializer=PostSerializer(data=request.data)
        if post_serializer.is_valid():
            post_serializer.save()
            return  Response(post_serializer.data,status=status.HTTP_200_OK)
def delete_view(request,id):
    if request.method=='GET':
        pass
    Upload.objects.get(id=id).image.delete(save=True)
