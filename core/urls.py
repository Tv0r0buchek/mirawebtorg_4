from django.urls import path
from core.views import ProductDetailView

urlpatterns = [
    path("<slug:slug>", ProductDetailView.as_view(), name="product_detail")

]
