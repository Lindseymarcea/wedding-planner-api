from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Guestlist
from .serializers import GuestlistSerializer


# Create your views here.
# request handler- takes a request and gives a response
def say_hello(request):
    return HttpResponse('Hello World')

@api_view(['GET', 'POST'])
def guestlists_list(request):
    if request.method == 'GET':
        data = Guestlist.objects.all()
        print(data)

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


# def gift_registry(request):
#     if request.method == 'GET':
#         # <view logic>
#         return HttpResponse('result')

