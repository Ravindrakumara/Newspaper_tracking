from django.db import models



class Brand(models.Model):
    brand = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Brand"

    def __str__(self):
        return self.brand


class Category(models.Model):
    category = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Category"

    def __str__(self):
        return self.category



class Item(models.Model):
    Size = (
        ('F', 'Free'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('U', 'unknown'),
    )
    title = models.CharField(max_length=80)
    image = models.ImageField(upload_to='pics')
    price = models.DecimalField(max_digits=6,decimal_places=2)
    discount = models.DecimalField(max_digits=6,decimal_places=2)
    slug = models.SlugField(max_length=80)
    brand_name = models.ForeignKey(Brand,on_delete=models.CASCADE)
    category_name = models.ForeignKey(Category,on_delete=models.CASCADE)
    colour = models.CharField(max_length=80)
    size = models.CharField(max_length=80, choices=Size)
    weight = models.FloatField()
    discription = models.TextField(max_length=80)
    modify_date = models.DateTimeField()
    expiry_date = models.DateTimeField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
