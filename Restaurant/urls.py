from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('menu/', views.MenuItemList.as_view(), name='menu'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='single_menu'),
]