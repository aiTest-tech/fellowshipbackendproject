from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import MediaModelViewSet, HelloView, MeetwithFellowsView

router = DefaultRouter()
router.register("mediaurl", MediaModelViewSet, basename="mediaurl")
router.register("meet-our-fellows", MeetwithFellowsView, basename="meet-our-fellows")


urlpatterns = [path("hello/", HelloView.as_view(), name="hello")]
urlpatterns += router.urls
