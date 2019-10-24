from rest_framework.response import Response
from rest_framework.views import APIView


class StatusViewSet(APIView):

    @staticmethod
    def get(request):
        return Response(data={'status': 'running'})
