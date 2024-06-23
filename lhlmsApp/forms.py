from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.validators import EmailValidator

from .models import *

class Book_borrowedForm(ModelForm):
    class Meta:
        model = Book_borrowed
        fields = '__all__'

class Book_ordersForm(ModelForm):
    class Meta:
        model = Book_orders
        fields = '__all__'
        exclude=['status']

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class BooksForm(ModelForm):
    class Meta:
        model = Books
        fields = '__all__'

class StaffForm(ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'

class PublisherForm(ModelForm):
    class Meta:
        model = Publisher
        fields = '__all__'

class AuthorForm(ModelForm):
    class Meta:
        model = Author_detail
        fields = '__all__'

class createUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.CharField(validators=[EmailValidator()])
    phone = forms.CharField(max_length=15)
    subject = forms.CharField(max_length=250)
    message = forms.CharField(widget=forms.Textarea)
 