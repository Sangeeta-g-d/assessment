from django.urls import path
from .views import get_all_classes,book_class,get_bookings_by_email


urlpatterns = [
    path('classes/', get_all_classes, name='get_all_classes'),
    path('book/', book_class, name='book_class'),
    path('bookings/', get_bookings_by_email, name='get_bookings_by_email'),
]