from django.conf import UserSettingsHolder
from django.db import models
from products.models import Product
from products.serializers import ProductSerializer
# from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import filters

# from .serializers import ReviewSerializer


# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    product_image = models.CharField(max_length=255, default = "no image")
    product_review = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

# class UserListView(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = ReviewSerializer
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['username', 'email']


# # class ProductsList(generics.ListAPIView):
#     serializer_class = ProductSerializer

#     def get_queryset(self):
#         queryset = Product.object.all()
#         username = self.request.query_params.get('admin')
#         if username is not None:
#             queryset = queryset.filter(review_username=username)
#             return queryset

# class UserListView(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     filter_backends = [django_filters.rest_framework.DjangoFilterBackEnd]