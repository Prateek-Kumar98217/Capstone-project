from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url = 'home/', permanent = True)),
    path('home/', views.home, name='home'),
    path('menu/', views.MenuItemList.as_view(), name='menu'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='single_menu'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]