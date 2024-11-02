from django.urls import path
from . import views
urlpatterns = [  
    path('login/', views.loginPage,name='login'),
    path('register/', views.registerpage,name='register'), 
    path('profile/', views.profilepage,name='profile'),
    path('logout/',views.logoutpage, name='logout'),
]