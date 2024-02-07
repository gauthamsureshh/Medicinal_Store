from django.urls import path,include
from accounts import views

urlpatterns = [
    path('',views.home,name='homepage'),
    path('signup/',views.signup,name='signupage'),
    path('login/',views.loginpage,name='loginpage'),
    path('signout/',views.signout,name='signout'),
    path('user/',include('meds.urls'),name='user'),
    path('api/',include('api_med.urls'))
]
