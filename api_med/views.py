from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.status import HTTP_400_BAD_REQUEST,HTTP_404_NOT_FOUND,HTTP_200_OK
from rest_framework.authtoken.models import Token
from meds.forms import MedForm
from .serializers import MedSerializer
from meds.models import Medicine
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from accounts.forms import SignupForm

@api_view(['POST'])
@permission_classes((AllowAny,))
def signup(request):
    form=SignupForm(data=request.data)
    if form.is_valid():
        user=form.save()
        return Response("Account Created",status=status.HTTP_201_CREATED)
    return Response(form.errors,status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
@permission_classes((AllowAny,))
def api_login(request):
    username=request.data.get('username')
    password=request.data.get('password')
    if username is None or password is None:
        context={'error':'Provide Username and Password'}
        return Response(context,status=HTTP_400_BAD_REQUEST)
    user=authenticate(username=username,password=password)
    if not user:
        context={'error':'User Not Found'}
        return Response(context,status=HTTP_404_NOT_FOUND)
    token,_ =Token.objects.get_or_create(user=user)
    context={'token':token.key}
    return Response(context,status=HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def med_add(request):
    form=MedForm(request.POST)
    if form.is_valid():
        med=form.save()
        context={'id':med.id,'message':'Medicine Added'}
        return Response(context,status=status.HTTP_201_CREATED)
    else:
        return Response(form.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def med_edit(request,id):
    med=get_object_or_404(Medicine,id=id)
    form=MedForm(request.data,instance=med)
    if form.is_valid():
        form.save()
        serializer=MedSerializer(med)
        return Response(serializer.data)
    else:
        return Response(form.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def med_list(request):
    med=Medicine.objects.all()
    serializer=MedSerializer(med,many=True)
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def med_delete(request,id):
    try:
        med=Medicine.objects.get(id=id)
        med.delete()
        return Response("Medicine Deleted")
    except Medicine.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def med_search(request):
    if request.method=='GET':
        query=request.GET.get('query')
        med=Medicine.objects.filter(name__icontains=query)
        serializer=MedSerializer(med,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)        



