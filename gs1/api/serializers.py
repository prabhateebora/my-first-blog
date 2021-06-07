from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
	#name = serializers.CharField(read_only = True )
	#name = serializers.Charfield(validators = [start_with_r])
	#validators
	'''def start_with_r(value):
		if value[0].lower() != 'r':
			raise serializers.ValidationError("the starting leter should be R")
		else :
			return value 
			'''	


	class Meta:
		model = Student 
		fields = ['name','roll','city']
		#read_only_fields= ['name' , 'roll']
		extra_kwargs = {'name': {'read_only' : True}}








'''
#validators
def start_with_r( value):
	if value[0].lower() != 'r':
		raise serializers.ValidationError("the starting leter should be R")
	else :
		return value 	



class StudentSerializer(serializers.Serializer):
	id = serializers.IntegerField()
	name = serializers.CharField(max_length = 100, validators = [start_with_r])
	roll = serializers.IntegerField()
	city = serializers .CharField(max_length = 100)





	def create(self, validate_data):
		return Student.objects.create(**validate_data)




	def update(self, instance, validate_data ):
		print(instance.name)
		print(validate_data)
		instance.name = validate_data.get('name',instance.name)
		print(instance.name)
		instance.roll = validate_data.get('roll',instance.roll)
		instance.city = validate_data.get('city',instance.city)
		instance.save()
		return instance

	#field validation
	def validate_roll(self, value):
		if value > 200:
			raise serializers.ValidationError("seat full")
		else :
			return value   
	#object validation
	def validate (self, data):
		nm = data.get('name')
		ct = data.get('city')
		if nm.lower()=='rohit' and ct.lower() != 'ranchi':
			raise serializers.ValidationError("city must be ranchi")
		else :
			return data  


'''






