from django.db import models

class Product(models.Model):
    CAT=((1,'Mobile'),(2,'Shoes'),(3,'Cloths'))
    name=models.CharField(max_length=50,verbose_name='Product Name')
    price=models.IntegerField()
    cat=models.IntegerField(verbose_name='Category',choices=CAT)
    pdetails=models.CharField(max_length=50,verbose_name='Product Details')
    is_active=models.BooleanField(default=True)
    pimage=models.ImageField(upload_to='image')
