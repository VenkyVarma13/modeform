from django import forms
# from .models import studentmodel

class studentform(forms.Form):
    name = forms.CharField()
    rollno = forms.IntegerField()
    email = forms.EmailField()
    feedback = forms.CharField(widget=forms.Textarea)
        