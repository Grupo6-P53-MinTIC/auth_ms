from django.contrib import admin
from django.urls import path
from authApp import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('user/', views.UserCreateView.as_view()),
    path('user/<int:pk>', views.UserRetrieveUpdateDeleteView.as_view()),
    path('user/<int:pk>', views.UserDetailView.as_view()),

    # All users
    path('users/', views.AllUsersView.as_view()),
    # All divers
    path('drivers/', views.AllDriversView.as_view()),
    # All cars
    path('cars/', views.AllCarsView.as_view()),

    path('car/', views.CarListCreateView.as_view()),
    path('car/<int:pk>', views.CarRetrieveUpdateDeleteView.as_view()),
    # Get car by 'numero de placa'
    path('car/<int:pk>', views.CarDetailView.as_view()),
    #Get car by driver
    path('car_driver/<int:id_driver>', views.CarDriverView.as_view()),
]


