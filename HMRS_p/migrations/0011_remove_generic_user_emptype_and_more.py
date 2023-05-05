# Generated by Django 4.1.4 on 2023-03-09 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HMRS_p', '0010_alter_workexperience_myuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='generic_user',
            name='empType',
        ),
        migrations.RemoveField(
            model_name='generic_user',
            name='emp_Grades',
        ),
        migrations.RemoveField(
            model_name='generic_user',
            name='emp_grade_Type',
        ),
        migrations.RemoveField(
            model_name='generic_user',
            name='employeeClass',
        ),
        migrations.RemoveField(
            model_name='generic_user',
            name='employeeSpec',
        ),
        migrations.RemoveField(
            model_name='generic_user',
            name='salaryCl',
        ),
        migrations.RemoveField(
            model_name='generic_user',
            name='title',
        ),
        migrations.RemoveField(
            model_name='generic_user',
            name='workingRelationName',
        ),
        migrations.AddField(
            model_name='academictitle',
            name='myUser',
            field=models.OneToOneField(default=2, on_delete=django.db.models.deletion.CASCADE, to='HMRS_p.generic_user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee_class',
            name='myUser',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='HMRS_p.generic_user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employeespecialization',
            name='myUser',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='HMRS_p.generic_user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employeetype',
            name='myUser',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='HMRS_p.generic_user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grades',
            name='myUser',
            field=models.OneToOneField(default=2, on_delete=django.db.models.deletion.CASCADE, to='HMRS_p.generic_user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gradetypes',
            name='myUser',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='HMRS_p.generic_user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='salaryclass',
            name='myUser',
            field=models.OneToOneField(default=2, on_delete=django.db.models.deletion.CASCADE, to='HMRS_p.generic_user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='working_relations',
            name='myUser',
            field=models.OneToOneField(default=2, on_delete=django.db.models.deletion.CASCADE, to='HMRS_p.generic_user'),
            preserve_default=False,
        ),
    ]