from django.shortcuts import render, redirect, get_object_or_404
from .models import FitnessClass, Booking
from django.utils.timezone import make_aware
from datetime import datetime
import pytz
from django.http import JsonResponse
from datetime import date

IST = pytz.timezone('Asia/Kolkata')


def admin_dashboard(request):
    total_classes = FitnessClass.objects.count()
    total_bookings = Booking.objects.count()
    context = {
        'total_classes': total_classes,
        'total_bookings': total_bookings,
        'current_url_name':"dashboard"
    }
    return render(request, 'dashboard.html',context)


def manage_classes(request):
    today = date.today()
    classes = FitnessClass.objects.all().order_by('-id')
    context = {
        'today':today,
        'classes':classes,
        'current_url_name':"manage_classes"
    }
    return render(request, 'manage_classes.html', context)

def add_class(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        try:
            name = request.POST['name']
            instructor = request.POST['instructor']
            start_date = make_aware(datetime.strptime(request.POST['start_date'], '%Y-%m-%d'))
            total_slots = int(request.POST['total_slots'])

            FitnessClass.objects.create(
                name=name,
                instructor=instructor,
                start_date=start_date,
                total_slots=total_slots,
                available_slots=total_slots
            )

            return JsonResponse({'success': True, 'message': 'Class added successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': f'Error: {str(e)}'})
    return JsonResponse({'success': False, 'message': 'Invalid request'})

def edit_class(request, class_id):
    today = date.today()
    fitness_class = get_object_or_404(FitnessClass, id=class_id)
    if request.method == 'POST':
        fitness_class.name = request.POST['name']
        fitness_class.instructor = request.POST['instructor']
        fitness_class.start_date = datetime.strptime(request.POST['date_time'], '%Y-%m-%d').date()
        fitness_class.available_slots = int(request.POST['available_slots'])
        fitness_class.save()
        return redirect('manage_classes')
    context = {
        'class': fitness_class,
        'current_url_name':"manage_classes"
    }
    return render(request, 'edit_class.html', context)

def delete_class(request, class_id):
    fitness_class = get_object_or_404(FitnessClass, id=class_id)
    fitness_class.delete()
    return redirect('manage_classes')


def all_bookings_view(request):
    bookings = Booking.objects.select_related('fitness_class').all()
    context = {
        'current_url_name':'view_bookings',
        'bookings': bookings
    }
    return render(request, 'view_bookings.html',context)