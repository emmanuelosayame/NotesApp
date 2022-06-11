from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
#from rest_framework.serializers import serializer
from .serializers import NoteSerializer
from .models import Note

@api_view(['GET', 'POST'])
def notes(request):

   if request.method == 'GET':
      notesdata = Note.objects.all().order_by('-updated')
      serializer = NoteSerializer(notesdata , many=True)
      return Response(serializer.data)

   if request.method == 'POST':
      data = request.data
      notedata = Note.objects.create(body = data['body'])
      serializer = NoteSerializer(notedata, many=False)
      return Response(serializer.data)

@api_view(['GET' , 'PUT' , 'DELETE'])
def note(request, pk):

   if request.method == 'GET':
      notedata = Note.objects.get(id=pk)
      serializer = NoteSerializer(notedata, many=False)
      return Response(serializer.data)

   if request.method == 'PUT':
      data = request.data
      notedata = Note.objects.get(id=pk)
      serializer = NoteSerializer(data=data, instance=notedata)
      if serializer.is_valid():
          serializer.save()
      return Response(serializer.data)
   
   if request.method == 'DELETE':
      notedata = Note.objects.get(id=pk)
      notedata.delete()
      return Response('yikes')
