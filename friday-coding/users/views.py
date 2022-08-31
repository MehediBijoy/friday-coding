from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import RegistrationSerializer


class Registration(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data='registration successfull')
