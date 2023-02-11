# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class HmrsPAcademictitle(models.Model):
    id = models.BigAutoField(primary_key=True)
    acadtitle = models.CharField(db_column='acadTitle', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HMRS_p_academictitle'


class HmrsPEmployeeClass(models.Model):
    id = models.BigAutoField(primary_key=True)
    fullname = models.CharField(db_column='fullName', max_length=100)  # Field name made lowercase.
    shortname = models.CharField(db_column='shortName', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HMRS_p_employee_class'


class HmrsPEmployeespecialization(models.Model):
    id = models.BigAutoField(primary_key=True)
    fullname = models.CharField(max_length=100)
    shortname = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'HMRS_p_employeespecialization'


class HmrsPEmployeetype(models.Model):
    id = models.BigAutoField(primary_key=True)
    fullttitle = models.CharField(db_column='fulltTitle', max_length=100)  # Field name made lowercase.
    shorttitle = models.CharField(db_column='shortTitle', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HMRS_p_employeetype'


class HmrsPGenericUser(models.Model):
    givenname = models.CharField(db_column='givenName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    surname = models.CharField(db_column='surName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    displayname = models.CharField(db_column='displayName', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    fathersname = models.CharField(db_column='fathersName', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    mothersname = models.CharField(db_column='mothersName', max_length=100000, blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(primary_key=True, max_length=20000)
    idissuer = models.CharField(db_column='idIssuer', max_length=50000, blank=True, null=True)  # Field name made lowercase.
    issuedate = models.DateField(db_column='issueDate', blank=True, null=True)  # Field name made lowercase.
    birthdate = models.DateField(db_column='birthDate', blank=True, null=True)  # Field name made lowercase.
    tin = models.IntegerField(db_column='TIN', blank=True, null=True)  # Field name made lowercase.
    ssn = models.IntegerField(db_column='SSN', blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(max_length=1000, blank=True, null=True)
    nationality = models.CharField(max_length=2)
    address = models.CharField(max_length=100, blank=True, null=True)
    homephone = models.IntegerField(db_column='homePhone', blank=True, null=True)  # Field name made lowercase.
    mobilephone = models.IntegerField(db_column='mobilePhone', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(max_length=1000, blank=True, null=True)
    workaddress = models.CharField(db_column='workAddress', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    emptype = models.ForeignKey(HmrsPEmployeetype, models.DO_NOTHING, db_column='empType_id', blank=True, null=True)  # Field name made lowercase.
    emp_grades = models.ForeignKey('HmrsPGrades', models.DO_NOTHING, db_column='emp_Grades_id', blank=True, null=True)  # Field name made lowercase.
    emp_grade_type = models.ForeignKey('HmrsPGradetypes', models.DO_NOTHING, db_column='emp_grade_Type_id', blank=True, null=True)  # Field name made lowercase.
    employeeclass = models.ForeignKey(HmrsPEmployeeClass, models.DO_NOTHING, db_column='employeeClass_id', blank=True, null=True)  # Field name made lowercase.
    employeespec = models.ForeignKey(HmrsPEmployeespecialization, models.DO_NOTHING, db_column='employeeSpec_id', blank=True, null=True)  # Field name made lowercase.
    salarycl = models.ForeignKey('HmrsPSalaryclass', models.DO_NOTHING, db_column='salaryCl_id', blank=True, null=True)  # Field name made lowercase.
    title = models.ForeignKey(HmrsPAcademictitle, models.DO_NOTHING, blank=True, null=True)
    work_experience = models.ForeignKey('HmrsPWorkexpirience', models.DO_NOTHING, db_column='work_Experience_id', blank=True, null=True)  # Field name made lowercase.
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HMRS_p_generic_user'


class HmrsPGenericUserWorkingrelationname(models.Model):
    id = models.BigAutoField(primary_key=True)
    generic_user = models.ForeignKey(HmrsPGenericUser, models.DO_NOTHING)
    working_relations = models.ForeignKey('HmrsPWorkingRelations', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'HMRS_p_generic_user_workingRelationName'
        unique_together = (('generic_user', 'working_relations'),)


class HmrsPGrades(models.Model):
    id = models.BigAutoField(primary_key=True)
    gradefullname = models.CharField(db_column='gradeFullName', max_length=100)  # Field name made lowercase.
    gradeshortname = models.CharField(db_column='gradeShortName', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HMRS_p_grades'


class HmrsPGradetypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    field_class = models.ForeignKey(HmrsPEmployeeClass, models.DO_NOTHING, db_column='_class_id', blank=True, null=True)  # Field renamed because it started with '_'.
    grade = models.ForeignKey(HmrsPGrades, models.DO_NOTHING, blank=True, null=True)
    specialization = models.ForeignKey(HmrsPEmployeespecialization, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HMRS_p_gradetypes'


class HmrsPSalaryclass(models.Model):
    id = models.BigAutoField(primary_key=True)
    shortname = models.CharField(db_column='shortName', max_length=100)  # Field name made lowercase.
    fullname = models.CharField(db_column='fullName', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HMRS_p_salaryclass'


class HmrsPWorkexpirience(models.Model):
    id = models.BigAutoField(primary_key=True)
    legal_status = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    startdate = models.DateField(db_column='startDate')  # Field name made lowercase.
    enddate = models.DateField(db_column='endDate')  # Field name made lowercase.
    additional_info = models.TextField()
    previous_salaryclass = models.CharField(db_column='previous_salaryClass', max_length=100)  # Field name made lowercase.
    current_salaryclass = models.ForeignKey(HmrsPSalaryclass, models.DO_NOTHING, db_column='current_salaryClass_id', blank=True, null=True)  # Field name made lowercase.
    grade = models.ForeignKey(HmrsPGrades, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HMRS_p_workexpirience'


class HmrsPWorkingRelations(models.Model):
    id = models.BigAutoField(primary_key=True)
    fullname = models.CharField(db_column='fullName', max_length=100)  # Field name made lowercase.
    shortname = models.CharField(db_column='shortName', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HMRS_p_working_relations'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
