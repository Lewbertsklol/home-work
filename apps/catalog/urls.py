from django.urls import path
from . import views


app_name = 'catalog'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('product/<int:pk>/', views.product_view, name='product'),
    path('feedback/', views.feedback_view, name='feedback'),
]
