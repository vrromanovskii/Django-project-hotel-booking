"""
URL configuration for site_hotel_booking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hotel_booking.views import *


urlpatterns = [
    path('booking/', index),
    path('admin/', admin.site.urls),
    path('hotel_rooms/', hotel_rooms, name='hotel_rooms'),
    path('', hotel_main_page, name='hotel_main_page'),
    path('book/<int:room_id>/', book_room, name='book_room'),
    path('delete/<int:room_id>/', delete_room, name='delete_room'),
    path('room_admin_panel/', room_admin_panel, name='room_admin_panel'),
    path('bookings_list/<int:room_id>/', bookings_list, name='bookings_list'),
    path('add_room/', add_room, name='add_room'),
    path('delete_booking/<int:booking_id>/', delete_booking, name='delete_booking'),
]
