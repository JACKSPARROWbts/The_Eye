from django.urls import path
from . import views
from .views import delete_view
from .api import ViewSet
from rest_framework import routers
urlpatterns=[
        path('delete/<id>',delete_view),
     path('api/uploaded/',views.PostView.as_view()),
]
# router=routers.DefaultRouter()
# router.register('api/uploaded',ViewSet,'post_list')
# urlpatterns=router.urls