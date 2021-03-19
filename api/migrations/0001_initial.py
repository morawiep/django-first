# Generated by Django 3.1.7 on 2021-03-04 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Klub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=64)),
                ('miasto', models.CharField(max_length=64)),
                ('liga', models.CharField(max_length=64)),
                ('rok_zalozenia', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
