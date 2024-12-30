from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import MediaModelViewSet, HelloView, MeetwithFellowsViewSet, BatchViewSet

router = DefaultRouter()
router.register("mediaurl", MediaModelViewSet, basename="mediaurl")
router.register("meet-our-fellows", MeetwithFellowsViewSet, basename="meet-our-fellows")
router.register('batch', BatchViewSet, basename = "batch")


urlpatterns = [path("hello/", HelloView.as_view(), name="hello")]
urlpatterns += router.urls
