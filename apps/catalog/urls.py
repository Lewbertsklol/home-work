from django.urls import path
from . import views


app_name = 'catalog'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('feedback/', views.FeedbackView.as_view(), name='feedback'),
]
