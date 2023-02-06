from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from product import views

urlpatterns = [
    path('products/', views.product_list),
    path('products/<int:pk>/', views.product_detail),
    path('bulkupload/<int:id>/<int:token>/', views.simple_upload),
]

urlpatterns = format_suffix_patterns(urlpatterns)