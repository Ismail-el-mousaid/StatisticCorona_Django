#from flask import Flask, render_template, request
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

filename = 'covid16112020.json'


@csrf_exempt
def index(request):
    if request.method == 'GET':
        res = render(request, 'index.html')
        return HttpResponse(res)
    else:
        country1 = request.POST.get('country1','')
        country2 = request.POST['country2']
        country3 = request.POST['country3']
        print(country1, country2, country3)

        casesCountry1 = getCases(country1)
        casesCountry2 = getCases(country2)
        casesCountry3 = getCases(country3)
        print("casesCountry1: ", casesCountry1)

        deathsCountry1 = getDeaths(country1)
        deathsCountry2 = getDeaths(country2)
        deathsCountry3 = getDeaths(country3)
        print(deathsCountry1)

        dateLabels = getDates(country1)
        print(dateLabels)

        resultat = render(request, 'index.html', {"country1": country1, "country2": country2, "country3": country3,
                       "casesCountry1": casesCountry1, "casesCountry2": casesCountry2, "casesCountry3": casesCountry3,
                       "deathsCountry1": deathsCountry1, "deathsCountry2": deathsCountry2,
                       "deathsCountry3": deathsCountry3, "dateLabels": dateLabels})
        return HttpResponse(resultat)


def getCases(country):
    with open(filename) as json_file:
        jsonData = json.load(json_file)
        caseList =[]
        for record in jsonData['records']:
            if record['countryterritoryCode']==country:
                caseList.append(int(record['cases']))
    return (list(reversed(caseList)))

def getDeaths(country):
    with open(filename) as json_file:
        jsonData = json.load(json_file)
        deathsList =[]
        for record in jsonData['records']:
            if record['countryterritoryCode']==country:
                deathsList.append(int(record['deaths']))
    return (list(reversed(deathsList)))

def getDates(country):
    with open(filename) as json_file:
        jsonData = json.load(json_file)
        dateRepList =[]
        for record in jsonData['records']:
            if record['countryterritoryCode']==country:
                dateRepList.append(record['dateRep'])
    return (list(reversed(dateRepList)))




