from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('products/', views.ProductList.as_view()),
    path('products/<int:id>/', views.product_detail),
    path('collection/', views.collection_list),
    path('collection/<int:id>/', views.product_detail)
]
