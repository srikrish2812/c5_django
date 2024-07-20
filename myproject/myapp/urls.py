from django.urls import path
from . import views

urlpatterns = [
    path('dishes/<str:dish>', views.dishes_with_path),
    path('dishes/', views.dishes_with_query)
    
]
