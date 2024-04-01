from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated , AllowAny
from django.contrib.auth import get_user_model
from rest_framework import exceptions
from .models import metadata,document
from rest_framework.decorators import parser_classes
from rest_framework.parsers import FileUploadParser
from django.http import HttpResponse
from .serializer import FileSerializer






class register(APIView):
    permission_classes = (AllowAny, ) 

    def post(self, request):
        User = get_user_model()
        email = request.data.get('email')
        password = request.data.get('password')
        if  (email is None) or (password is None):
            raise exceptions.AuthenticationFailed(
                'email and password required')
        user = User.objects.filter(email=email).first()
        if user is None:
            user =  User.objects.create_user(email=email,username=email,password=password)
            user.save()
            return Response({'message': 'User created successfully' })
        else:
            raise exceptions.AuthenticationFailed(
                'this email already exist')

class upload_metadata(APIView):
    permission_classes = (IsAuthenticated, )
    def post(self, request):
        name = request.data.get('name')
        string = request.data.get('string')
        if (name is None) or (string is None):
            raise exceptions.AuthenticationFailed('name and string are required')
        if metadata.objects.filter(name=name).first() is None:
            meta = metadata.objects.create(name=name,string=string)
            meta.save()
            content = {'message': 'Meta Data Uploaded Successfully'}
            return Response(content)
        else:
            raise exceptions.AuthenticationFailed('this metadata already exist')
		
class get_metadata(APIView):
    permission_classes = (IsAuthenticated, )
    def get(self, request):
        name = request.data.get('name')
        if (name is None) :
            raise exceptions.AuthenticationFailed('name is required')
        meta = metadata.objects.filter(name=name).first()
        if meta is None:
            raise exceptions.AuthenticationFailed('this metadata is not exist') 
        else:
            content = {'metadta': {'id':meta.id,'name':meta.name,'string':meta.string}}
            return Response(content)


class get_all_metadata(APIView):
    permission_classes = (IsAuthenticated, )
    def get(self, request):
        
        meta = metadata.objects.all()
        if meta.count() < 1:
            raise exceptions.AuthenticationFailed('there are no any metadata') 
        else:
            meta_data =[]
            for m in meta:
                meta_data.append({
                    'id':m.id,'name':m.name,'string':m.string
                })
            content = {'metadta':meta_data}
            return Response(content)


class FileUploadView(APIView):
    parser_classes = [FileUploadParser]
    permission_classes = (IsAuthenticated, )

    def post(self, request, filename, format=None):
        file_obj = request.data['file']
        if file_obj is None:
            raise exceptions.AuthenticationFailed('There is no file added') 
        doc = document.objects.create(name=filename,doc=file_obj)
        doc.save()
        content={
            'message': 'data uploaded successfully'
        }
        return Response(content)

class get_documents(APIView):
    parser_classes = [FileUploadParser]
    permission_classes = (IsAuthenticated, )

    def get(self, request, format=None):
        docs = document.objects.all()
        documents=[]
        for d in docs:
            documents.append({
                'id':d.id,
                'name':d.name,
                'file':d.doc.url
            })
        content={
            'data':documents
        }
        return Response(content)


class get_document(APIView):
    parser_classes = [FileUploadParser]
    permission_classes = (IsAuthenticated, )

    def get(self, request,filename, format=None):
        doc = document.objects.filter(name=filename).first()
        if doc is None:
            raise exceptions.AuthenticationFailed(
                'file not exist')
        data = FileSerializer(doc)
        return Response({'data':data.data})
        
