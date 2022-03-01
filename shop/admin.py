from django.contrib import admin

# Register your models here.
from .models import Product, Orders, OrderUpdate, Blogpost, Feedback, Detail, Prepare

admin.site.register(Product)
admin.site.register(Orders)
admin.site.register(OrderUpdate)
admin.site.register(Blogpost)
admin.site.register(Feedback)
admin.site.register(Detail)
admin.site.register(Prepare)


