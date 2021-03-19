from django.contrib.auth.models import User, Group
from rest_framework import viewsets, filters
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import UserSerializer, KlubSerializer, LigaSerializer, PiłkarzSerializer, AgentSerializer
from .models import Klub, Liga, Piłkarz, Agent


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]


class KlubViewSet(viewsets.ModelViewSet):
    queryset = Klub.objects.all()
    serializer_class = KlubSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['nazwa', 'miasto']
    search_fields = ['nazwa', 'miasto']


class LigaViewSet(viewsets.ModelViewSet):
    queryset = Liga.objects.all()
    serializer_class = LigaSerializer


class PiłkarzViewSet(viewsets.ModelViewSet):
    queryset = Piłkarz.objects.all()
    serializer_class = PiłkarzSerializer

    def create(self, request, *args, **kwargs):
        piłkarz = Piłkarz.objects.create(imie=request.data['imie'],
                                         nazwisko=request.data['nazwisko'],
                                         data_urodzenia=request.data['data_urodzenia'],
                                         pozycja=request.data['pozycja'],
                                         czy_aktywny=request.data['czy_aktywny'])
        serializer = PiłkarzSerializer(piłkarz, many=False)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        piłkarz = self.get_object()
        piłkarz.imie = request.data['imie']
        piłkarz.nazwisko = request.data['nazwisko']
        piłkarz.data_urodzenia = request.data['data_urodzenia']
        piłkarz.pozycja = request.data['pozycja']
        piłkarz.czy_aktywny = request.data['czy_aktywny']
        piłkarz.save()
        serializer = PiłkarzSerializer(piłkarz, many=False)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def modyfikuj_klub(self, request, **kwargs):
        piłkarz = self.get_object()
        klub = Klub.objects.get(id=request.data['klub'])
        piłkarz.klub = klub
        piłkarz.save()
        serializer = PiłkarzSerializer(piłkarz, many=False)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def modyfikuj_agenta(self, request, **kwargs):
        piłkarz = self.get_object()
        agent = Agent.objects.get(id=request.data['agent'])
        piłkarz.agent = agent
        piłkarz.save()
        serializer = PiłkarzSerializer(piłkarz, many=False)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def zmien_aktywnosc(self, request, **kwargs):
        piłkarz = self.get_object()
        piłkarz.czy_aktywny = request.data['czy_aktywny']
        piłkarz.save()
        serializer = PiłkarzSerializer(piłkarz, many=False)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        piłkarz = self.get_object()
        piłkarz.delete()
        return Response("piłkarz usunięty")


class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

    def create(self, request, *args, **kwargs):
        agent = Agent.objects.create(imie=request.data['imie'],
                                     nazwisko=request.data['nazwisko'])
        serializer = AgentSerializer(agent, many=False)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        agent = self.get_object()
        agent.imie = request.data['imie']
        agent.nazwisko = request.data['nazwisko']
        serializer = AgentSerializer(agent, many=False)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        agent = self.get_object()
        agent.delete()
        return Response("Agent usunięty")
