from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Klub, Liga, Piłkarz, Agent


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'password']
        extra_kwargs = {'password': {'required': True, 'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class LigaMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Liga
        fields = '__all__'

class KlubSerializer(serializers.ModelSerializer):
    liga = LigaMiniSerializer(many=False, read_only=True)
    class Meta:
        model = Klub
        fields = '__all__'

class KlubMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Klub
        fields = ['nazwa', 'miasto']

class LigaSerializer(serializers.ModelSerializer):
    kluby = KlubMiniSerializer(many=True, read_only=True)
    class Meta:
        model = Liga
        fields = ['id', 'kraj',  'nazwa', 'kluby']

class PiłkarzSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piłkarz
        fields = '__all__'
        depth = 2

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = '__all__'