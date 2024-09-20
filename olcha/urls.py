from django.urls import path
from .views import CategoryListApiView, CategoryDetailApiView

urlpatterns = [
    path('', CategoryListApiView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailApiView.as_view(), name='category-detail'),
]
