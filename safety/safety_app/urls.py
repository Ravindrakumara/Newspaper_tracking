
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from.views import ItemViewSet,BrandViewSet,CategoryViewSet

router = routers.DefaultRouter()
router.register('Item', ItemViewSet)
router.register('Brand', BrandViewSet)
router.register('Category', CategoryViewSet)

urlpatterns = [
    path('',include(router.urls))
]
