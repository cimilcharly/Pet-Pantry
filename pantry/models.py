from django.db import models

# Create your models here.
class Register(models.Model):
    name=models.CharField(max_length=20)
    phone=models.IntegerField()
    email=models.EmailField()
    address=models.CharField(max_length=505)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    def __str__(self):
        return  self.username

class product(models.Model):
    Product_name=models.CharField(max_length=300)
    Price=models.IntegerField()
    Stock=models.IntegerField()
    image=models.FileField()


class cart(models.Model):
    user_details=models.ForeignKey(Register,on_delete=models.CASCADE)
    product_details=models.ForeignKey(product,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1,null=True)

class wish_list(models.Model):
    user_details = models.ForeignKey(Register, on_delete=models.CASCADE)
    product_details=models.ForeignKey(product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, null=True)



class Order(models.Model):
    user = models.ForeignKey(Register, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=15)
    country = models.CharField(max_length=15)
    zip_code = models.CharField(max_length=10, null=True)
    phone = models.CharField(max_length=15)
    product_order = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total_price = models.IntegerField()
    payment_status = models.CharField(max_length=20,null=True)
    purchase_date = models.DateTimeField(auto_now=True, null=True)
    product_status = models.CharField(max_length=50,null=True, default='Order Placed')
    instruction = models.CharField(max_length=50,null=True, default='Your Order Has Been Successfully Placed')
    delivery_date = models.DateField(null=True)

class Mail(models.Model):
    mail = models.CharField(max_length=25)
    def __str__(self):
        return self.mail

class PasswordReset(models.Model):
    user=models.ForeignKey(Register, on_delete=models.CASCADE)
    token=models.CharField(max_length=200)

class deliveryboy(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phno=models.IntegerField()
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    proof=models.FileField()
    status=models.CharField(max_length=10,default='pending',null=True)
    work_status=models.CharField(max_length=20,default='free')

class orderitem(models.Model):
    user_detaill=models.CharField(max_length=20)
    delivery=models.CharField(max_length=20)
    order_details=models.ForeignKey(Order,on_delete=models.CASCADE)
    product_detail=models.ForeignKey(product,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    price=models.IntegerField()
    status=models.CharField(max_length=20,default='pending')
