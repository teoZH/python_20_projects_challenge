from django.shortcuts import render, redirect, get_object_or_404
from .forms import CarsForm
from .models import Cars
from django.http import Http404


# Create your views here.


def homepage(request):
    cars = Cars.objects.all()
    return render(request, 'index.html', {'cars': cars})


def create(request):
    context = {}
    if request.method == 'POST':
        form = CarsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = CarsForm()
    context = {
        'form': form
    }
    return render(request, 'create_cars.html', context)


def delete(request, car_id):
    car = get_object_or_404(Cars, pk=car_id)
    if request.method == "POST":
        car.delete()
        return redirect('homepage')
    else:
        form = CarsForm(instance=car)
        for f in form.fields:
            form.fields[f].disabled=True
    context = {
        'form': form
    }
    return render(request, 'delete_cars.html', context)


def details(request, car_id):
    return render(request, 'details.html')
