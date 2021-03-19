# Generated by Django 3.1.7 on 2021-03-04 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_klub_liga'),
    ]

    operations = [
        migrations.AlterField(
            model_name='klub',
            name='liga',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='kluby', to='api.liga'),
        ),
        migrations.CreateModel(
            name='Piłkarz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=32)),
                ('nazwisko', models.CharField(max_length=32)),
                ('data_urodzenia', models.DateField(default='2000-01-01')),
                ('pozycja', models.IntegerField(choices=[(3, 'Pomocnik'), (2, 'Obrońca'), (0, 'Tam gdzie trzeba'), (4, 'Napastnik'), (1, 'Bramkarz')], default=0)),
                ('klub', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.klub')),
            ],
        ),
    ]