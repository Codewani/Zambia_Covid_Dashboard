# Generated by Django 4.0 on 2022-01-01 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_alter_coviddata_confirmedcases_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TodayData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(blank=True, null=True)),
                ('Tests', models.CharField(max_length=200, null=True)),
                ('ConfirmedCases', models.CharField(max_length=200, null=True)),
                ('Recoveries', models.CharField(max_length=200, null=True)),
                ('FirstDoseVaccinations', models.CharField(blank=True, max_length=200, null=True)),
                ('FullyVaccinated', models.CharField(blank=True, max_length=200, null=True)),
                ('Deaths', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='CovidData',
        ),
        migrations.AddField(
            model_name='overalldata',
            name='Date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
