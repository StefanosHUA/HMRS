# Generated by Django 4.1.4 on 2023-01-14 10:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acadTitle', models.CharField(choices=[('Επίκουρος Καθηγητής επί θητεία', 'Επίκουρος Καθηγητής επί θητεία'), ('Μόνιμος Επίκουρος Καθηγητής', 'Μόνιμος Επίκουρος Καθηγητής'), ('Αναπληρωτής Καθηγητής', 'Αναπληρωτής Καθηγητής'), ('Καθηγητής Α Βαθμίδας', 'Καθηγητής Α Βαθμίδας'), ('Α - Δ Εισαγωγική Δ', 'Α - Δ Εισαγωγική Δ'), ('Α - Ε Εισαγωγική Ε', 'Α - Ε Εισαγωγική Ε'), ('Καμία Τιμή', 'Καμία Τιμή')], default=None, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='employee_Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(choices=[('Πανεπιστημιακής Εκπαίδευση', 'Πανεπιστημιακής Εκπαίδευσης'), ('Τεχνολογικής Εκπαίδευσης', 'Τεχνολογικής Εκπαίδευσης'), ('Δευτεροβάθμιας Εκπαίδευσης', 'Δευτεροβάθμιας Εκπαίδευσης'), ('Υποχρεωτικής Εκπαίδευσης', 'Υποχρεωτικής Εκπαίδευσης')], default=None, max_length=100)),
                ('shortName', models.CharField(choices=[('ΠΕ', 'ΠΕ'), ('ΤΕ', 'ΤΕ'), ('ΔΕ', 'ΔΕ'), ('ΥΕ', 'ΥΕ')], default=None, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='employeeSpecialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(choices=[('Διοικητικού - Οικονομικού', 'Διοικητικού - Οικονομικού'), ('Πληροφορικής', 'Πληροφορικής'), ('Διοικητικού - Λογιστικού', 'Διοικητικού - Λογιστικού'), ('Βιβλιοθηκονόμων', 'Βιβλιοθηκονόμων'), ('Μηχανικών', 'Μηχανικών'), ('Επιμελητών', 'Επιμελητών')], default=None, max_length=100)),
                ('shortname', models.CharField(choices=[('ΔΟ', 'ΔΟ'), ('ΠΛΗ', 'ΠΛΗ'), ('ΔΛ', 'ΔΛ'), ('ΒΙ', 'ΒΙ'), ('ΜΗΧ', 'ΜΗΧ'), ('ΕΠΙ', 'ΕΠΙ')], default=None, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='employeeType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fulltTitle', models.CharField(choices=[('Διδακτικό Ερευνητικό Προσωπικό', 'Διδακτικό Ερευνητικό Προσωπικό'), ('Εργαστηριακό Διδακτικό Προσωπικό', 'Εργαστηριακό Διδακτικό Προσωπικό'), ('Ειδικό Τεχνικό Εργαστηριακό Προσωπικό', 'Ειδικό Τεχνικό Εργαστηριακό Προσωπικό'), ('Διοικητικό Προσωπικό', 'Διοικητικό Προσωπικό'), ('Υπάλληλοι με απόσπαση', 'Υπάλληλοι με απόσπαση'), ('Εντεταλμένοι Διδάσκοντες', 'Εντεταλμένοι Διδάσκοντες')], default=None, max_length=100)),
                ('shortTitle', models.CharField(choices=[('ΔΕΠ', 'ΔΕΠ'), ('ΕΔΙΠ', 'ΕΔΙΠ'), ('ΕΤΕΠ', 'ΕΤΕΠ'), ('ΔΠ', 'ΔΠ'), ('YA', 'YA'), ('ΕΔ', 'ΕΔ')], default=None, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='grades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gradeFullName', models.CharField(choices=[('ΒΑΔΜΙΔΑ Α', 'ΒΑΔΜΙΔΑ Α'), ('ΒΑΔΜΙΔΑ Β', 'ΒΑΔΜΙΔΑ Β')], default=None, max_length=100)),
                ('gradeShortName', models.CharField(choices=[('Α', 'Α'), ('Β', 'Β')], default=None, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='salaryClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortName', models.CharField(default=None, max_length=100)),
                ('fullName', models.CharField(default=None, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='working_Relations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(choices=[('Μόνιμος Υπάλληλος', 'Μόνιμος Υπάλληλος'), ('Ιδιωτικού δικαίου αορίστου χρόνου', 'Ιδιωτικού δικαίου αορίστου χρόνου'), ('Ιδιωτικού δικαίου ορισμένου χρόνου', 'Ιδιωτικού δικαίου ορισμένου χρόνου'), ('Σύμβαση εργασίας', 'Σύμβαση εργασίας')], default=None, max_length=100)),
                ('shortName', models.CharField(choices=[('ΜΥ', 'ΜΥ'), ('ΙΔΑΧ', 'ΙΔΑΧ'), ('ΙΔΟΧ', 'ΙΔΟΧ'), ('ΣΕ', 'ΣΕ')], default=None, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legal_status', models.CharField(choices=[('Ιδιωτικός', 'Ιδιωτικός'), ('Δημόσιος', 'Δημόσιος')], default=None, max_length=100)),
                ('organization', models.CharField(default=None, max_length=100)),
                ('startDate', models.DateField(default=None)),
                ('endDate', models.DateField(default=None)),
                ('additional_info', models.TextField(default=None)),
                ('previous_salaryClass', models.CharField(default=None, max_length=100)),
                ('current_salaryClass', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HMRS_p.salaryclass')),
                ('grade', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HMRS_p.grades')),
            ],
        ),
        migrations.CreateModel(
            name='gradeTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_class', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HMRS_p.employee_class')),
                ('grade', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HMRS_p.grades')),
                ('specialization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HMRS_p.employeespecialization')),
            ],
        ),
        migrations.CreateModel(
            name='generic_User',
            fields=[
                ('givenName', models.CharField(default=None, max_length=100, null=True)),
                ('surName', models.CharField(default=None, max_length=100, null=True)),
                ('displayName', models.CharField(default=None, max_length=1000, null=True)),
                ('fathersName', models.CharField(default=None, max_length=1000, null=True)),
                ('mothersName', models.CharField(default=None, max_length=100000, null=True)),
                ('id', models.CharField(max_length=20000, primary_key=True, serialize=False)),
                ('idIssuer', models.CharField(default=None, max_length=50000, null=True)),
                ('issueDate', models.DateField(default=None, max_length=200, null=True)),
                ('birthDate', models.DateField(default=None, max_length=200, null=True)),
                ('TIN', models.IntegerField(default=None, null=True)),
                ('SSN', models.IntegerField(default=None, null=True)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default=None, max_length=1000, null=True)),
                ('nationality', django_countries.fields.CountryField(max_length=2)),
                ('address', models.CharField(default=None, max_length=100, null=True)),
                ('homePhone', models.IntegerField(default=None, null=True)),
                ('mobilePhone', models.IntegerField(default=None, null=True)),
                ('email', models.EmailField(default=None, max_length=1000, null=True)),
                ('workAddress', models.CharField(default=None, max_length=1000, null=True)),
                ('empType', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HMRS_p.employeetype')),
                ('emp_Grades', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HMRS_p.grades')),
                ('emp_grade_Type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HMRS_p.gradetypes')),
                ('employeeClass', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HMRS_p.employee_class')),
                ('employeeSpec', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HMRS_p.employeespecialization')),
                ('salaryCl', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HMRS_p.salaryclass')),
                ('title', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HMRS_p.academictitle')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('work_Experience', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HMRS_p.workexperience')),
                ('workingRelationName', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HMRS_p.working_relations')),
            ],
        ),
    ]
