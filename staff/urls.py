from django.urls import path
from . import views

urlpatterns = [
    path('staff_page/', views.display_staff,
         name='staff_page'),
    path('staff_page/burgess/', views.display_burgess_staff,
         name='burgess_staff'),
    path('staff_page/hayward/', views.display_hayward_staff,
         name='hayward_staff'),
]
