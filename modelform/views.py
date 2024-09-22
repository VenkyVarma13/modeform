from django.shortcuts import render
from . import forms


# Create your views here.


def thankyou(request):
    return render(request, 'modelform/thankyou.html')


def studentview(request):
    form = forms.studentform()
    if request.method == "POST":
        form = forms.studentform(request.POST)
        if form.is_valid():
            print("form data is validated and printing feedback info")
            print("student name:", form.cleaned_data['name'])
            print("student rollno:", form.cleaned_data['rollno'])
            print("student mail id:", form.cleaned_data['email'])
            print("student feedback:", form.cleaned_data['feedback'])
            return thankyou(request)
    return render(request, 'modelform/feedback.html', {'form': form})
