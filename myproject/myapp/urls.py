from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('menu/',views.menu),
    path('display_date',views.display_date)
    
]
