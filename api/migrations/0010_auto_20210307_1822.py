# Generated by Django 3.1.7 on 2021-03-07 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20210305_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piłkarz',
            name='pozycja',
            field=models.CharField(choices=[('Napastnik', 'Napastnik'), ('Obrońca', 'Obrońca'), ('Pomocnik', 'Pomocnik'), ('Bramkarz', 'Bramkarz'), ('Tam gdzie trzeba', 'Tam gdzie trzeba')], default='Tam gdzie trzeba', max_length=32),
        ),
    ]
