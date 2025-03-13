from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class OrganizationSetting(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    currency = models.CharField(max_length=255, null=True, blank=True, default="Rs")
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name
    

class Restaurant(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name
    


class FoodCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='categories/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name
    


class Food(models.Model):
    type_options = (
        ('veg', 'Veg'),
        ('non-veg', 'Non-Veg')
    )
    
    
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='foods/', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    category = models.ForeignKey(FoodCategory, on_delete=models.DO_NOTHING)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.DO_NOTHING)
    type = models.CharField(max_length=255, choices=type_options, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name
    
    
    
class Customer(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, unique=True)
    password = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    photo = models.ImageField(upload_to='customers/', null=True, blank=True)
    otp = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name



class Order(models.Model):
    status_options = (
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Processing', 'Processing'),
        ('On The Way', 'On The Way'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled')
    )
    
    
    id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=255, choices=status_options, default="Pending")
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    address = models.CharField(max_length=255, null=True, blank=True)
    latitude = models.CharField(max_length=255, null=True, blank=True)
    longitude = models.CharField(max_length=255, null=True, blank=True)
    destination_phone = models.CharField(max_length=255, null=True, blank=True)
    sub_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    delivery_charge = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.food.name


class Banner(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    url = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='banners/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.id)


class Rating(models.Model):
    id = models.BigAutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    star = models.IntegerField(default=0)
    review = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.id)
    

class Notification(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    message = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to= 'notifications/', null=True, blank=True)
    url = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
