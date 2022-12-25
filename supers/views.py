from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperSerializer
from .models import Super

@api_view(['GET', 'POST'])
def supers_list(request):

    if request.method == 'GET':
        super_type = request.query_params.get('super_type')
        print(super_type)
        super_types = Super.objects.all()
            
        if super_type:
            super_types = super_types.filter(super_type__type = super_type)

        serializer = SuperSerializer(super_types, many=True)
        return Response(serializer.data)

        
    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def heroes_and_villains(request):

    heroes = Super.objects.filter(super_type=1)
    villains = Super.objects.filter(super_type=2)

    heroes_serializer = SuperSerializer(heroes, many = True)
    villains_serializer = SuperSerializer(villains, many = True)

    custom_response_dict = {
        'heroes:' : heroes_serializer.data,
        'villains' : villains_serializer.data
    }

    return Response(custom_response_dict)


@api_view(['GET', 'PUT', 'DELETE'])
def supers_detail(request, pk):
    product = get_object_or_404(Super, pk=pk)
    if request.method == "GET":
        serializer = SuperSerializer(product)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = SuperSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# @api_view(['GET'])
# def supers_detail(request, pk):
#     try:
#         super = Super.objects.get(pk=pk)
#         serializer = SuperSerializer(super)
#         return Response (serializer.data)
#     except Super.DoesNotExist:
#         return Response (status = status.HTTP_404_NOT_FOUND)