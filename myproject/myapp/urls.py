from django.urls import path, re_path
from . import views

urlpatterns = [
    path('dishes/<str:dish>', views.dishes_with_path),
    path('dishes/', views.dishes_with_query),
    re_path(r"^menu_item/[0-9]{2}/$", views.regex),
    path('home',views.form_view),
    path('about/', views.about),
    path('menu/', views.menu),
    path('menu_card/', views.menu_by_id),
]
