from django.urls import path
from . import views

urlpatterns = [
     path('', views.discussion_list, name='home'),
     path('<slug:slug>/', views.discussion_content, name='discussion_content'),
     path('<slug:slug>/edit_comment/<int:comment_id>',
          views.comment_edit, name='comment_edit'),
     path('<slug:slug>/delete_comment/<int:comment_id>',
          views.comment_delete, name='comment_delete'),
     path('<slug:slug>/edit_discussion/',
          views.discussion_edit, name='discussion_edit/'),
     path('<slug:slug>/delete_discussion/',
          views.discussion_delete, name='discussion_delete/')
]
