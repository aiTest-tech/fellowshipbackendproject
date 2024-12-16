from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import MediaModelViewSet, HelloView

router = DefaultRouter()
router.register("mediaurl", MediaModelViewSet, basename="mediaurl")


urlpatterns = [path("hello/", HelloView.as_view(), name="hello")]
urlpatterns += router.urls
