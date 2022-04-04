from django.shortcuts import render

# Create your views here.
from products.models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from products.serializers import ProductSerializer
from .models import Review
from .serializers import ReviewSerializer
from . import serializers
from django.shortcuts import get_object_or_404


# Create your views here.
@api_view(['GET'])
def review_filter_list(request):
    review_param = request.query_params.get('review')
    sort_param = request.query_params.get('sort')
    
    product = Product.objects.all()
    if review_param:
        product = product.filter(review_name = product_param)
    if sort_param:
        product = product.order_by(sort_param)

    serializer = ProductSerializer(product, many= True)
    return Response(serializer.data)

@api_view(['GET','POST'])
def review_list(request):
    if request.method == 'GET':
        review = Review.objects.all()
        serializer = ReviewSerializer(review, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def review_list(request):

    appending_dict_example = {}
    appending_dict_example['title'] = 'beef'
    print(appending_dict_example)

    reviews = Review.objects.all()
    
    custom_response_dictionary = {}

    for review in reviews:

        product = Product.objects.filter(review_id=review.id)

        product_serializer = ProductSerializer(product, many=True)

        custom_response_dictionary[review.name] = {
            "address": review.address,
            "products": product_serializer.data
        }
    return Response(custom_response_dictionary)