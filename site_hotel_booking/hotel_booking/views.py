from django.http import HttpResponse
from django.shortcuts import render
from .models import Hotel
from django.template.loader import render_to_string
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Hotel, Bookings
from .forms import BookingForm, HotelForm


# Create your views here.



def index(request):
    return HttpResponse('Страница приложения hotel booking')

def hotel_rooms(request):
    rooms = Hotel.objects.all()
    return render(request, 'hotel_booking/hotel_rooms.html', {'rooms': rooms,})

def hotel_main_page(request):
    # t = render_to_string("hotel_booking/hotel_main_page.html")
    # return HttpResponse(t)
    data = {'title': 'Главная страница сервиса бронирования номеров отеля'}
    return render(request, "hotel_booking/hotel_main_page.html", data)


def book_room(request, room_id):
    room = get_object_or_404(Hotel, id=room_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.room = room  # привязываем к выбранному номеру
            booking.save()
            messages.success(request, f'Номер "{room.name}" успешно забронирован!')
            return redirect('hotel_rooms')  # замените на имя вашего URL со списком номеров
    else:
        # Предзаполняем форму, если нужно
        form = BookingForm(initial={'room': room})

    def delete_room(request, room_id):
        room = get_object_or_404(Hotel, id=room_id)
        room_name = room.name  # сохраним имя для сообщения
        room.delete()
        messages.success(request, f'Номер "{room_name}" успешно удален вместе со всеми бронированиями.')

    return render(request, 'hotel_booking/book_room.html', {'form': form, 'room': room})

def delete_booking(request, booking_id):
    booking = get_object_or_404(Bookings, id=booking_id)
    room_id = booking.room.id
    booking.delete()
    messages.success(request, 'Бронирование удалено.')
    return redirect('bookings_list', room_id=room_id)

def delete_room(request, room_id):
    room = get_object_or_404(Hotel, id=room_id)
    room_name = room.name  # сохраним имя для сообщения
    room.delete()
    messages.success(request, f'Номер "{room_name}" успешно удален вместе со всеми бронированиями.')

def room_admin_panel(request):
    rooms = Hotel.objects.all()
    return render(request, 'hotel_booking/room_admin_panel.html', {'rooms': rooms})

def bookings_list(request, room_id):
    room = get_object_or_404(Hotel, id=room_id)
    bookings = room.bookings_set.all()  # предполагаем related_name='bookings'
    # если related_name не задан, используйте: bookings = room.booking_set.all()
    return render(request, 'hotel_booking/bookings_list.html', {'room': room, 'bookings': bookings})

def add_room(request):
    if request.method == 'POST':
        form = HotelForm(request.POST)
        if form.is_valid():
            room = form.save()  # создаётся объект Hotel
            messages.success(request, f'Номер "{room.name}" успешно добавлен.')
            return redirect('hotel_rooms')  # замените на имя вашего URL со списком номеров
    else:
        form = HotelForm()
    return render(request, 'hotel_booking/add_room.html', {'form': form})

