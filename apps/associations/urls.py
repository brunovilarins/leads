from rest_framework import routers

from .views import AssociationViewSet

app_name = "associations"
router = routers.DefaultRouter()

router.register("", AssociationViewSet, basename="associations")

urlpatterns = router.urls
