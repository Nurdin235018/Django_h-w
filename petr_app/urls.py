from django.urls import path
from .views import category_list, category_create, category_detail, category_change, category_delete

urlpatterns = [
    path('categories/', category_list),
    path('category-create/', category_create),
    path('categories/<int:pk>/', category_detail),
    path('category-change/<int:pk>/', category_change),
    path('category-delete/<int:pk>/', category_delete)
]
