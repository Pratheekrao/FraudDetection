# models.py in Login app
from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from review.models import BuyerDetails  # Import BuyerDetails from reviews app

class LoginDetails(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # Will store hashed password
    role = models.CharField(max_length=255)
    last_login = models.DateTimeField(null=True, blank=True)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.email

    class Meta:
        db_table = "logindetails"

class SellerDetails(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=255, null=True)
    seller_id = models.CharField(max_length=255, primary_key=True)
    login = models.OneToOneField(
        LoginDetails, 
        on_delete=models.CASCADE, 
        related_name='seller_profile',
        null=True
    )

    def __str__(self):
        return f"{self.name} ({self.email})"

    class Meta:
        db_table = "sellerdetails"
