from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from users.models import User
from police.models import PoliceOfficer
from mortuary.models import Mortuary, MortuaryStaff
from stations.models import PoliceStation
from missing.models import MissingPerson
from unidentified.models import UnidentifiedBody
from .serializers import UserSerializer, PoliceOfficerSerializer, MortuarySerializer, MortuaryStaffSerializer, PoliceStationSerializer, MissingPersonSerializer, UnidentifiedBodySerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PoliceOfficerViewSet(viewsets.ModelViewSet):
    queryset = PoliceOfficer.objects.all()
    serializer_class = PoliceOfficerSerializer

class MortuaryViewSet(viewsets.ModelViewSet):
    queryset = Mortuary.objects.all()
    serializer_class = MortuarySerializer

class MortuaryStaffViewSet(viewsets.ModelViewSet):
    queryset = MortuaryStaff.objects.all()
    serializer_class = MortuaryStaffSerializer

class PoliceStationViewSet(viewsets.ModelViewSet):
    queryset = PoliceStation.objects.all()
    serializer_class = PoliceStationSerializer

class MissingPersonViewSet(viewsets.ModelViewSet):
    queryset = MissingPerson.objects.all()
    serializer_class = MissingPersonSerializer

class UnidentifiedBodyViewSet(viewsets.ModelViewSet):
    queryset = UnidentifiedBody.objects.all()
    serializer_class = UnidentifiedBodySerializer

