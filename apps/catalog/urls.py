from django.urls import path
from django.views.decorators.cache import cache_page

from . import views


app_name = 'catalog'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),

    path('product/create/', views.ProductCreateView.as_view(), name='product_form'),
    path('product/<int:pk>/', cache_page(60)(views.ProductDetailView.as_view()), name='product_detail'),
    path('product/update/<int:pk>/', views.ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', views.ProductDeleteView.as_view(), name='product_delete'),

    path('product/<int:product_pk>/versions/', views.VersionListView.as_view(), name='version_list'),
    path('product/<int:product_pk>/versions/create/', views.VersionCreateView.as_view(), name='version_form'),
    path('versions/delete/<int:pk>/', views.VersionDeleteView.as_view(), name='version_delete'),
    path('versions/toggle_current/<int:pk>/', views.toggle_current_version, name='version_toggle'),

    path('feedback/', views.FeedbackView.as_view(), name='feedback'),
]
