from django.urls import path
from .views import *
urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list'),
    path('create/', TiresCreateView.as_view(), name='product-create'),
    path('all/', TiresListView.as_view(), name='product-all'),
]
