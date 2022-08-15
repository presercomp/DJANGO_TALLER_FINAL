from django.shortcuts import render
from .serializers import ReservationSerializer
from .models import Reservation
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins, generics
from rest_framework import viewsets

# Create your views here. Reservations
class ReservationViewSets(viewsets.ModelViewSet):
    queryset = Reservation.objects.order_by('date','hour').all()
    serializer_class = ReservationSerializer

class ReservationList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Reservation.objects.order_by('date','hour').all()
    serializer_class = ReservationSerializer
    
    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)

class ReservationDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Reservation.objects.order_by('date','hour').all()
    serializer_class = ReservationSerializer
    
    def get(self, request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        return self.update(request, pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)