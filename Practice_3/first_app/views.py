from django.shortcuts import render
from .forms import ExampleForm, Example
# Create your views here.
def home(request):
    form = ExampleForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, './first_app/home.html', {'form':form})

def model(request):
    form = Example(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, './first_app/home.html', {'form':form})
        
