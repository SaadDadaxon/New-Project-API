from rest_framework import views, status
from rest_framework.response import Response

from .serializers import ProSerializers
from ..models import Profile


class MyProfile(views.APIView):
    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return Response({'detail': 'Authenticated is required '}, status=status.HTTP_404_NOT_FOUND)
        profile = Profile.objects.filter(user_id=self.request.user.id).first()
        if profile:
            serializer = ProSerializers(profile)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'detail': 'User Not Found'}, status=status.HTTP_404_NOT_FOUND)



