from django.urls import path
from django.conf.urls import include
from ojas import views

urlpatterns = [path('', views.uploadfile, name='upload')]