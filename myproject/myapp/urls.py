from django.urls import path, re_path
from . import views

urlpatterns = [
    path('dishes/<str:dish>', views.dishes_with_path),
    path('dishes/', views.dishes_with_query),
    re_path(r"^menu_item/[0-9]{2}/$", views.regex)
    
]
