from django.db import models
from django.contrib.auth.models import User

class Request(models.Model):
    STATUS_CHOICES = [
        ('Новая', 'Новая'),
        ('Принято в работу', 'Принято в работу'),
        ('Выполнено', 'Выполнено'),
    ]
    
    CATEGORY_CHOICES = [
        ('Квартира', 'Квартира'),
        ('Дом', 'Дом'),
        ('Офис', 'Офис'),
        ('Коммерческое помещение', 'Коммерческое помещение'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Квартира')
    image = models.ImageField(upload_to='images/')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Новая')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title