from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RideSerializers, RideBookSerializer
from rest_framework import generics
from .models import Rides
from rest_framework.permissions import AllowAny, IsAuthenticated


# Create your views here.
# class RiderViewSet(viewsets.ModelViewSet):
#     queryset = Rides.objects.all()
#     serializer_class = RideSerializers
#     # permission_classes = [IsAuthenticated]
    
class RiderViewSet(generics.ListCreateAPIView):
    queryset = Rides.objects.all()
    serializer_class = RideSerializers
    # permission_classes = [IsAdminUser]

    # def list(self, request):
    #     queryset = self.get_queryset()
    #     serializer = RideSerializers(queryset, many=True)
    #     return Response(serializer.data)
