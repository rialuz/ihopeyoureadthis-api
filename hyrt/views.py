from django.http import JsonResponse
from .models import Letter
from .serializers import LetterSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def letters_list(request):

    # get all letters
    # serialize them
    # return json
    if(request.method == 'GET'):
        letters = Letter.objects.all()
        serializer = LetterSerializer(letters, many=True)
        return Response(serializer.data)
    
    if(request.method == 'POST'):
        serializer = LetterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

@api_view(['GET'])
def get_letter_by_id(request, id):

    try:
        letter = Letter.objects.get(pk=id)
    except Letter.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
     
    if request.method == 'GET':
        serializer = LetterSerializer(letter)
        return Response(serializer.data)