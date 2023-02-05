from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Guestlist, To_do, Cuisine, Song_choice
from .serializers import GuestlistSerializer, To_doSerializer, CuisineSerializer, Song_choiceSerializer

@api_view(['GET', 'POST'])
def guestlists_list(request):
    if request.method == 'GET':
        data = Guestlist.objects.all()

        serializer = GuestlistSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = GuestlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def guestlist_detail(request, pk):
    try:
        guestlist = Guestlist.objects.get(pk=pk)
    except Guestlist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = GuestlistSerializer(guestlist, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        guestlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# TO_DO

@api_view(['GET', 'POST'])
def to_do_list(request):
    if request.method == 'GET':
        data = To_do.objects.all()

        serializer = To_doSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = To_doSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def to_do_detail(request, pk):
    try:
        to_do = To_do.objects.get(pk=pk)
    except To_do.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = To_doSerializer(to_do, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        to_do.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Cuisine
@api_view(['GET', 'POST'])
def cuisine_list(request):
    if request.method == 'GET':
        data = Cuisine.objects.all()

        serializer = CuisineSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CuisineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def cuisine_detail(request, pk):
    try:
        cuisine = Cuisine.objects.get(pk=pk)
    except Cuisine.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = CuisineSerializer(cuisine, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cuisine.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# Song_choice
@api_view(['GET', 'POST'])
def song_choice_list(request):
    if request.method == 'GET':
        data = Song_choice.objects.all()

        serializer = Song_choiceSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = Song_choiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def song_choice_detail(request, pk):
    try:
        song_choice = Song_choice.objects.get(pk=pk)
    except Song_choice.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = Song_choiceSerializer(song_choice, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        song_choice.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)