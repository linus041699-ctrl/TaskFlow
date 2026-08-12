from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('H', 'High'),
        ('M', 'Medium'),
        ('L', 'Low'),
    ]

    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('C', 'Completed'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateField()
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='M')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def priority_score(self):
        
        score = {'H': 3, 'M': 2, 'L': 1}.get(self.priority, 1)

        days_left = (self.due_date - timezone.now().date()).days

        if days_left < 0:
            score += 3   
        elif days_left <= 2:
            score += 2         
        elif days_left <= 7:
            score += 1          

        return score
