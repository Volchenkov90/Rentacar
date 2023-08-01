from django.urls import path
from . import views
urlpatterns = [
    path('signupaccount/', views.signupaccount, name='signupaccount'),
    path('logout/', views.logoutaccount, name='logoutaccount'),
    path('login/', views.loginaccount, name='loginaccount'),
    path('makereview/', views.makereview, name='makereview'),
    path('successreview/', views.newreview, name='newreview'),
    path('reviews/', views.reviews, name='reviews'),
         
    
]