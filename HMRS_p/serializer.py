from rest_framework import serializers, viewsets
from .models import  *

#gradeTypes,working_Relations, AcademicTitle,employee_Class, employeeSpecialization,

class UserSerializer(serializers.ModelSerializer):
    #'employeeClass', 'employeeSpec', 'salaryCl', 'emp_Grades'
    class Meta:
        model = generic_User
        fields = ('user', 'givenName', 'surName', 'displayName', 'fathersName', 'mothersName', 'id', 'idIssuer', 'issueDate', 'birthDate', 'TIN', 'SSN', 'sex', 'nationality', 'address', 'homePhone', 'mobilePhone', 'email', 'workAddress',
        'general_emp_Type', 'specific_emp_Type')


class gradesSer(serializers.ModelSerializer):
    class Meta:
        model = grades
        fields = '__all__'

            
class Previous_Salary_Class(serializers.ModelSerializer):
    class Meta:
        model = salaryClass
        fields = '__all__'


class Experience(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = '__all__'


    
class empSpecificType(serializers.ModelSerializer):
    class Meta:
        model = employeeSpecificType
        fields = '__all__'


class emp_Type(serializers.ModelSerializer):
    class Meta:
        model = employeeType
        fields = ('myUser', 'fulltTitle', 'shortTitle')

#ΔΕΠ 
class DEP(serializers.ModelSerializer):
    class Meta:
        model = depProfile
        fields = '__all__'


#ΔΙΟΙΚΗΤΙΚΟ ΠΡΟΣΩΠΙΚΟ
class DP(serializers.ModelSerializer):
    class Meta:
        model = DPprofile
        fields = '__all__'
       
