# Generated by Django 4.1.4 on 2023-03-07 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HMRS_p', '0005_alter_academictitle_acadtitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academictitle',
            name='acadTitle',
            field=models.CharField(choices=[('Επίκουρος Καθηγητής επί θητεία', 'Επίκουρος Καθηγητής επί θητεία'), ('Μόνιμος Επίκουρος Καθηγητής', 'Μόνιμος Επίκουρος Καθηγητής'), ('Αναπληρωτής Καθηγητής', 'Αναπληρωτής Καθηγητής'), ('Καθηγητής Α Βαθμίδας', 'Καθηγητής Α Βαθμίδας'), ('Α - Δ Εισαγωγική Δ', 'Α - Δ Εισαγωγική Δ'), ('Α - Ε Εισαγωγική Ε', 'Α - Ε Εισαγωγική Ε'), ('Καμία Τιμή', 'Καμία Τιμή')], default=None, max_length=200),
        ),
    ]
