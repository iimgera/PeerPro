from rest_framework.routers import DefaultRouter
from apps.dashboard.views import TeamEmployeeView

router = DefaultRouter()

router.register('teams',TeamEmployeeView,basename='teams')

urlpatterns = router.urls