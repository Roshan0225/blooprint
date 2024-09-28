from django.urls import path
from .views import ItemCreateView, ItemRetrieveView, ItemUpdateView, ItemDeleteView,ItemListView

urlpatterns = [
    path('items/', ItemCreateView.as_view(), name='item-create'),
    path('items/<int:pk>/', ItemRetrieveView.as_view(), name='item-retrieve'),
    path('items/<int:pk>/update/', ItemUpdateView.as_view(), name='item-update'),
    path('items/<int:pk>/delete/', ItemDeleteView.as_view(), name='item-delete'),
    path('items/all/', ItemListView.as_view(), name='item-list'),
]
