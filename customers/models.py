from django.db import models

# model for customer.
from django.contrib.auth.models import User
class Customer(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'Live'),(DELETE,'Delete'))
    address=models.TextField
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer_profile')
    phone=models.CharField(max_length=10)
    image=models.ImageField(upload_to='media/')
    delete_status = models.IntegerField(choices=DELETE_CHOICES, default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name