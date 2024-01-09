from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from .serializers import ItemSerializer
from .models import Item
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


# Create your views here.
@api_view(['GET'])
def index(request):
    return Response({"Status": "Working"})
@api_view(['GET','POST'])
def get_item_list(request):
    if request.method == 'GET':
        item_data = Item.objects.all()
        serializer = ItemSerializer(item_data, many=True)
        return Response({"Items": serializer.data})

    elif request.method == 'POST':
        data = request.data
        serializer = ItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def get_specific_item(request,id):
    if request.method == 'GET':
        try:
            item = Item.objects.filter(id=id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ItemSerializer(item, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        try:
            item = Item.objects.get(id=id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            item = Item.objects.get(id=id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(data={}, status=status.HTTP_405_METHOD_NOT_ALLOWED)