from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student 
from .serializers import StudentSerializer
from rest_framework.views import APIView
from rest_framework import status


@api_view(['GET','PUT','POST','PATCH','DELETE'])
def student_api(request, pk = None):
	if request.method == 'GET':
		#id = request.data.get('id')
		id = pk
		if id is not None:
			stu = Student.objects.get(id = id)
			serializer = StudentSerializer(stu)
			return Response(serializer.data)

		else:
			stu = Student.objects.all()
			serializer = StudentSerializer(stu , many = True )
			return Response(serializer.data)

	if request.method == 'POST':
		data = request.data 
		serializer = StudentSerializer(data = data)
		if serializer.is_valid():
			serializer.save()
			return Response({'msg' :'data validated'})	
		return Response(serializer.errors)
		

	if request.method == 'PUT':
		data = request.data 
		id = pk
		stu = Student.objects.get( pk =id)
		serializer = StudentSerializer(stu , data = data)  
		if serializer.is_valid():
			serializer.save()
			return Response({'msg':'completed updated'})
		else:
			return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


	if request.method == 'DELETE':
		id = request.data.get('id')
		stu = Student.objects.get(pk = id) 
		stu.delete()
		return Response({'msg':'data deleted'})

	   



	if request.method == 'PATCH':
		id = pk
		data = request.data
		stu = Student.objects.get(pk = id)
		serializer = StudentSerializer(stu,data =data , partial = True )
		if serializer.is_valid():
			serializer.save()
			return Response({'msg':'partial updated'})
		return Response(serializer.errors)             




		

	
