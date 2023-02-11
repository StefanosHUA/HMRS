from datetime import date, timezone
from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib import admin
from rest_framework import filters, generics
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Create your models here.

substring = 'hua'

def validate_email(value):
    if substring not in value:
        raise ValidationError(
            _('%(value)s is not a valid HUA email'),
            params={'value': value},
        )


SEX_Choices = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
)

Working_Relations = (
    ('Μόνιμος Υπάλληλος', 'Μόνιμος Υπάλληλος'),
    ('Ιδιωτικού δικαίου αορίστου χρόνου', 'Ιδιωτικού δικαίου αορίστου χρόνου'),
    ('Ιδιωτικού δικαίου ορισμένου χρόνου', 'Ιδιωτικού δικαίου ορισμένου χρόνου'),
    ('Σύμβαση εργασίας', 'Σύμβαση εργασίας'),

)

Working_Relations_short = (
    ('ΜΥ', 'ΜΥ'),
    ('ΙΔΑΧ', 'ΙΔΑΧ'),
    ('ΙΔΟΧ', 'ΙΔΟΧ'),
    ('ΣΕ', 'ΣΕ'),

)

emp_Class = (
    ('Πανεπιστημιακής Εκπαίδευση', 'Πανεπιστημιακής Εκπαίδευσης'),
    ('Τεχνολογικής Εκπαίδευσης', 'Τεχνολογικής Εκπαίδευσης'),
    ('Δευτεροβάθμιας Εκπαίδευσης', 'Δευτεροβάθμιας Εκπαίδευσης'),
    ('Υποχρεωτικής Εκπαίδευσης', 'Υποχρεωτικής Εκπαίδευσης'), 
)

emp_Class_short = (
    ('ΠΕ', 'ΠΕ'),
    ('ΤΕ', 'ΤΕ'),
    ('ΔΕ', 'ΔΕ'),
    ('ΥΕ', 'ΥΕ'), 
)


emp_Spec = (
    ('Διοικητικού - Οικονομικού', 'Διοικητικού - Οικονομικού'),
    ('Πληροφορικής', 'Πληροφορικής'),
    ('Διοικητικού - Λογιστικού', 'Διοικητικού - Λογιστικού'),
    ('Βιβλιοθηκονόμων', 'Βιβλιοθηκονόμων'),
    ('Μηχανικών', 'Μηχανικών'),
    ('Επιμελητών', 'Επιμελητών'),
)

emp_Spec_short = (
    ('ΔΟ', 'ΔΟ'),
    ('ΠΛΗ', 'ΠΛΗ'),
    ('ΔΛ', 'ΔΛ'),
    ('ΒΙ', 'ΒΙ'),
    ('ΜΗΧ', 'ΜΗΧ'),
    ('ΕΠΙ', 'ΕΠΙ'),
)


grades_full = (
    ('ΒΑΔΜΙΔΑ Α', 'ΒΑΔΜΙΔΑ Α'),
    ('ΒΑΔΜΙΔΑ Β', 'ΒΑΔΜΙΔΑ Β'),
)

grades_short = (
    ('Α', 'Α'),
    ('Β', 'Β')
)



type = (
    ('Διδακτικό Ερευνητικό Προσωπικό', 'Διδακτικό Ερευνητικό Προσωπικό'),
    ('Εργαστηριακό Διδακτικό Προσωπικό', 'Εργαστηριακό Διδακτικό Προσωπικό'),
    ('Ειδικό Τεχνικό Εργαστηριακό Προσωπικό', 'Ειδικό Τεχνικό Εργαστηριακό Προσωπικό'),
    ('Διοικητικό Προσωπικό', 'Διοικητικό Προσωπικό'),
    ('Υπάλληλοι με απόσπαση', 'Υπάλληλοι με απόσπαση'),
    ('Εντεταλμένοι Διδάσκοντες', 'Εντεταλμένοι Διδάσκοντες'),
)

short_type = (
    ('ΔΕΠ', 'ΔΕΠ'),
    ('ΕΔΙΠ', 'ΕΔΙΠ'),
    ('ΕΤΕΠ', 'ΕΤΕΠ'),
    ('ΔΠ', 'ΔΠ'),
    ('YA', 'YA'),
    ('ΕΔ', 'ΕΔ'),
)


legal_status = (
    ('Ιδιωτικός', 'Ιδιωτικός'),
    ('Δημόσιος', 'Δημόσιος'),
)



titles = (
    ('Επίκουρος Καθηγητής επί θητεία', 'Επίκουρος Καθηγητής επί θητεία'),
    ('Μόνιμος Επίκουρος Καθηγητής', 'Μόνιμος Επίκουρος Καθηγητής'),
    ('Αναπληρωτής Καθηγητής', 'Αναπληρωτής Καθηγητής'),
    ('Καθηγητής Α Βαθμίδας', 'Καθηγητής Α Βαθμίδας'),
    ('Α - Δ Εισαγωγική Δ', 'Α - Δ Εισαγωγική Δ'),
    ('Α - Ε Εισαγωγική Ε', 'Α - Ε Εισαγωγική Ε'),
    ('Καμία Τιμή', 'Καμία Τιμή'),
)




class working_Relations(models.Model):
    fullName = models.CharField(max_length=100, choices=Working_Relations, default=None)
    shortName = models.CharField(max_length=100, choices=Working_Relations_short, default = None)
    def __str__(self):
        return self.fullName
   
    
class AcademicTitle(models.Model):
    acadTitle = models.CharField(choices=titles, max_length=200, default=None) 
    def __str__(self):
        return self.acadTitle

class employee_Class(models.Model):
    fullName = models.CharField(max_length=100, choices=emp_Class, default=None)
    shortName = models.CharField(max_length=100, choices = emp_Class_short, default = None)
    def __str__(self):
        return self.fullName



class employeeSpecialization(models.Model):
    fullname = models.CharField(max_length=100, choices=emp_Spec, default=None)
    shortname = models.CharField(max_length=100, choices = emp_Spec_short, default = None)
    def __str__(self):
        return self.fullname


class grades(models.Model):
    gradeFullName = models.CharField(max_length=100, choices=grades_full, default=None)
    gradeShortName = models.CharField(max_length=100, choices = grades_short, default = None)

    def __str__(self):
        return self.gradeFullName


class salaryClass(models.Model):
    shortName = models.CharField(max_length=100, default=None)
    fullName = models.CharField(max_length=100, default = None)

    def __str__(self):
        return self.fullName


class employeeType(models.Model):
    fulltTitle = models.CharField(max_length=100, choices=type, default=None)
    shortTitle = models.CharField(max_length=100, choices = short_type, default = None)

    def __str__(self):
        return self.fulltTitle

disname = 'givenName' + ' ' + 'surName'

class WorkExperience(models.Model):
    legal_status = models.CharField(max_length=100, choices = legal_status, default = None)
    organization = models.CharField(max_length=100, default = None)
    startDate = models.DateField(default=None)
    endDate = models.DateField(default = None)
    additional_info = models.TextField(default = None)
    grade = models.ForeignKey(grades, null=True, on_delete=models.CASCADE)
    current_salaryClass = models.ForeignKey(salaryClass, null=True, on_delete=models.CASCADE)
    previous_salaryClass = models.CharField(max_length=100, default = None)

    def __str__(self):
        return self.organization

    

class gradeTypes(models.Model):
    _class = models.ForeignKey(employee_Class, null=True, on_delete=models.CASCADE)
    specialization = models.ForeignKey(employeeSpecialization, null=True, on_delete=models.CASCADE)
    grade = models.ForeignKey(grades, null=True, on_delete=models.CASCADE)    

    # def __str__(self):
    #     return self._class

 

class generic_User(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    givenName = models.CharField(max_length=100, default = None, null=True)
    surName = models.CharField(max_length=100, default = None, null=True)
    displayName = models.CharField(max_length=1000, default =  None, null=True)
    fathersName = models.CharField(max_length=1000, default=None, null=True)
    mothersName = models.CharField(max_length=100000, default = None, null=True)
    id = models.CharField(max_length=20000, primary_key=True)
    idIssuer = models.CharField(max_length=50000, default = None, null=True)
    issueDate = models.DateField(max_length=200, default = None, null=True )
    birthDate = models.DateField(max_length=200, default = None, null=True)
    TIN = models.IntegerField(default = None, null=True)
    SSN = models.IntegerField(default=None, null=True)
    sex = models.CharField(choices=SEX_Choices, max_length=1000, default = None, null=True)
    nationality = CountryField()
    address = models.CharField(max_length=100, default=None, null=True)
    homePhone = models.IntegerField(default = None, null=True)
    mobilePhone = models.IntegerField(default = None, null=True)
    email = models.EmailField(max_length=1000, default = None, null=True, validators = [validate_email])
    workAddress = models.CharField(max_length=1000, default = None, null=True)      
    # workingRelationName = models.CharField(max_length=100, choices = Working_Relations, default = None)
    # workingRelationName = models.ForeignKey(working_Relations, null=True, on_delete=models.CASCADE)
    work_Experience = models.ForeignKey(WorkExperience,  null=True, on_delete=models.CASCADE)
    emp_grade_Type = models.ForeignKey(gradeTypes, null=True, on_delete=models.CASCADE)
    workingRelationName = models.ForeignKey(working_Relations, null=True, on_delete=models.CASCADE)
    employeeClass = models.ForeignKey(employee_Class, null=True, on_delete=models.CASCADE)
    employeeSpec = models.ForeignKey(employeeSpecialization, null=True, on_delete=models.CASCADE)
    salaryCl = models.ForeignKey(salaryClass, null=True, on_delete=models.CASCADE)
    empType = models.ForeignKey(employeeType, null=True, on_delete=models.CASCADE)
    title = models.ForeignKey(AcademicTitle, null=True, on_delete=models.CASCADE)
    emp_Grades = models.ForeignKey(grades, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.displayName

#Search Module | Register on Django - Admin    
class searchTest(admin.ModelAdmin):
    search_fields = ['givenName', 'TIN', 'id']     

 
    

