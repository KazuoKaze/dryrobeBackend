from django.db import models
from django.utils.text import slugify

class JustSending(models.Model):
    COLOR_CHOICES = [
        ('Black', 'Black'),
        ('Blue', 'Blue'),
        ('Camo', 'Camo'),
        ('Green', 'Green'),
        ('Gray', 'Gray'),
        ('Orange', 'Orange'),
        ('Pink', 'Pink'),
        ('Purple', 'Purple'),
    ]
    ProductType_CHOICES = [
        ('Adapt', 'Adapt'),
        ('Boots & Mittens', 'Boots & Mittens'),
        ('Dryrobe® Advance', 'Dryrobe® Advance'),
        ('Headwear', 'Headwear'),
        ('Lite', 'Lite'),
        ('Towel Change Robes', 'Towel Change Robes'),
    ]
    Size_CHOICES = [
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('8', '8'),
        ('10', '10'),
        ('12', '12'),
        ('14', '14'),
        ('16', '16'),
        ('One Size', 'One Size'),
    ]
    PRODUCTTYPE_CHOICES = [
        ('Adults', 'Adults'),
        ('Kids', 'Kids'),
        ('Accessories', 'Accessories'),
    ]
    productTitle = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bio = models.CharField(max_length=99999, null=True, blank=True)
    bio2 = models.CharField(max_length=99999, null=True, blank=True)
    bio3 = models.CharField(max_length=99999, null=True, blank=True)
    bio4 = models.CharField(max_length=99999, null=True, blank=True)
    productImage = models.ImageField(upload_to='uploads/', blank=True, null=True)
    # productImage2 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    # productImage3 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    # productImage4 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    # productImage5 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    # productImage6 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    # productImage7 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    # productImage8 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    # productImage9 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    createdAT = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    quantity = models.IntegerField(default=1)
    size = models.CharField(max_length=255, null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    isOnFrontPage = models.BooleanField(default=False)
    defaultcolors = models.CharField(max_length=50, choices=COLOR_CHOICES, default='')
    defaultSize = models.CharField(max_length=50, choices=Size_CHOICES, default='')
    defaultproductType = models.CharField(max_length=50, choices=ProductType_CHOICES, default='')
    defaultproductVar = models.CharField(max_length=255, choices=PRODUCTTYPE_CHOICES, default='')

    class Meta:
        verbose_name_plural = 'products'
        ordering = ['createdAT']

    def __str__(self):
        return f"{self.id} - {self.productTitle}"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.productTitle)
        super().save(*args, **kwargs)
    


    

class Coupon(models.Model):
    product = models.ManyToManyField(JustSending, related_name='coupon')
    coupon = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        verbose_name_plural = 'coupon'

    def __str__(self):
        return f"{self.coupon}"
    

class SizeVariant(models.Model):
    firstVariant = models.CharField(max_length=255, null=True, blank=True)
    secondVariant = models.CharField(max_length=255, null=True, blank=True)
    thirdVariant = models.CharField(max_length=255, null=True, blank=True)
    fourthVariant = models.CharField(max_length=255, null=True, blank=True)
    product = models.ManyToManyField(JustSending, related_name='variant')

    class Meta: 
        verbose_name_plural = 'SizeVariant'

    def __str__(self):
        return f"{self.firstVariant}"
    
class ColorClassVariant(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    varianImg1 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    varianImg2 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    varianImg3 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    varianImg4 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    varianImg5 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    varianImg6 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    varianImg7 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    varianImg8 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    varianImg9 = models.ImageField(upload_to='uploads/', blank=True, null=True)

    class Meta: 
        verbose_name_plural = 'ColorClassVariant'

    def __str__(self):
        return f"{self.title}"
    
class ColorVariant(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    varianImg = models.ImageField(upload_to='uploads/', blank=True, null=True)    
    product = models.ManyToManyField(JustSending, related_name='colorvariant')
    imgsHere = models.ForeignKey(ColorClassVariant, on_delete=models.CASCADE,  related_name='colorclassvariant')

    class Meta: 
        verbose_name_plural = 'ColorVariant'

    def __str__(self):
        return f"{self.title}"
    

    
class OrderItem(models.Model):
    firstName = models.CharField(max_length=255, null=True, blank=True)
    lastName = models.CharField(max_length=255, null=True, blank=True)
    phoneNumber = models.IntegerField()
    email = models.EmailField(max_length=255, null=True, blank=True)
    fullName = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    address2 = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    pinCode = models.IntegerField()
    phoneNumber2 = models.IntegerField()
    textNote = models.CharField(max_length=955, null=True, blank=True)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        verbose_name_plural = 'Order Details'

    def __str__(self):
        return f"{self.email}"
    
class OrderItemProduct(models.Model):
    order_item = models.ForeignKey(OrderItem, related_name='order_items', on_delete=models.CASCADE)
    product = models.ForeignKey(JustSending, related_name='products', on_delete=models.CASCADE)
    size = models.CharField(max_length=255, null=True, blank=True)
    color = models.ForeignKey(ColorVariant, related_name='order_item_colors', on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Order'

    def __str__(self):
        return f"{self.product.productTitle} - Size: {self.size} (Quantity: {self.quantity})"