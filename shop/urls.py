from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("blogpost/<int:id>", views.blogpost, name="blogHome"),
    path("about/", views.about, name="AboutUs"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="Search"),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path("checkout/", views.checkout, name="Checkout"),
    path("detail/", views.detail, name="detail"),
    path("feedback/", views.feedback, name="feedback"),
    path("product/", views.product, name="Product"),
    path("prepare/", views.prepare, name="prepare"),
    
]
