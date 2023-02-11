from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import generic_User, working_Relations, AcademicTitle, WorkExperience, gradeTypes, employee_Class, employeeSpecialization, grades, salaryClass, employeeType
from .serializer import UserSerializer, WR, Title, Experience, fullGrade, emp_Speci, emp_Cl, emp_Type
# Create your views here.

#GET

@api_view(['GET'])
def getUser(request):
    user = generic_User.objects.all()
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getTitle(request):
    title = AcademicTitle.objects.all()
    title_seri = Title(title, many=True)
    return Response(title_seri.data)


@api_view(['GET'])
def getExperience(request):
    exp = WorkExperience.objects.all()
    exp_serial = Experience(exp, many=True)
    return Response(exp_serial.data)



@api_view(['GET'])
def getGrade_Types(request):
    grade = gradeTypes.objects.all()
    grade_Seri = fullGrade(grade, many=True)
    return Response(grade_Seri.data)

# ----------------------------------------
#NEW GETS

@api_view(['GET'])
def getWorking_Relation(request):
    workRL = working_Relations.objects.all()
    workRL_serial = WR(workRL, many=True)
    return Response(workRL_serial.data)



@api_view(['GET'])
def getSpecialization(request):
    Spec = employeeSpecialization.objects.all()
    Spec_Seri = emp_Speci(Spec, many=True)
    return Response(Spec_Seri.data)


@api_view(['GET'])
def getEmpClass(request):
    empClass = employee_Class.objects.all()
    class_Seri = emp_Cl(empClass, many=True)
    return Response(class_Seri.data)


@api_view(['GET'])
def getEmpType(request):
    Type = employeeType.objects.all()
    Type_Seri = emp_Type(Type, many=True)
    return Response(Type_Seri.data)



@api_view(['GET'])
def getGrade_Types(request):
    grade = gradeTypes.objects.all()
    grade_Seri = fullGrade(grade, many=True)
    return Response(grade_Seri.data)


@api_view(['GET'])
def getGrade_Types(request):
    grade = gradeTypes.objects.all()
    grade_Seri = fullGrade(grade, many=True)
    return Response(grade_Seri.data)


grades, salaryClass, employeeType


#POST


@api_view(['POST'])
def postUser(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_vald():
        serializer.save()
        return Response(serializer.data)



@api_view(['POST'])
def postWR(request):
    serializer1 = WR(data=request.data)
    if serializer1.is_vald():
        serializer1.save()
        return Response(serializer1.data)




@api_view(['POST'])
def postTitle(request):
    title_seri = Title(data=request.data)
    if title_seri.is_vald():
        title_seri.save()
        return Response(title_seri.data)