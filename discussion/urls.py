from . import views
from django.urls import path

urlpatterns = [
    path('', views.DiscussionList.as_view(), name='home'),
    path('<slug:slug>/', views.discussion_content, name='discussion_content'),
]