from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from countries.models import Country
from countries.serializers import CountriesSerializer

def index(request):
    return render(request, 'index.html')

@api_view(['GET', 'POST'])
def countries_list(request):
    if request.method == 'GET':
        countries = Country.objects.all()
        name = request.GET.get('name', None)
        if name is not None:
            countries = countries.filter(name__icontains=name)
        countries_serializer = CountriesSerializer(countries, many=True)
        return JsonResponse(countries_serializer.data, safe=False)
    elif request.method == 'POST':
        countries_data = JSONParser().parse(request)
        countries_serializer = CountriesSerializer(data=countries_data)
        if countries_serializer.is_valid():
            countries_serializer.save()
            return JsonResponse(countries_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(countries_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse({'message': 'Invalid request method'}, status=status.HTTP_400_BAD_REQUEST)