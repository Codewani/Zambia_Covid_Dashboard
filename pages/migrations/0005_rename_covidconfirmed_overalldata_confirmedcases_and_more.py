# Generated by Django 4.0 on 2021-12-29 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_rename_comfirmedcases_coviddata_confirmedcases_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='overalldata',
            old_name='CovidConfirmed',
            new_name='ConfirmedCases',
        ),
        migrations.RenameField(
            model_name='overalldata',
            old_name='CovidRecoveries',
            new_name='FirstDoseVaccinations',
        ),
        migrations.RenameField(
            model_name='overalldata',
            old_name='VaccineFirstDose',
            new_name='FullyVaccinated',
        ),
        migrations.RenameField(
            model_name='overalldata',
            old_name='VaccineFullyVaccinated',
            new_name='Recoveries',
        ),
    ]