from django.http import JsonResponse
from .models import Letter
from .serializers import LetterSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.views.generic import ListView
from django.db.models import Q
from rest_framework import filters

class ListResultsView(generics.ListAPIView):
    queryset = Letter.objects.all().order_by('-created_at')
    serializer_class = LetterSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['recipient']
    http_method_names = ["get","post"]

    # def create_letter(request):
    #     if(request.method == 'POST'):
    #         serializer = LetterSerializer(data=request.data)
    #         if serializer.is_valid(raise_exception=True):
    #             serializer.save()
    #             return Response(serializer.data, status=status.HTTP_201_CREATED)

class LetterView(generics.ListAPIView):
    queryset = Letter.objects.all().order_by('-created_at')
    serializer_class = LetterSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('recipient')


@api_view(['POST'])
def create_letter(request):
            if(request.method == 'POST'):
                serializer = LetterSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def get_letter_by_id(request, id):

    try:
        letter = Letter.objects.get(pk=id)
    except Letter.DoesNotExist:
        return Response({"Not Found": "This id does not exist."}, status=status.HTTP_404_NOT_FOUND)
     
    if request.method == 'GET':
        serializer = LetterSerializer(letter)
        return Response(serializer.data)