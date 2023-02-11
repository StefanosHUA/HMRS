from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.


admin.site.register(AcademicTitle)
admin.site.register(working_Relations)
admin.site.register(employee_Class)
admin.site.register(employeeSpecialization)
admin.site.register(grades)
admin.site.register(gradeTypes)
admin.site.register(WorkExperience)
admin.site.register(employeeType)
admin.site.register(salaryClass)
admin.site.register(generic_User, searchTest)
