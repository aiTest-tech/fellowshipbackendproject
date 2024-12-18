from rest_framework.viewsets import ModelViewSet
from .models import MediaModel, MeetOurFellowsModel
from .serializers import MediaModelSerializer, MeetOurFellowsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class MediaModelViewSet(ModelViewSet):
    queryset = MediaModel.objects.all()
    serializer_class = MediaModelSerializer


class HelloView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"name": "brijesh"})

class MeetwithFellowsView(ModelViewSet):
    queryset = MeetOurFellowsModel.objects.all()
    serializer_class = MeetOurFellowsSerializer