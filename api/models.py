from django.db import models
from django.conf import settings
from UserProfile.models import Customer

# Create your models here.

class Category(models.Model):
    title=modals.CharField(max_length=200)
    caregory_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    slug= models.SlugField(default=None)
    featured_product = models.OneToOneField('Product',on_delete=models.CASCADE,blank=True, null=True, related_name='featured')
    icon = models.Charfield (max_Length=100, default=None, blank= True, null=True)


    def __str__(self):
        return self.title


class Product(models.Model):
    name= models.ChatField(max_length=200)
    description = models.TextField(blank=True, null=True)
    discount= models.TextField(default=False)
    image = models.ImageField(uplad_to='img',blank=True, null=True, default='')
    old_price= models.FloatField(default=False)
    category= models.ForeignKey('Category',on_delete=models.SET_NULL, blank=True, null=True, related_name='products')
    slug = models.SlugField(default=None)
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True)
    inventory=models.IntegerField(default=5)
    top_deal= models.BooleanField(default=False)
    flash_sales= models.BooleanField(default=False)

class Review(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE, related_name = "reviews")
    date_created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(default="description")
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.description




class Cart(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    created  = models.DatetimeField(auto_now_add=True)

    def __str__(self):
        return str(self.cart_id)


class Cartitems(models.Model):
    cart= models.ForeignKey('Cart',on_delete=models.CASCADE, blank=True, null=True)
    product= models.ForeignKey('Product',on_delete=models.CASCADE, blank=True, null=True, related_name='cartitems')
    quantity=models.IntegerField(default=0)





