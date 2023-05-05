# Generated by Django 4.1.4 on 2023-04-02 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HMRS_p', '0015_remove_academictitle_profile_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AcademicTitle',
        ),
        migrations.DeleteModel(
            name='employee_Class',
        ),
        migrations.DeleteModel(
            name='employeeSpecialization',
        ),
        migrations.DeleteModel(
            name='working_Relations',
        ),
        migrations.RemoveField(
            model_name='workexperience',
            name='current_salaryClass',
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='previous_salaryClass',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HMRS_p.salaryclass'),
        ),
    ]