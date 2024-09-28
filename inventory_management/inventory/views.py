from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Item
from .serializers import ItemSerializer
from rest_framework.permissions import IsAuthenticated
from django.core.cache import cache
from rest_framework.response import Response

class ItemCreateView(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

class ItemRetrieveView(generics.RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        item_id = kwargs.get('pk')
        cached_item = cache.get(f'item_{item_id}')
        if cached_item:
            return Response(cached_item)
        
        response = super().get(request, *args, **kwargs)
        cache.set(f'item_{item_id}', response.data)
        return response
    

class ItemListView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        cached_items = cache.get('all_items')
        if cached_items:
            return Response(cached_items)
        
        response = super().list(request, *args, **kwargs)
        cache.set('all_items', response.data)
        return response
    

class ItemUpdateView(generics.UpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

class ItemDeleteView(generics.DestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]
