from django.db import models

class FitnessClass(models.Model):
    CLASS_CHOICES = [
        ('Yoga', 'Yoga'),
        ('Zumba', 'Zumba'),
        ('HIIT', 'HIIT'),
    ]

    name = models.CharField(max_length=20, choices=CLASS_CHOICES)
    instructor = models.CharField(max_length=100)
    start_date = models.DateField()
    total_slots = models.PositiveIntegerField()
    available_slots = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        # Ensure available_slots does not exceed total_slots
        if self.available_slots > self.total_slots:
            self.available_slots = self.total_slots
        super().save(*args, **kwargs)

class Booking(models.Model):
    fitness_class = models.ForeignKey(FitnessClass, on_delete=models.CASCADE, related_name='bookings')
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField()
    booked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('fitness_class', 'client_email')
    def __str__(self):
        return f"{self.client_name} - {self.fitness_class.name} on {self.fitness_class.date_time.strftime('%Y-%m-%d %H:%M')}"
