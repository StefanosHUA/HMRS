from rest_framework import serializers, viewsets
from .models import  generic_User, working_Relations, AcademicTitle, WorkExperience, gradeTypes, employee_Class, employeeSpecialization, grades, salaryClass, employeeType



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = generic_User
        fields = ('user', 'givenName', 'surName', 'displayName', 'fathersName', 'mothersName', 'id', 'idIssuer', 'issueDate', 'birthDate', 'TIN', 'SSN', 'sex', 'nationality', 'address', 'homePhone', 'mobilePhone', 'email', 'workAddress',
        'workingRelationName', 'employeeClass', 'employeeSpec', 'salaryCl', 'empType', 'title', 'emp_Grades')


class WR(serializers.ModelSerializer):
    class Meta:
        model = working_Relations
        fields = ('fullName', 'shortName')

            
class Title(serializers.ModelSerializer):
    class Meta:
        model = AcademicTitle
        fields = ('acadTitle',)


class Experience(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = ('legal_status', 'organization', 'startDate', 'endDate', 'additional_info', 'grade', 'current_salaryClass', 'previous_salaryClass')


class fullGrade(serializers.ModelSerializer):
    class Meta:
        model = gradeTypes
        fields = ('_class', 'specialization', 'grade')


class emp_Speci(serializers.ModelSerializer):
    class Meta:
        model = employeeSpecialization
        fields = ('fullname', 'shortname')

    
class emp_Cl(serializers.ModelSerializer):
    class Meta:
        model = employee_Class
        fields = ('fullName', 'shortName')


class emp_Type(serializers.ModelSerializer):
    class Meta:
        model = employeeType
        fields = ('fulltTitle', 'shortTitle')