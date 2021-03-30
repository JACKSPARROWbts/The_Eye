from TheEye.models import Upload
from rest_framework import viewsets,permissions
from .serializers import PostSerializer
class ViewSet(viewsets.ModelViewSet):
    queryset=Upload.objects.all()
    permissions_classes=[
        permissions.AllowAny
    ]
    serializer_class=PostSerializer