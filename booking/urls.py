from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_dashboard, name='admin-dashboard'),
    path('manage_classes',views.manage_classes, name='manage_classes'),
    path('add_class',views.add_class,name="add_class"),
    path('edit_class/<int:class_id>/',views.edit_class,name="edit_class"),
    path('delete_class/<int:class_id>/',views.delete_class,name="delete_class"),
    path('all_bookings/', views.all_bookings_view, name='all_bookings'),
]