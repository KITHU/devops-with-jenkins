from rest_framework import routers, serializers, viewsets

from product.views import ProductViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'product', ProductViewSet)

urlpatterns = router.urls
