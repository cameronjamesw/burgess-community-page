from . import views
from django.urls import path

urlpatterns = [
    path('', views.DiscussionList.as_view(), name='home'),
]