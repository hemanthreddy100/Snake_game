from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('snake/', views.snake_game, name='snake'),
    path('logout/', views.logout_view, name='logout'),
]
