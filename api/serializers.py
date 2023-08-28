from rest_framework import serializers
from api.models import Category,Books

class CategoriesSerializer(serializers.ModelSerializer):
    category_id=serializers.ReadOnlyField()
    class Meta:
        model = Category
        fields = '__all__'

class BooksSerializer(serializers.ModelSerializer):
    id=serializers.ReadOnlyField() 
    class Meta:
        model= Books
        fields = '__all__'
