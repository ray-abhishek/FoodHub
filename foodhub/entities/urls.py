from entities import views
from rest_framework.routers import DefaultRouter
from django.urls import include, path

router = DefaultRouter()
router.register(r'merchants', views.MerchantViewSet)
router.register(r'items', views.ItemViewSet)
router.register(r'stores', views.StoreViewSet)
router.register(r'orders', views.OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
