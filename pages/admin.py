from django.contrib import admin

# Register your models here.

from .models import *

@admin.register(VaccinationSites)
class VaccinationSitesAdmin(admin.ModelAdmin):
    list_display = ('province', 'district', 'site')
    ordering = ('province',)
    search_fields = ('province', 'district', 'site')
    
@admin.register(TodayData)
class TodayDataAdmin(admin.ModelAdmin):
    list_display = ('Date', 'Tests', 'ConfirmedCases', 'Recoveries', 'FirstDoseVaccinations', 'FullyVaccinated', 'Deaths')
    ordering = ('Date',)

@admin.register(OverallData)
class OverallDataAdmin(admin.ModelAdmin):
    list_display = ('Date', 'Confirmed', 'Recoveries', 'Active', 'FirstDoseVaccinations', 'FullyVaccinated', 'Deaths')
    ordering = ('Date',)
    
