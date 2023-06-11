from django.urls import path
from . import views
from core.views import index

app_name = 'plant'

urlpatterns = [
    path('<int:pk>/', views.detail, name='detail'),
    path('', index, name='index'),
]