from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt 
from django.utils.decorators import method_decorator
import io 
from rest_framework import status
from django.views import View




# model object - sigle student data


"""def student_details(request, pk):
	stu = Student.objects.get(id = pk )
	#print(stu)
	serializer = StudentSerializer(stu)
	#print(serializer)
	json_data = JSONRenderer().render(serializer.data) 
	#print(jason_data)
	return HttpResponse(json_data, content_type='application/json')
	#return JsonResponse(serializer.data)






	#queryset- all student data

def student_list(request):
	stu = Student.objects.all()
	#print(stu)
	serializer = StudentSerializer(stu, many = True)
	#print(serializer)
	json_data = JSONRenderer().render(serializer.data) 
	#print(jason_data)
	return HttpResponse(json_data, content_type='application/json')
	#return JsonResponse(serializer.data, safe = True)



@csrf_exempt
def student_create(request):
	if request.method == 'POST':
		json_data = request.body
		stream = io.BytesIO(json_data )
		pythondata = JSONParser().parse(stream)
		serializer = StudentSerializer(data=pythondata )
		if serializer.is_valid():
			serializer.save()
			res ={'msg':'data created' }
			json_data = JSONRenderer().render(res)
			return HttpResponse(json_data, content_type='applications/json') 
		else :
			json_data = JSONRenderer().render(serializer.errors)
			return HttpResponse(json_data, content_type='applications/json')



@csrf_exempt
def studentapi(request):
	if request.method == 'GET' :

		json_data = request.body
		stream = io.BytesIO(json_data)
		pythondata = JSONParser().parse(stream)
		id = pythondata.get('id' , None)
		if id is not None:
			stu = Student.objects.get(id = id )
			serializer = StudentSerializer(stu)
			json_data = JSONRenderer().render(serializer.data)
			return HttpResponse(json_data, content_type = 'application/json')

		else :
			stu = Student.objects.all() 
			serializer = StudentSerializer(stu, many = True)
			json_data = JSONRenderer().render(serializer.data)
			return HttpResponse(json_data , content_type='application/json')

	if request.method == 'POST':
		json_data = request.body
		stream = io.BytesIO(json_data)
		pythondata = JSONParser().parse(stream)
		serializer = StudentSerializer(data= pythondata)
		if serializer.is_valid():
			serializer.save()
			res = {
			'msg'  : 'data created',
			}
			json_data = JSONRenderer().render(res)
			return HttpResponse(json_data, content_type='application/json')

		else :
			json_data = JSONRenderer().render(serializer.errors)
			return HttpResponse(json_data , content_type ='application/json')

	if request.method == 'PUT':
		json_data = request.body
		stream = io.BytesIO(json_data)
		pythondata = JSONParser().parse(stream)
		id = pythondata.get('id')
		stu = Student.objects.get(id = id)
		serializer = StudentSerializer(stu, data = pythondata, partial = True )
		if serializer.is_valid():
			serializer.save()
			print(serializer)
			res ={ 'msg' :'data is updated'}
			json_data = JSONRenderer().render(res)
			return HttpResponse (json_data ,content_type= 'application/json')
		else:
			json_data = JSONRenderer().render(serializer.errors)
			return HttpResponse (json_data ,content_type= 'application/json')    


	if request.method == 'DELETE' :
		json_data = request.body 
		stream = io.BytesIO(json_data)
		pythondata = JSONParser().parse(stream)
		id = pythondata.get('id')
		stu = Student.objects.get(id = id)
		stu.delete()
		res ={ 'msg' :'data is deleted'}
		json_data = JSONRenderer().render(res)
		return HttpResponse (json_data ,content_type= 'application/json')
"""
@method_decorator(csrf_exempt, name ='dispatch')
class StudentAPI(View): 
	def get(self, request, *args, **kwargs):
		json_data = request.body
		stream = io.BytesIO(json_data)
		pythondata = JSONParser().parse(stream)
		id = pythondata.get('id' , None)
		if id is not None:
			stu = Student.objects.get(id = id )
			serializer = StudentSerializer(stu)
			json_data = JSONRenderer().render(serializer.data)
			return HttpResponse(json_data, content_type = 'application/json')

		else :
			stu = Student.objects.all() 
			serializer = StudentSerializer(stu, many = True)
			json_data = JSONRenderer().render(serializer.data)
			return HttpResponse(json_data , content_type='application/json')
	def post(self, request, *args, **kwargs):  
		json_data = request.body
		stream = io.BytesIO(json_data)
		pythondata = JSONParser().parse(stream)
		serializer = StudentSerializer(data= pythondata)
		if serializer.is_valid():
			serializer.save()
			res = {
			'msg'  : 'data created',
			}
			json_data = JSONRenderer().render(res)
			return HttpResponse(json_data, content_type='application/json')

		else :
			json_data = JSONRenderer().render(serializer.errors)
			return HttpResponse(json_data , content_type ='application/json')
	def put(self, request, *args, **kwargs): 
		json_data = request.body
		stream = io.BytesIO(json_data)
		pythondata = JSONParser().parse(stream)
		id = pythondata.get('id')
		stu = Student.objects.get(id = id)
		serializer = StudentSerializer(stu, data = pythondata, partial = True )
		if serializer.is_valid():
			serializer.save()
			print(serializer)
			res ={ 'msg' :'data is updated'}
			json_data = JSONRenderer().render(res)
			return HttpResponse (json_data ,content_type= 'application/json')
		else:
			json_data = JSONRenderer().render(serializer.errors)
			return HttpResponse (json_data ,content_type= 'application/json')   




	def delete(self, request, *args, **kwargs): 
		json_data = request.body

		json_data = request.body 
		stream = io.BytesIO(json_data)
		pythondata = JSONParser().parse(stream)
		id = pythondata.get('id')
		stu = Student.objects.get(id = id)
		stu.delete()
		res ={ 'msg' :'data is deleted'}
		json_data = JSONRenderer().render(res)
		return HttpResponse (json_data ,content_type= 'application/json')
	 

		
			  




		





		 






		
	   






