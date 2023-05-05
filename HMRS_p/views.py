from django.views.generic import ListView, CreateView, UpdateView
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializer import *
#gradeTypes,

#fullGrade,working_Relations, AcademicTitle,employee_Class, employeeSpecialization,WR, Title,emp_Speci, emp_Cl,

# Create your views here.

#GET

@api_view(['GET'])
def getUser(request):
    user = generic_User.objects.all()
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getSpecType(request):
    title = employeeSpecificType.objects.all()
    title_seri = empSpecificType(title, many=True)
    return Response(title_seri.data)


@api_view(['GET'])
def getExperience(request):
    exp = WorkExperience.objects.all()
    exp_serial = Experience(exp, many=True)
    return Response(exp_serial.data)



@api_view(['GET'])
def getPreviousGrades(request):
    grade = grades.objects.all()
    grade_Seri = gradesSer(grade, many=True)
    return Response(grade_Seri.data)



@api_view(['GET'])
def getPrevious_Salary_Class(request):
    workRL = salaryClass.objects.all()
    salary_CLass = Previous_Salary_Class(workRL, many=True)
    return Response(salary_CLass.data)

# ----------------------------------------
#NEW GETS


@api_view(['GET'])
def getDEP(request):
    Spec = depProfile.objects.all()
    Spec_Seri = DEP(Spec, many=True)
    return Response(Spec_Seri.data)


@api_view(['GET'])
def getDP(request):
    empClass = DPprofile.objects.all()
    class_Seri = DP(empClass, many=True)
    return Response(class_Seri.data)


@api_view(['GET'])
def getEmpType(request):
    Type = employeeType.objects.all()
    Type_Seri = emp_Type(Type, many=True)
    return Response(Type_Seri.data)



#POST


@api_view(['POST'])
def postUser(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

