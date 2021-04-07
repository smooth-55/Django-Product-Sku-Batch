from django.db import models
import uuid

# Create your models here.

class CommonAttributes(models.Model):
    created_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class Product(CommonAttributes):

    BRAND_CHOICES = [
        ('ZOD', 'Zodiac'),
        ('PAN', 'Park Avenue'),
        ('NKE', 'Nike'),
        ('ADS', 'Adidas'),
        ('SPR', 'Spykar'),
        ('GSR', 'Gstar'),
        
    ]

    PRODUCT_CATEGORY_CHOICES = [
        ('SE', 'Shoes'),
        ('ST', 'Shirt'),
        ('PT', 'Pant'),

    ]
    
    image = models.ImageField(upload_to='dynamic_images')
    label = models.CharField(max_length=2, choices=PRODUCT_CATEGORY_CHOICES)
    price = models.FloatField()
    brand = models.CharField(max_length=3, choices=BRAND_CHOICES)
    description = models.TextField()
    remaining_stock = models.PositiveIntegerField(default=1)
    
    
    class Meta:
        verbose_name = 'Products'
        verbose_name_plural = 'Product'
        db_table = 'product'
        ordering = ['-created_on']
        

    def __str__(self):
        return self.label

class Sku(CommonAttributes):
    COLOR_CHOICES = [
        ('RD', 'Red'),
        ('WE', 'White'),
        ('GY', 'Gray'),
        ('YW', 'Yellow'),
        ('BK', 'Black'),

    ]

    SIZE_CHOICES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra_Large'),

    ]

    GENDER_CHOICES = [
        ('M', 'Mens'),
        ('F', 'Womens'),
    ]

    id  = models.UUIDField(primary_key=True, default = uuid.uuid4, editable = False)
    sku_code = models.CharField(max_length=250,null=True,blank=True)
    color = models.CharField(max_length=2, choices=COLOR_CHOICES)
    size = models.CharField(max_length=2, choices=SIZE_CHOICES) 
    gender_category = models.CharField(max_length=1, choices=GENDER_CHOICES)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
   
    class Meta:
        verbose_name = 'Skus'
        verbose_name_plural = 'Sku'
        db_table = 'sku'
        ordering = ['-id']

    def save(self, *args, **kwargs):
            self.sku_code = self.gender_category + '-' + self.product.label + '-' + self.product.brand + '-' + self.color + '-' + self.size + '-' + str(self.id)        
            super(Sku, self).save(*args, **kwargs)

    def __str__(self):
        return self.sku_code

class Batch(CommonAttributes):
    sku = models.ForeignKey(Sku, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Batchs'
        verbose_name_plural = 'Batch'
        db_table = 'batch'
  
    def __str__(self):
        return str(self.id)



