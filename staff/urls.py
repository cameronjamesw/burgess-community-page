from . import views
from django.urls import path

urlpatterns = [
    path('staff_page/', views.display_staff, name='staff_page'),
    path('staff_page/burgess/', views.display_burgess_staff, name='burgess_staff'),
]