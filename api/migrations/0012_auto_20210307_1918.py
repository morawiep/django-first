# Generated by Django 3.1.7 on 2021-03-07 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20210307_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piłkarz',
            name='pozycja',
            field=models.CharField(choices=[('Napastnik', 'Napastnik'), ('Bramkarz', 'Bramkarz'), ('Obrońca', 'Obrońca'), ('Tam gdzie trzeba', 'Tam gdzie trzeba'), ('Pomocnik', 'Pomocnik')], default='Tam gdzie trzeba', max_length=32),
        ),
    ]
