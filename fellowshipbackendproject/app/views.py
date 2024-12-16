from rest_framework.viewsets import ModelViewSet
from .models import MediaModel
from .serializers import MediaModelSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class MediaModelViewSet(ModelViewSet):
    queryset = MediaModel.objects.all()
    serializer_class = MediaModelSerializer


class HelloView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"name": "brijesh"})
