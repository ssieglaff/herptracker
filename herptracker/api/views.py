from api.models import *
from api.serializers import *
from django.http import Http404
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import permissions
from rest_framework import status
import json

# Create your views here.

class HerpList(APIView):
    # API endpoint for interating with the list of herp entries
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        print(request)
        user = authenticate(request.user, )
        if request.auth != None:
            herps = Herp.objects.all()
            serializer = HerpSerializer(herps, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request, format=None):
        serializer = HerpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HerpDetail(APIView):
    # API endpoint for interacting with a specific herp entry
    def get(self, request, herpid, format=None):
        herp = Herp.objects.get(id=herpid)
        serializer = HerpSerializer(herp)
        return Response(serializer.data)

    def put(self, request, herpid, format=None):
        herp = Herp.objects.get(id=herpid)

        herp.species = request.data.get('species')
        herp.sex = request.data.get('sex')
        herp.svl = request.data.get('svl')
        herp.tail = request.data.get('tail')
        herp.tibia = request.data.get('tibia')
        herp.notes = request.data.get('notes')

        try:
            herp.clean_fields()
        except ValidationError as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        
        herp.save()
        return Response(HerpSerializer(herp).data, status=status.HTTP_202_ACCEPTED)

    def delete(self, request, herpid, format=None):
        herp = Herp.objects.get(id=herpid)
        herp.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

class ObservationList(APIView):
    # API endpoint for interating with the list of observation entries
    def get(self, request, format=None):
        obs = Observation.objects.all()
        serializer = ObservationSerializer(obs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ObservationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ObservationDetail(APIView):
    # API endpoint for interacting with a specific observation entry
    def get(self, request, obsid, format=None):
        obs = Observation.objects.get(id=obsid)
        serializer = ObservationSerializer(obs)
        return Response(serializer.data)

    def put(self, request, obsid, format=None):
        obs = Observation.objects.get(id=obsid)

        obs.herp = Herp.objects.get(id=request.data.get('herp'))
        obs.trapType = request.data.get('trapType')
        obs.latitute = request.data.get('latitute')
        obs.longitude = request.data.get('longitude')
        obs.timeSet =  request.data.get('timeSet')
        obs.timeChecked = request.data.get('timeChecked')

        try:
            obs.clean_fields()
        except ValidationError as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        
        obs.save()
        return Response(ObservationSerializer(obs).data, status=status.HTTP_202_ACCEPTED)

    def delete(self, request, obsid, format=None):
        obs = Observation.objects.get(id=obsid)
        obs.delete()
        return Response(status=status.HTTP_202_ACCEPTED)