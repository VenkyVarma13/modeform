from django import forms
from django.core import validators
# from .models import studentmodel

class studentform(forms.Form):
    name = forms.CharField()
    rollno = forms.IntegerField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    rpassword = forms.CharField(widget=forms.PasswordInput)
    feedback = forms.CharField(widget=forms.Textarea, validators=[validators.MaxLengthValidator(40), validators.MinLengthValidator(10)])
    bot_handler = forms.CharField(required=False, widget=forms.HiddenInput)

    def clean(self):
        print('Total Form Validation')
        cleaned_data = super().clean()
        inputpassword = cleaned_data['password']
        inputrpassword = cleaned_data['rpassword']
        if inputpassword != inputrpassword:
            raise forms.ValidationError('Password is Not matched')
        bot_hnd = cleaned_data['bot_handler']
        if len(bot_hnd) > 0:
            raise forms.ValidationError('thank bot')