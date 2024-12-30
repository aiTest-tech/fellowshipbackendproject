from rest_framework.viewsets import ModelViewSet
from .models import MediaModel, MeetOurFellowsModel, BatchModel
from .serializers import MediaModelSerializer, MeetOurFellowsSerializer, BatchSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class MediaModelViewSet(ModelViewSet):
    queryset = MediaModel.objects.all()
    serializer_class = MediaModelSerializer


class HelloView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"name": "brijesh"})


class MeetwithFellowsViewSet(ModelViewSet):
    queryset = MeetOurFellowsModel.objects.all()
    serializer_class = MeetOurFellowsSerializer

class BatchViewSet(ModelViewSet):
    queryset = BatchModel.objects.all()
    serializer_class = BatchSerializer