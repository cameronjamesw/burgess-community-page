from . import views
from django.urls import path

urlpatterns = [
    path('', views.discussion_list, name='home'),
    path('<slug:slug>/', views.discussion_content, name='disc_content'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
     path('<slug:slug>/edit_discussion/',
         views.discussion_edit, name='discussion_edit/'),
]