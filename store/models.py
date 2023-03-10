from tkinter import CASCADE
from django.db import models
from category.models import Category
from category.models import SubCategory
from django.urls import reverse
from accounts.models import Account
from django.db.models import Avg, Count

# Create your models here.
#in html template we write images.url it will print the url of the image
#once its rendered in the browser it will match with the media folder   
class Product(models.Model):
    product_name    = models.CharField(max_length=200, unique=True)
    slug            = models.SlugField(max_length=200, unique=True)
    description     = models.TextField(max_length=500, blank=True)
    price           = models.IntegerField()
    images          = models.ImageField(upload_to='photos/products')
    stock           = models.IntegerField()
    is_available    = models.BooleanField(default=True)
    #cascade = whenever we deleate the category the product is attached to that category will be deleated 
    maincategory = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE,null=True,blank=True)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)
# ######self mean this product ,category.slug means the inside the app category and get to models model.category.slug 
    def get_url(self):
     return reverse('product_detail', args=[self.maincategory.slug, self.slug,])

    def subget_url(self):
     return reverse('subproduct_detail', args=[self.subcategory.slug, self.slug,])

    def __str__(self):
        return self.product_name

    def averageReview(self):
        #filter the product by self (particualr product) aggreagte the function for particular produt and it takes the avhg for the rating for this product
        reviews = ReviewRating.objects.filter(product=self, status=True).aggregate(average=Avg('rating'))
        avg = 0
        if reviews['average'] is not None:
            avg = float(reviews['average'])
        return avg

    def countReview(self):
        reviews = ReviewRating.objects.filter(product=self, status=True).aggregate(count=Count('id'))
        count = 0
        if reviews['count'] is not None:
            count = int(reviews['count'])
        return count
    

class VariationManager(models.Manager):
    def colors(self):
        return super(VariationManager, self).filter(variation_category='color', is_active=True)

    def sizes(self):
        return super(VariationManager, self).filter(variation_category='size', is_active=True)

variation_category_choice = (
    ('color', 'color'),
    ('size', 'size'),
)





# this class to separate the color from the sizes

class Variation(models.Model):
    product= models.ForeignKey(Product,on_delete=models.CASCADE)# if the product id deleted also the variation will delete 
    variation_category= models.CharField(max_length=100,choices=variation_category_choice)
    variation_value = models.CharField(max_length=100)
    is_active= models.BooleanField(default=True)
    created_date=models.DateTimeField(auto_now=True)
    
    objects=VariationManager()
    def __str__(self):
       return self.variation_value
   
   

class ReviewRating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, blank=True)
    review = models.TextField(max_length=500, blank=True)
    rating = models.FloatField()
    ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject




class ProductGallery(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='store/products', max_length=255)

    def __str__(self):
        return self.product.product_name
# this for spelling 
    class Meta:
        verbose_name = 'productgallery'
        verbose_name_plural = 'product gallery'

