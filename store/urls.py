
from django.urls import path

from web_project import views
from . import views

urlpatterns = [
    path('',views.store, name="store"),
    path('category/<slug:category_slug>/', views.store, name='products_by_category'),
    path('subcategory/<slug:subcategory_slug>/<slug:maincategory_slug>/', views.substore, name='products_by_subcategory'),

    path('maincategory/<slug:maincategory_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('subcategorycategory/<slug:subcategory_slug>/<slug:product_slug>/', views.subproduct_detail, name='subproduct_detail'),

    path('search/',views.search,name='search'),
    path('submit_review/<int:product_id>/', views.submit_review, name='submit_review'),
]