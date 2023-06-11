from django.urls import path
from base import views

urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.loginUser,name='login'),
    path('home/',views.home,name='home'),
    path('logout/', views.logoutUser, name="logout"),
]
