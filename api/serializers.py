from rest_framework import serializers
from users.models import User
from police.models import PoliceOfficer
from mortuary.models import Mortuary, MortuaryStaff
from stations.models import PoliceStation
from missing.models import MissingPerson
from unidentified.models import UnidentifiedBody

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class PoliceOfficerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoliceOfficer
        fields = '__all__'

class MortuarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Mortuary
        fields = '__all__'

class MortuaryStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = MortuaryStaff
        fields = '__all__'

class PoliceStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoliceStation
        fields = '__all__'

class MissingPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = MissingPerson
        fields = '__all__'

class UnidentifiedBodySerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidentifiedBody
        fields = '__all__'
