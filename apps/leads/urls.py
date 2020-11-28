from rest_framework import routers

from .views import LeadsViewSet

app_name = "leads"
router = routers.DefaultRouter()

router.register("", LeadsViewSet, basename="leads")

urlpatterns = router.urls
