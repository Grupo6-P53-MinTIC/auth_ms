from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from authApp import views

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('verifyToken/', views.VerifyTokenView.as_view()),

    # path('admin/', admin.site.urls),
    path('userByToken/', views.getUserByToken.as_view()),
    path('user/', views.UserCreateView.as_view()),
    # path('userDelUpt/<int:pk>', views.UserRetrieveUpdateDeleteView.as_view()),
    path('user/<int:pk>', views.UserDetailView.as_view()),

    # All users
    path('users/', views.AllUsersView.as_view()),
    # All divers
    path('drivers/', views.AllDriversView.as_view()),
    # All cars
    path('cars/', views.AllCarsView.as_view()),

    path('car/', views.CarListCreateView.as_view()),
    path('car/<str:pk>', views.CarRetrieveUpdateDeleteView.as_view()),
    # Get car by 'numero de placa'
    path('car/<str:pk>', views.CarDetailView.as_view()),
    #Get car by driver
    path('car-driver/<int:idDriver>', views.CarDriverView.as_view()),
]


