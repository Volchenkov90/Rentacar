from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from .models import Car
from .models import Questions
from django.contrib import messages

# Create your views here.




def home(request):
    cars = Car.objects.all() 
    return render(request, 'home.html',{'cars': cars})
    
def description(request, car_index): 
    car = get_object_or_404(Car,pk=car_index)    
    return render(request, 'description.html', {'car': car})

def calculator(request, car_index):
    car = get_object_or_404(Car,pk=car_index)
    return render(request, 'calculator.html', {'car': car})

def calc(request, car_index):
    
    if request.method == 'POST':
        days = request.POST.get('days')
        car = get_object_or_404(Car,pk=car_index)
        result = " " 
        days_int = int(days)                     
        if days_int < 7 and days_int > 0:
            result = f"Your price is {car.price_day * days_int} CZK"
        elif days_int > 7 and days_int < 30:
            result = f"Your price is {car.price_week * days_int} CZK"
        elif days_int == 30:
            result = f"Your price is {car.price_month * days_int} CZK"
        else:
            result = "Enter the correct number (1-30) please"            
        messages.info(request, result)
        return redirect('calculator', car_index=car_index)           
    messages.info(request, result)    
    return redirect('calculator', car_index=car_index)
    

def question(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        question = request.POST.get('question')

        contact = Questions(username=username, phone=phone, question=question)
        contact.save()
        
    return render(request, 'success.html')

def contacts(request):
    return render(request, 'contacts.html')





