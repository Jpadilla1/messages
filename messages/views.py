from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Message
from .serializers import MessageSerializer


class MessageViewSet(ModelViewSet):
    model = Message
    serializer_class = MessageSerializer


class WebhookReceiverView(APIView):

    def post(self, request):
        print request.DATA
        return Response(request.DATA)
