from django.db import models
import datetime
import uuid
# Create your models here.

class Category(models.Model):
    category_code=models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    category_image = models.URLField(max_length=500)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'
        db_table = 'Category'



class Product(models.Model):
    product_code=models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    description = models.TextField()
    product_offer = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    return_option = models.BooleanField(default=False)
    return_date = models.DateField(null=True, blank=True)
    count = models.IntegerField(default=0)



    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Products'
        db_table = 'Product'
        verbose_name = 'Product'

class ProductInventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    instock = models.IntegerField()
    limitedstock = models.IntegerField()
    reservedstock = models.IntegerField()

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name_plural = 'ProductInventory'
        db_table = 'ProductInventory'
        verbose_name = 'ProductInventory'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.URLField(max_length=500)


    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name_plural = 'Product Images'
        db_table = 'Product_Image'
        verbose_name = 'Product Image'

class ProductSection(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    section_code=models.CharField(max_length=50)
    section_name = models.CharField(max_length=100)

    def __str__(self):
        return self.section_name


    class Meta:
        verbose_name_plural = 'Product Sections'
        db_table = 'Product_Section'
        verbose_name = 'Product Section'


class ProductAttribute(models.Model):
    section = models.ForeignKey(ProductSection, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Product Attributes'
        db_table = 'Product_Attribute'
        verbose_name = 'Product Attribute'

class Relatedproduct(models.Model):
    product = models.ForeignKey(Product, related_name='related_products',on_delete=models.CASCADE)
    related_product = models.ForeignKey(Product, related_name='related_to_products',on_delete=models.CASCADE)

    def __str__(self):
        return self.related_product.name

    class Meta:
        verbose_name_plural = 'Related Products'
        db_table = 'Related_Product'
        verbose_name = 'Related Product'


class BillingAddress(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    mobile=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    country=models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Billing Address'
        db_table = 'Billing_Address'
        verbose_name = 'Billing Address'

class ShippingAddress(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    mobile=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    country=models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Shipping Address'
        db_table = 'Shipping_Address'
        verbose_name = 'Shipping Address'


class Orderstatus(models.Model):
    orderstatus = models.CharField(max_length=100)

    def __str__(self):
        return self.orderstatus

    class Meta:
        verbose_name_plural = 'Order Status'
        db_table = 'Order_Status'
        verbose_name = 'Order Status'


class order(models.Model):
    order_code=models.CharField(max_length=50)
    order_id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ManyToManyField(Product)
    order_status = models.ForeignKey(Orderstatus, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name_plural = 'Orders'
        db_table = 'Order'
        verbose_name = 'Order'

class ordersummary(models.Model):
    order_summary_id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order=models.ForeignKey(order, on_delete=models.CASCADE)
    order_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.order_summary_id

    class Meta:
        verbose_name_plural = 'Order Summary'
        db_table = 'Order_Summary'
        verbose_name = 'Order Summary'

class Wishlist(models.Model):
    wishlist_code=models.CharField(max_length=50)
    wishlist_id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ManyToManyField(Product)

    def __str__(self):
        return self.wishlist_code

    class Meta:
        verbose_name_plural = 'Wishlist'
        db_table = 'Wishlist'
        verbose_name = 'Wishlist'


