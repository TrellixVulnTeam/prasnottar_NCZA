from rest_framework import serializers
#from rest_framework import employees
from . models import questions

class questionsSerializer(serializers.ModelSerializer):
	
	class Meta:
		model= questions
		fields =('question','courses')
		