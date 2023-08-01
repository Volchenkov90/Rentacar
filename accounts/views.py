from django.shortcuts import get_object_or_404, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import redirect
from django.db import IntegrityError 
from .forms import UserCreateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .models import Review

# Create your views here.


def signupaccount(request):
    if request.method == 'GET':
        return render(request, 'signupaccount.html',{'form':UserCreateForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    request.POST['username'],
                    password= request.POST['password1']
                    )
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signupaccount.html', {'form':UserCreateForm, 'error':'Username already taken. Choose new username.'})
        else:
            return render(request, 'signupaccount.html', {'form':UserCreateForm, 'error':'Passwords do not match'})
    
def logoutaccount(request):
    logout(request)
    return redirect('home')

def loginaccount(request):
    if request.method == 'GET':
        return render(request, 'loginaccount.html',
        {'form':AuthenticationForm})
    else:
        user = authenticate(request,
        username=request.POST['username'],
        password=request.POST['password'])
        if user is None:
            return render(request,'loginaccount.html', {'form': AuthenticationForm(), 
                                                        'error': 'username and password do not match'})
        else:
            login(request,user)
            return redirect('home')

def makereview(request):
    return render(request, 'makereview.html')

def newreview(request):
    if request.method == 'POST':
        
        user = request.user
        text = request.POST.get('somewords')
        mark_condition = request.POST.get('condition')
        mark_staff = request.POST.get('staff')
        mark_cost = request.POST.get('cost')
        mark_location = request.POST.get('location')
        average_mark = round((int(mark_condition) + int(mark_staff) + int(mark_cost) + int(mark_location))/4, 1)

        new_review = Review(text=text, mark_condition=mark_condition, mark_staff=mark_staff, mark_cost=mark_cost, mark_location=mark_location, average_mark=average_mark, user=user)
        new_review.save()
        
    return render(request, 'successreview.html')
def reviews(request):
    user_reviews = Review.objects.all()
    return render(request, 'reviews.html', {'user_reviews':user_reviews})




