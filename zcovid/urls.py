"""zcovid URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from pages.views import *

urlpatterns = [
    #navbar
    path('',                   home_view,                  name='home'),
    path('vaccine/',           vaccine_view,               name='vaccine'),
    path('data/',              data_view),
    #covid province pages
    path('centralcovid/',      covid_central_view,         name='centralcovid'),
    path('copperbeltcovid/',   covid_copperbelt_view,      name='copperbeltcovid'),
    path('easterncovid/',      covid_eastern_view,         name='easterncovid'),
    path('luapulacovid/',      covid_luapula_view,         name='luapulacovid'),
    path('lusakacovid/',       covid_lusaka_view,          name='lusakacovid'),
    path('muchingacovid/',     covid_muchinga_view,        name='muchingacovid'),
    path('northerncovid/',     covid_northern_view,        name='northerncovid'),
    path('northwesterncovid/', covid_northwestern_view,    name='northwesterncovid'),
    path('southerncovid/',     covid_southern_view,        name='southerncovid'),
    path('westerncovid/',      covid_western_view,         name='westerncovid'),
    #covid southern district pages
    path('chibombocovid/',      chibombo_view,         name='chibombocovid'),
    #vaccine pages
    path('centralvaccine/',      vaccine_central_view,         name='centralvaccine'),
    path('copperbeltvaccine/',   vaccine_copperbelt_view,      name='copperbeltvaccine'),
    path('easternvaccine/',      vaccine_eastern_view,         name='easternvaccine'),
    path('luapulavaccine/',      vaccine_luapula_view,         name='luapulavaccine'),
    path('lusakavaccine/',       vaccine_lusaka_view,          name='lusakavaccine'),
    path('muchingavaccine/',     vaccine_muchinga_view,        name='muchingavaccine'),
    path('northernvaccine/',     vaccine_northern_view,        name='northernvaccine'),
    path('northwesternvaccine/', vaccine_northwestern_view,    name='northwesternvaccine'),
    path('southernvaccine/',     vaccine_southern_view,        name='southernvaccine'),
    path('westernvaccine/',      vaccine_western_view,         name='westernvaccine'),
    path('admin/', admin.site.urls),
]
"""zcovid URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
