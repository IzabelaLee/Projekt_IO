from django.urls import path

from . import views

app_name = 'plants'
ROOT_URLCONF = 'plants.urls'

urlpatterns = [
    path('<int:pk>/', views.detail, name='detail'),
]