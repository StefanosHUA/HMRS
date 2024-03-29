# Generated by Django 4.1.4 on 2023-03-29 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HMRS_p', '0012_remove_employee_class_myuser_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='generic_user',
            old_name='salaryCl',
            new_name='salary_Cl',
        ),
        migrations.RemoveField(
            model_name='academictitle',
            name='myUser',
        ),
        migrations.RemoveField(
            model_name='employeetype',
            name='myUser',
        ),
        migrations.AddField(
            model_name='generic_user',
            name='empType',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HMRS_p.employeetype'),
        ),
        migrations.AddField(
            model_name='generic_user',
            name='title',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HMRS_p.academictitle'),
        ),
        migrations.AlterField(
            model_name='employeetype',
            name='fulltTitle',
            field=models.CharField(choices=[('Διδακτικό Ερευνητικό Προσωπικό (ΔΕΠ)', 'Διδακτικό Ερευνητικό Προσωπικό (ΔΕΠ)'), ('Διοικητικό Προσωπικό', 'Διοικητικό Προσωπικό'), ('Έκτακτο Προσωπικό', 'Έκτακτο Προσωπικό')], default=None, max_length=1000),
        ),
        migrations.AlterField(
            model_name='employeetype',
            name='shortTitle',
            field=models.CharField(choices=[('ΔΕΠ', 'ΔΕΠ'), ('ΕΔΙΠ', 'ΕΔΙΠ'), ('ΕΤΕΠ', 'ΕΤΕΠ')], default=None, max_length=100),
        ),
    ]
