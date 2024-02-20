from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, Phone: {self.phone}, Address: {self.address}, Registered: {self.date_registered.strftime('%Y-%m-%d %H:%M')}"

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField() 
    date_add_product = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return (f"Name: {self.name}, Price: ${self.price}, "
                f"Quantity: {self.quantity}, Added on: {self.date_add_product.strftime('%Y-%m-%d')}")


class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        product_ids = ', '.join(str(product.id) for product in self.products.all())
        return (f"Customer: {self.customer.name}, "
                f"Products: [{product_ids}], Total Price: ${self.total_price}, "
                f"Ordered on: {self.date_ordered.strftime('%Y-%m-%d')}")
