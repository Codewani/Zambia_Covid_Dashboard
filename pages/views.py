from django.shortcuts import render
from datetime import datetime
import urllib, json

from .models import *

# Create your views here.
def home_view(request, *args, **kwargs):
    #daily cases
    newCaseslabels = []
    casesData = []
    #daily deaths
    dailyDeaths = []
    tests = []

    queryset = TodayData.objects.order_by('-Date')[::-1]
    mylist = (queryset[-14::])

    for date in mylist:
        #append date
        x = date.Date
        y = x.strftime("%B %d,%Y")
        newCaseslabels.append(y)
        #append Confirmed Cases
        a = int(date.ConfirmedCases.replace(',', ''))
        casesData.append(a)
        #append daily deaths
        dailyDeaths.append(int(date.Deaths.replace(',', '')))
        #append number of tests
        tests.append(int(date.Tests.replace(',', '')))
    CumulativeLabels = []
    ActiveCases = []

    overall = OverallData.objects.order_by('-Date')[::-1]
    overalllist = (overall[-14::])

    for i in overalllist:
        ActiveCases.append(int(i.Active.replace(',', '')))
        x = i.Date
        y = x.strftime("%B %d,%Y")
        CumulativeLabels.append(y)
    overalldata = OverallData.objects.order_by('-Date')[0]
    latestdata  = TodayData.objects.order_by('-Date')[0]
    # latestdata = CovidData.objects.latest('id')
    total = int(overalldata.FirstDoseVaccinations.replace(',', '')) + int(overalldata.FullyVaccinated.replace(',', ''))
    totalvaccinations = f"{total:,d}"
    
    
    return render(request, "index.html",
                  {'data': latestdata,
                   'overall': overalldata,
                   'casesLabels': newCaseslabels,
                   'x': casesData,
                   'dailyDeaths': dailyDeaths,
                   'totalvaccinations': totalvaccinations,
                   'activeCases': ActiveCases,
                   'cumulativeLabels': CumulativeLabels,
                   'Tests': tests
                   })

def vaccine_view(request, *args, **kwargs):
        #daily cases
    labels = []
    firstDoseData = []
    #daily deaths
    fullyVaccinatedData = []

    queryset = TodayData.objects.order_by('-Date')[::-1]
    mylist = (queryset[-7::])
    for i in mylist:
        #append date
        x = i.Date
        y = x.strftime("%B %d,%Y")
        labels.append(y)
        #append Confirmed Cases
        a = int(i.FirstDoseVaccinations.replace(',', ''))
        firstDoseData.append(a)
        #append daily deaths
        fullyVaccinatedData.append(int(i.FullyVaccinated.replace(',', '')))
    vaccinationsites = VaccinationSites.objects.all()
    overalldata = OverallData.objects.latest('id')
    latestdata  = TodayData.objects.order_by('-Date')[0]
    total = int(overalldata.FirstDoseVaccinations.replace(',', '')) + int(overalldata.FullyVaccinated.replace(',', ''))
    totalvaccinations = f"{total:,d}"
    return render(request, "vaccines.html", {'sites': vaccinationsites,
                                             'overall': overalldata,
                                             'data': latestdata,
                                             'labels': labels,
                                             'firstDose': firstDoseData,
                                             'fullyVaccinated': fullyVaccinatedData,
                                             'totalvaccinations': totalvaccinations})
    
def data_view(request, *args, **kwargs):
    url = "https://api.covid19api.com/live/country/zambia/status/confirmed"
    res = urllib.request.urlopen(url)
    data = json.loads(res.read())
    loaddata = data[-1]
    cumulativeconfirmed = f"{loaddata['Confirmed']:,d}"
    active = f"{loaddata['Active']:,d}"
    deaths = f"{loaddata['Deaths']:,d}"
    recoveries = f"{(loaddata['Confirmed'] - loaddata['Active']):,d}"
    print (cumulativeconfirmed)
    
    return render(request, "data.html", {'Confirmed': cumulativeconfirmed,
                                         'Deaths': deaths,
                                         'Active': active,
                                         'Recoveries': recoveries})
def contact_view(request, *args, **kwargs):
    return render(request, "aboutcovid.html", {})

def homeremedies_view(request, *args, **kwargs):
    return render(request, "homeremedies.html", {})
def login_view(request, *args, **kwargs):
    return render(request, "vaccine.html", {})
#covid19 pages
def covid_central_view(request, *args, **kw):
    return render(request, "Covid_provinces/central/central.html", {})
def covid_copperbelt_view(request, *args, **kw):
    return render(request, "Covid_provinces/copperbelt/copperbelt.html", {})
def covid_eastern_view(request, *args, **kw):
    return render(request, "Covid_provinces/eastern/eastern.html", {})
def covid_luapula_view(request, *args, **kw):
    return render(request, "Covid_provinces/luapula/luapula.html", {})
def covid_lusaka_view(request, *args, **kw):
    return render(request, "Covid_provinces/lusaka/lusaka.html", {})
def covid_muchinga_view(request, *args, **kw):
    return render(request, "Covid_provinces/muchinga/muchinga.html", {})
def covid_northwestern_view(request, *args, **kw):
    return render(request, "Covid_provinces/northwestern/northwestern.html", {})
def covid_northern_view(request, *args, **kw):
    return render(request, "Covid_provinces/northern/northern.html", {})
def covid_southern_view(request, *args, **kw):
    return render(request, "Covid_provinces/southern/southern.html", {})
def covid_western_view(request, *args, **kw):
    return render(request, "Covid_provinces/western/western.html", {})
#covid districts
#southern
def chibombo_view(request, *args, **kw):
    return render(request, "Covid_provinces/central/districts/Chibombo/chibombo.html", {})



#vaccine pages
def vaccine_central_view(request, *args, **kw):
    return render(request, "vaccine_provinces/central/central.html", {})
def vaccine_copperbelt_view(request, *args, **kw):
    return render(request, "vaccine_provinces/copperbelt/copperbelt.html", {})
def vaccine_eastern_view(request, *args, **kw):
    return render(request, "vaccine_provinces/eastern/eastern.html", {})
def vaccine_luapula_view(request, *args, **kw):
    return render(request, "vaccine_provinces/luapula/luapula.html", {})
def vaccine_lusaka_view(request, *args, **kw):
    return render(request, "vaccine_provinces/lusaka/lusaka.html", {})
def vaccine_muchinga_view(request, *args, **kw):
    return render(request, "vaccine_provinces/muchinga/muchinga.html", {})
def vaccine_northwestern_view(request, *args, **kw):
    return render(request, "vaccine_provinces/northwestern/northwestern.html", {})
def vaccine_northern_view(request, *args, **kw):
    return render(request, "vaccine_provinces/northern/northern.html", {})
def vaccine_southern_view(request, *args, **kw):
    return render(request, "vaccine_provinces/southern/southern.html", {})
def vaccine_western_view(request, *args, **kw):
    return render(request, "vaccine_provinces/western/western.html", {})