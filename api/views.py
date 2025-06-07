from rest_framework.decorators import api_view
from rest_framework.response import Response
from booking.models import *
from .serializers import FitnessClassSerializer,BookingSerializer,BookingDetailSerializer
from rest_framework import status

@api_view(['GET'])
def get_all_classes(request):
    classes = FitnessClass.objects.all()
    serializer = FitnessClassSerializer(classes, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def book_class(request):
    serializer = BookingSerializer(data=request.data)
    if serializer.is_valid():
        class_id = serializer.validated_data['class_id']
        client_name = serializer.validated_data['client_name']
        client_email = serializer.validated_data['client_email']

        try:
            fitness_class = FitnessClass.objects.get(id=class_id)
        except FitnessClass.DoesNotExist:
            return Response({'error': 'Fitness class not found.'}, status=status.HTTP_404_NOT_FOUND)

        # Check if already booked
        if Booking.objects.filter(fitness_class=fitness_class, client_email=client_email).exists():
            return Response({'error': 'You have already booked this class.'}, status=status.HTTP_400_BAD_REQUEST)

        if fitness_class.available_slots <= 0:
            return Response({'error': 'No slots available.'}, status=status.HTTP_400_BAD_REQUEST)

        # Reduce available slots
        fitness_class.available_slots -= 1
        fitness_class.save()

        # Save booking
        Booking.objects.create(
            fitness_class=fitness_class,
            client_name=client_name,
            client_email=client_email
        )

        return Response({'message': 'Booking successful.'}, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_bookings_by_email(request):
    email = request.query_params.get('email')
    if not email:
        return Response({'error': 'Email parameter is required.'}, status=status.HTTP_400_BAD_REQUEST)

    bookings = Booking.objects.filter(client_email=email)
    if not bookings.exists():
        return Response({'message': 'No bookings available for this email id.'}, status=status.HTTP_200_OK)
    serializer = BookingDetailSerializer(bookings, many=True)
    return Response(serializer.data)