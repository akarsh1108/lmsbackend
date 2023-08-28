from django.contrib import admin
from django.urls import path,include
from api.views import CategoryViewSet,BooksViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'categories',CategoryViewSet)
router.register(r'books',BooksViewSet)


urlpatterns = [
    path('',include(router.urls))
]
