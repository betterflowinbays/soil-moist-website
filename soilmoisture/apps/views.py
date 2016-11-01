from django.shortcuts import render

def index(request):
    return render(request, 'soilmoisture/home.html')

def contact(request):
    return render(request, 'soilmoisture/templates/basic.html', {'content':['If you would like to contact me please email me at',' mike.morris@ecodev.vic.gov.au']})
