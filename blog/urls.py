from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('dashboard/', views.Userdashboard, name='dashboard'),
    path('signup/', views.Usersignup, name='signup'),
    path('login/', views.Userlogin, name='login'),
    path('logout/', views.Userlogout, name='logout'),
    path('addblog/', views.Addblog, name='addblog'),
    path('updateblog/<int:pk>', views.BlogUpdateView.as_view(), name='updateblog'),
    path('deleteblog/<int:pk>', views.BlogDeleteView.as_view(), name='deleteblog'),
]
