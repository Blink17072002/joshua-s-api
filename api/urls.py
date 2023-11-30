from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_view, name='view'),
    path('<int:pk>/', views.adjust_models_view, name='adjust_models_view')
]