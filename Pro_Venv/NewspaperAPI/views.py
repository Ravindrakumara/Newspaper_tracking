from django.shortcuts import render
from django.http import FileResponse
from reportlab.pdfgen import canvas
from django.db.models import Model
from rest_framework import viewsets,status
from .models import Consumer,Newspaper,Intake,User#,Daily_Cart ,Order
from .serializers import NewspaperSerializer, \
    IntakeSerializer, ConsumerSerializer, UserSerializer# RegiSerializer' OrderSerializer,

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class NewspaperViewSet(viewsets.ModelViewSet):
    queryset = Newspaper.objects.all()
    serializer_class = NewspaperSerializer

class IntakeViewSet(viewsets.ModelViewSet):
    queryset = Intake.objects.all()
    serializer_class = IntakeSerializer

class ConsumerViewSet(viewsets.ModelViewSet):
    queryset = Consumer.objects.all()
    serializer_class = ConsumerSerializer



