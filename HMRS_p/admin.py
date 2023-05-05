from django.contrib import admin
from django.contrib.auth.admin import UserAdmin # type: ignore
from .models import *
from import_export.admin import ExportActionMixin
# Register your models here.


#TitleInline, empTypeInline,

class DPprofile(admin.StackedInline):
    model = DPprofile
    extra = 0

class DEPprofile(admin.StackedInline):
    model = depProfile
    extra = 0

class WorkExpirienceInline(admin.StackedInline):
    model = WorkExperience
    extra = 0

class UserAdmin(ExportActionMixin, admin.ModelAdmin):
    

    inlines = [WorkExpirienceInline, DPprofile, DEPprofile]
    search_fields = ['givenName', 'displayName', 'surName', 'TIN', 'id']
    list_display = ['displayName', 'id']
    list_filter = ['address', 'general_emp_Type']

#gradesInline, Employee_ClassInline, SpecInline, salaryClassInline

# admin.site.register(AcademicTitle)
# admin.site.register(working_Relations)
# admin.site.register(employee_Class)
# admin.site.register(employeeSpecialization)
admin.site.register(employeeSpecificType)
admin.site.register(grades)
admin.site.register(WorkExperience) #UserAdmin
admin.site.register(employeeType)
admin.site.register(salaryClass)
admin.site.register(generic_User, UserAdmin)
