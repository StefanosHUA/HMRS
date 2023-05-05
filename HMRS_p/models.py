from datetime import date, timezone
from importlib.util import LazyLoader
from django import forms
from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib import admin
from rest_framework import filters, generics
from django.core.exceptions import ValidationError
from django.conf import settings 
from django.utils.translation import gettext_lazy as _
# Create your models here.

grade_change_string = 'Διαδικασία εξέλιξης σε επόμενη βαθμίδα βάσει νομοθεσίας'
scale_info = 'Κάθε 2 έτη'

substring = '@hua.gr'

def validate_email(value):
    if substring not in value:
        raise ValidationError(
            _('%(value)s is not a valid HUA email'),
            params={'value': value},
        )


SEX_Choices = getattr(settings, 'SEX_Choices', (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
))


grade_titles = getattr(settings, 'grade_choices', (
    ('A', 'A'),
    ('B', 'B'),
    ('Γ', 'Γ'),
    ('Δ', 'Δ'),
    ('Ε', 'Ε'),
))

pay_scale = getattr(settings, 'PayScale', (
    ('MK:1', 'MK:1'),
    ('MK:2', 'MK:2'),
    ('MK:3', 'MK:3'),
    ('MK:4', 'MK:4'),
    ('MK:5', 'MK:5'),
    ('MK:6', 'MK:6'),
    ('MK:7', 'MK:7'),
    ('MK:8', 'MK:8'),
    ('MK:9', 'MK:9'),
    ('MK:10', 'MK:10'),
    ('MK:11', 'MK:11'),
    ('MK:12', 'MK:12'),
    ('MK:13', 'MK:13'),
    ('MK:14', 'MK:14'),
    ('MK:15', 'MK:15'),
    ('MK:16', 'MK:16'),
    ('MK:17', 'MK:17'),
    ('MK:18', 'MK:18'),
    ('MK:19', 'MK:19'),
))

#γενικες κατηγοριες προσωπικου

general_categories = getattr(settings, 'general_choices', (

    ('Διδακτικό Ερευνητικό Προσωπικό (ΔΕΠ)', 'Διδακτικό Ερευνητικό Προσωπικό (ΔΕΠ)'),
    ('Διοικητικό Προσωπικό', 'Διοικητικό Προσωπικό'),
    ('Έκτακτο Προσωπικό', 'Έκτακτο Προσωπικό'),

))

general_short =getattr(settings, 'general_choices', (

    ('ΔΕΠ', 'ΔΕΠ'),
    ('ΔΠ', 'ΔΠ'),
    ('ΈΠ', 'EΠ'),

))


#ειδικές κατηγορίες προσωπικού
type = getattr(settings, 'type_choices', (
    ('Διδακτικό Ερευνητικό Προσωπικό', 'Διδακτικό Ερευνητικό Προσωπικό'),
    ('Εργαστηριακό Διδακτικό Προσωπικό', 'Εργαστηριακό Διδακτικό Προσωπικό'),
    ('Ειδικό Τεχνικό Εργαστηριακό Προσωπικό', 'Ειδικό Τεχνικό Εργαστηριακό Προσωπικό'),
    ('Διοικητικό Προσωπικό', 'Διοικητικό Προσωπικό'),
    ('Υπάλληλοι με απόσπαση', 'Υπάλληλοι με απόσπαση'),
    ('Εντεταλμένοι Διδάσκοντες', 'Εντεταλμένοι Διδάσκοντες'),
))

short_type = getattr(settings, 'short_choices', (
    ('ΔΕΠ', 'ΔΕΠ'),
    ('ΕΔΙΠ', 'ΕΔΙΠ'),
    ('ΕΤΕΠ', 'ΕΤΕΠ'),
    ('ΔΠ', 'ΔΠ'),
    ('YA', 'YA'),
    ('ΕΔ', 'ΕΔ'),
))

#σχεσεις εργασιας διοικητικου προσωπικου
Working_Relations = getattr(settings, 'Working_Relations_Choices', (
    ('Μόνιμος Υπάλληλος', 'Μόνιμος Υπάλληλος'),
    ('Ιδιωτικού δικαίου αορίστου χρόνου', 'Ιδιωτικού δικαίου αορίστου χρόνου'),
    ('Ιδιωτικού δικαίου ορισμένου χρόνου', 'Ιδιωτικού δικαίου ορισμένου χρόνου'),
    ('Σύμβαση εργασίας', 'Σύμβαση εργασίας'),

))

Working_Relations_short = getattr(settings, 'WR_Short', (
    ('ΜΥ', 'ΜΥ'),
    ('ΙΔΑΧ', 'ΙΔΑΧ'),
    ('ΙΔΟΧ', 'ΙΔΟΧ'),
    ('ΣΕ', 'ΣΕ'),

))

#ειδικοτητες διοικητικου προσωπικου 
emp_Class = getattr(settings, 'empClass', (
    ('Πανεπιστημιακής Εκπαίδευση', 'Πανεπιστημιακής Εκπαίδευσης'),
    ('Τεχνολογικής Εκπαίδευσης', 'Τεχνολογικής Εκπαίδευσης'),
    ('Δευτεροβάθμιας Εκπαίδευσης', 'Δευτεροβάθμιας Εκπαίδευσης'),
    ('Υποχρεωτικής Εκπαίδευσης', 'Υποχρεωτικής Εκπαίδευσης'), 
))

emp_Class_short = getattr(settings, 'empClassShort', (
    ('ΠΕ', 'ΠΕ'),
    ('ΤΕ', 'ΤΕ'),
    ('ΔΕ', 'ΔΕ'),
    ('ΥΕ', 'ΥΕ'), 
))

#κλάδος διοικητικου προσωπικου
emp_Spec = getattr(settings, 'empSpecChoices', (
    ('Διοικητικού - Οικονομικού', 'Διοικητικού - Οικονομικού'),
    ('Πληροφορικής', 'Πληροφορικής'),
    ('Διοικητικού - Λογιστικού', 'Διοικητικού - Λογιστικού'),
    ('Βιβλιοθηκονόμων', 'Βιβλιοθηκονόμων'),
    ('Μηχανικών', 'Μηχανικών'),
    ('Επιμελητών', 'Επιμελητών'),
))

emp_Spec_short = getattr(settings, 'emp_Short', (
    ('ΔΟ', 'ΔΟ'),
    ('ΠΛΗ', 'ΠΛΗ'),
    ('ΔΛ', 'ΔΛ'),
    ('ΒΙ', 'ΒΙ'),
    ('ΜΗΧ', 'ΜΗΧ'),
    ('ΕΠΙ', 'ΕΠΙ'),
))


grades_full = getattr(settings, 'grades_choices', (
    ('ΒΑΔΜΙΔΑ Α', 'ΒΑΔΜΙΔΑ Α'),
    ('ΒΑΔΜΙΔΑ Β', 'ΒΑΔΜΙΔΑ Β'),
))

grades_short = getattr(settings, 'gradesShort', (
    ('Α', 'Α'),
    ('Β', 'Β')
))




legal_status = getattr(settings, 'legal_status_choices', (
    ('Ιδιωτικός', 'Ιδιωτικός'),
    ('Δημόσιος', 'Δημόσιος'),
))


#βαθμιδες μελων ΔΕΠ, ΕΔΙΠ, ΕΤΕΠ
titles = getattr(settings, 'title_choices', (
    ('Επίκουρος Καθηγητής επί θητεία', 'Επίκουρος Καθηγητής επί θητεία'),
    ('Μόνιμος Επίκουρος Καθηγητής', 'Μόνιμος Επίκουρος Καθηγητής'),
    ('Αναπληρωτής Καθηγητής', 'Αναπληρωτής Καθηγητής'),
    ('Καθηγητής Α Βαθμίδας', 'Καθηγητής Α Βαθμίδας'),
    ('Α - Δ Εισαγωγική Δ', 'Α - Δ Εισαγωγική Δ'),
    ('Α - Ε Εισαγωγική Ε', 'Α - Ε Εισαγωγική Ε'),
    ('Καμία Τιμή', 'Καμία Τιμή'),
))



class employeeType(models.Model):
    fulltTitle = models.CharField(max_length=1000, choices= general_categories, default=None)
    shortTitle = models.CharField(max_length=100, choices = general_short, default = None)
    
    def __str__(self):
        return self.fulltTitle

class employeeSpecificType(models.Model):
    fulltTitle = models.CharField(max_length=1000, choices= type, default=None)
    shortTitle = models.CharField(max_length=100, choices = short_type, default = None)
    
    def __str__(self):
        return self.fulltTitle



class salaryClass(models.Model):
    shortName = models.CharField(max_length=100, default=None)
    fullName = models.CharField(max_length=100, default = None)

    def __str__(self):
        return self.fullName



class grades(models.Model):
    gradeFullName = models.CharField(max_length=100, choices=grades_full, default=None)
    gradeShortName = models.CharField(max_length=100, choices = grades_short, default = None)

    def __str__(self):
        return self.gradeFullName


class generic_User(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    givenName = models.CharField(max_length=100, default = None, null=True)
    surName = models.CharField(max_length=100, default = None, null=True)
    displayName = models.CharField(max_length=50, default =  None, null=True)
    fathersName = models.CharField(max_length=20, default=None, null=True)
    mothersName = models.CharField(max_length=20, default = None, null=True)
    id = models.CharField(max_length=20000, primary_key=True)
    idIssuer = models.CharField(max_length=50, default = None, null=True)
    issueDate = models.DateField(max_length=20, default = None, null=True )
    birthDate = models.DateField(max_length=20, default = None, null=True)
    TIN = models.IntegerField(default = None, null=True)
    SSN = models.IntegerField(default=None, null=True)
    sex = models.CharField(choices=SEX_Choices, max_length=100, default = None, null=True)
    nationality = CountryField()
    address = models.CharField(max_length=10, default=None, null=True)
    homePhone = models.IntegerField(default = None, null=True)
    mobilePhone = models.IntegerField(default = None, null=True)
    email = models.EmailField(max_length=20, default = None, null=True, validators = [validate_email])
    workAddress = models.CharField(max_length=20, default = None, null=True)
    general_emp_Type = models.ForeignKey(employeeType, null=True, on_delete=models.CASCADE)   
    specific_emp_Type = models.ForeignKey(employeeSpecificType, null=True, on_delete=models.CASCADE)
    #-------------------------------------------------------------------------------------

    #emp_grade_Type = models.ForeignKey(gradeTypes, null=True, on_delete=models.CASCADE)
    #workingRelationName = models.ForeignKey(working_Relations, null=True, on_delete=models.CASCADE)
    #employeeClass = models.ForeignKey(employee_Class, null=True, on_delete=models.CASCADE)
    #employeeSpec = models.ForeignKey(employeeSpecialization, null=True, on_delete=models.CASCADE)
    #salary_Cl = models.ForeignKey(salaryClass, null=True, on_delete=models.CASCADE)
    #title = models.ForeignKey(AcademicTitle, null=True, on_delete=models.CASCADE)
    #emp_Grades = models.ForeignKey(grades, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.displayName

 
    

class WorkExperience(models.Model):
    myUser = models.ForeignKey(generic_User, on_delete=models.CASCADE)
    legal_status = models.CharField(max_length=100, choices = legal_status, default = None)
    organization = models.CharField(max_length=100, default = None)
    startDate = models.DateField(default=None)
    endDate = models.DateField(default = None)
    additional_info = models.TextField(default = None)
    grade = models.ForeignKey(grades, null=True, on_delete=models.CASCADE)
    previous_salaryClass = models.ForeignKey(salaryClass, null=True, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.organization
    
class depProfile(models.Model):
    UserAsg = models.ForeignKey(generic_User, on_delete=models.CASCADE)
    acadTitle = models.CharField(choices=titles, max_length=200, default=None)
    grade_change_info = models.CharField(max_length=100, default=grade_change_string)
    scale_change = models.CharField(max_length=50, default = scale_info)


class DPprofile(models.Model):
    UserAsg = models.ForeignKey(generic_User, on_delete=models.CASCADE)
    fullName = models.CharField(max_length=100, choices=Working_Relations, default=None)
    shortName = models.CharField(max_length=100, choices=Working_Relations_short, default = None)
    fullName2 = models.CharField(max_length=100, choices=emp_Class, default=None)
    shortName2 = models.CharField(max_length=100, choices = emp_Class_short, default = None)
    fullname3 = models.CharField(max_length=100, choices=emp_Spec, default=None)
    shortname3 = models.CharField(max_length=100, choices = emp_Spec_short, default = None)
    grade_change_info = models.CharField(max_length=100, choices=grade_titles, default = None)
    pay_scale_details = models.CharField(max_length=100, choices=pay_scale, default = None)



# class AcademicTitle(models.Model):
#     #profile = models.ForeignKey(depProfile, on_delete=models.CASCADE)
#     acadTitle = models.CharField(choices=titles, max_length=200, default=None) 
#     def __str__(self):
#         return self.acadTitle
    

# class working_Relations(models.Model):
#     #myProfile = models.ForeignKey(DPprofile, on_delete=models.CASCADE)
#     fullName = models.CharField(max_length=100, choices=Working_Relations, default=None)
#     shortName = models.CharField(max_length=100, choices=Working_Relations_short, default = None)
#     def __str__(self):
#         return self.fullName 
    

# class employee_Class(models.Model):
#     #profile = models.ForeignKey(DPprofile, on_delete = models.CASCADE)
#     fullName = models.CharField(max_length=100, choices=emp_Class, default=None)
#     shortName = models.CharField(max_length=100, choices = emp_Class_short, default = None)
#     def __str__(self):
#         return self.fullName

# class employeeSpecialization(models.Model):
#     #profile = models.ForeignKey(DPprofile, on_delete = models.CASCADE)
#     fullname = models.CharField(max_length=100, choices=emp_Spec, default=None)
#     shortname = models.CharField(max_length=100, choices = emp_Spec_short, default = None)
#     def __str__(self):
#         return self.fullname