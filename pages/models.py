from django.db import models

# Create your models here.
class VaccinationSites(models.Model):
    province     = models.CharField(max_length=200, null=True)
    district     = models.CharField(max_length=200, null=True)
    site         = models.CharField(max_length=200, null=True)
    date_created = models.DateField(auto_now_add=True, null=True)
    
    def __str__(self):
        return f"{self.province}," + f"{self.district}," + f"{self.site}" 

class TodayData(models.Model):
    Date                    = models.DateField(blank=True, null=True)
    Tests                   = models.CharField(max_length=200, null=True)
    ConfirmedCases          = models.CharField(max_length=200, null=True)
    Recoveries              = models.CharField(max_length=200, null=True)
    FirstDoseVaccinations   = models.CharField(max_length=200, null=True, blank=True)
    FullyVaccinated         = models.CharField(max_length=200, null=True, blank=True)
    Deaths                  = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.Date.strftime("%B %d,%Y")
    
    
class OverallData(models.Model):
    Date                  = models.DateField(blank=True, null=True)
    Confirmed             = models.CharField(max_length=200, null=True)
    Recoveries            = models.CharField(max_length=200, null=True)
    Active                = models.CharField(max_length=200, null=True)
    FirstDoseVaccinations = models.CharField(max_length=200, null=True)
    FullyVaccinated       = models.CharField(max_length=200, null=True)
    Deaths                = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.Date.strftime("%B %d,%Y")
    
    
    