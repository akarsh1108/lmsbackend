from django.shortcuts import render
from rest_framework import viewsets
from api.serializers import CategoriesSerializer,BooksSerializer
from api.models import Category,Books
# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategoriesSerializer

class BooksViewSet(viewsets.ModelViewSet):
    queryset=Books.objects.all()
    serializer_class=BooksSerializer

