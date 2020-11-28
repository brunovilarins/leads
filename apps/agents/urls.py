from rest_framework import routers

from .views import AgentsViewSet

app_name = "agents"
router = routers.DefaultRouter()

router.register("", AgentsViewSet, basename="agents")

urlpatterns = router.urls
