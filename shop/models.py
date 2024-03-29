from django.db import models
from django.db.models.fields import DateField, TextField

# Create your models here.

class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc=models.CharField(max_length=2000)
    pub_date=models.DateField()
    image = models.ImageField(upload_to="shop/images", default="  ")

    def __str__(self):
        return self.product_name

      

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    amount = models.IntegerField( default=0)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="") 

    def __str__(self):
        return self.name     

class OrderUpdate(models.Model):
    update_id  = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."        

class Blogpost(models.Model):
    post_id = models.AutoField(primary_key= True)
    tilte = models.CharField(max_length=50)
    head0 = models.CharField(max_length=500, default="")
    chead0 = models.CharField(max_length=5000, default="")
    head1 = models.CharField(max_length=500, default="")
    chead1 = models.CharField(max_length=5000, default="")
    head2 = models.CharField(max_length=500, default="")
    chead2 = models.CharField(max_length=5000, default="")
    pub_date = models.DateField()
    thumbnail = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        return self.tilte  

class Feedback(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    comments = models.TextField(max_length=50)

    def __str__(self):
        return self.name

class Detail(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    appointmentdate = models.CharField(max_length=50)
    appointmenttime = models.CharField(max_length=50)
    message = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Prepare(models.Model):
    yourname = models.CharField(max_length=50)
    youremail = models.CharField(max_length=10)
    yourphone = models.CharField(max_length=10)
    youraddress = models.CharField(max_length=50)
    yourspecialnote = models.CharField(max_length=50)
    yourcity = models.CharField(max_length=50)
    yourstate = models.CharField(max_length=50)
    postalcode = models.CharField(max_length=50)
    drugname = models.CharField(max_length=50)
    potency = models.CharField(max_length=50)
    prepared = models.CharField(max_length=50)
    quantity = models.CharField(max_length=50)

    def __str__(self):
        return self.yourname
