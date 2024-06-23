from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.utils import timezone

from datetime import date


import random
#from .utils import slugify_instance_title
# Create your models here.

#A function to check length
def stud_reg_no(value):
    an_integer = value
    a_string = str(an_integer)
    number = int (a_string)
    length = len(a_string)
    if number<6000:
            raise ValidationError(
                _('%(value)s cannot be less than 6001')
        )

def staff_reg_no(value):
    an_integer = value
    a_string = str(an_integer)
    number = int (a_string)
    if number<4000:
        raise ValidationError(
            _('%(value)s cannot be less than 4001')
        )
    
def stud_age(value):
    an_integer = value
    a_string = str(an_integer)
    length = int(a_string)
    if length<14:
        raise ValidationError(
        _('%(value)s age needs to be more or equal to 14')
        )

def other_age(value):
    an_integer = value
    a_string = str(an_integer)
    length = int(a_string)
    if length <20:
        raise ValidationError(
            _('%(value)s age needs to be more or equal to 20')
        )


def books_can_borrow(value):
    an_integer = value
    a_string = str(an_integer)
    number = int (a_string)
    if number >3:
        raise ValidationError(
            _('%(value)s Student can only borrow 3 books')
        )

def page_lenght(value):
    an_integer = value
    a_string = str(an_integer)
    digits = len (a_string)
    if digits > 3:
        raise ValidationError(
            _('%(value)s inapproriate! enter again')
        )
    
def book_serial_no(value):
    an_integer = value
    a_string = str(an_integer)
    lenght = len (a_string)
    if lenght !=5 :
        raise ValidationError(
            _('%(value)s invalid serial no: lenght=5')
        )
    

    

def person_id(value):
    an_integer = value
    a_string = str(an_integer)
    lenght = len (a_string)
    if lenght !=8 :
        raise ValidationError(
            _('%(value)s ID should contain 8 digits')
        )
    
def year_lenght(value):
    an_integer = value
    a_string = str(an_integer)
    lenght = len (a_string)
    if lenght !=4 :
        raise ValidationError(
            _('%(value)s Invalid Year')
        )
    
def phone(value):
    an_integer = value
    a_string = str(an_integer)
    lenght = len (a_string)
    if lenght != 12 :
        raise ValidationError(
            _('%(value)s Invalid Phone number')
        )



#Add to model field



class Staff(models.Model):
    ROLE = (
        ('Warden','Warden'),
        ('Security guard','Security guard'),
        ('Developer','Developer'),
        ('Stock management','Stock management'),
        ('Secretary','Secretary'),
    )
    SEX = (
        ('F','F'),
        ('M','M'),
    )
    name = models.CharField(max_length=200, null ="True")
    ID_no = models.PositiveIntegerField(validators=[person_id], null ="True", unique=True)
    reg_no = models.PositiveIntegerField(validators=[staff_reg_no], null ="True", unique=True)
    age = models.PositiveIntegerField(validators=[other_age], null ="True")
    role = models.CharField(max_length=200, null ="True", choices=ROLE)
    email = models.CharField(max_length=60, null ="True", blank = True)
    sex = models.CharField(max_length=200, null ="True", choices=SEX)
    phone_no = models.IntegerField(validators=[phone], null ="True")
    
    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=200, null ="True", unique = True)
    
    city_of_origin = models.CharField(max_length=200, null ="True",)

    def __str__(self):
        return self.name


class Author_detail(models.Model):
    name = models.CharField(max_length=200, null ="True", unique=True)
    Genres = models.CharField(max_length=200, null ="True")
    spouse = models.CharField(max_length=200, null ="True", blank=True)
    other_achievements = models.CharField(max_length=200, null ="True", blank=True)

    def __str__(self):
        return self.name
    
class Books(models.Model):
    STATUS = (
        ('Pending Order','Pending Order'),
        ('Delivered Order','Delivered Order'),
        
    )

    name = models.CharField(max_length=200, null ="True", unique=True)
    Genres = models.CharField(max_length=200, null ="True")
    
    Serial_no = models.PositiveIntegerField(validators=[book_serial_no], null ="True", unique=True)
    
    year_of_publication = models.IntegerField(validators=[year_lenght], null ="True")

    author = models.ForeignKey(Author_detail, null = True, on_delete= models.SET_NULL)

    publisher = models.CharField(max_length=200, null ="True")
    pages =  models.PositiveIntegerField(validators=[page_lenght], null ="True")
    
    in_stock = models.PositiveIntegerField(null ="True")

    def __str__(self):
        return self.name
    
class Student(models.Model):
    name = models.CharField(max_length=200, null ="True")
    FORM = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
    )
    STREAM = (
        ('A','A'),
        ('B','B'),
        ('C','C'),
    )
    SEX = (
        ('F','F'),
        ('M','M'),
       
    )

    form = models.CharField(max_length=200, null ="True", choices=FORM)
   
    stream = models.CharField(max_length=200, null ="True", choices=STREAM)
    reg_no = models.IntegerField(validators=[stud_reg_no], null ="True", unique=True)
    sex = models.CharField(max_length=200, null ="True", choices=SEX)
    age = models.PositiveIntegerField(validators=[stud_age], null ="True")
    date_joined = models.DateTimeField(null = True, auto_now_add = True)

    
    def __str__(self):
        return self.name

    #def get_absolute_url(self):
        #return f'/students/{self.slug}/'
        #return reverse("students", kwargs={'slug': self.slug})

class Book_orders(models.Model):
    STATUS = (
        ('Pending Order','Pending Order'),
        ('Delivered Order','Delivered Order'),
        
    )
    book_name = models.ForeignKey(Books, null= True, on_delete = models.SET_NULL)
    quantity = models.PositiveIntegerField(null ="True")
    publisher_name =  models.ForeignKey(Publisher, null= True, on_delete = models.SET_NULL)
    date_of_order = models.DateTimeField(auto_now_add = True, null ="True")
    status = models.CharField(max_length=200, null ="True", choices = STATUS)

    def __str__(self):
        return self.book_name.name

class Book_borrowed(models.Model):
    FINE = (
        ('Yes','Yes'),
        ('No','No'),
        
    )
    stud_name = models.ForeignKey(Student, null = True, on_delete = models.SET_NULL)
    books_borrowed = models.ForeignKey(Books, null = True, on_delete = models.SET_NULL)
    date_of_borrow = models.DateTimeField(auto_now_add = True, null ="True")
    date_of_return = models.DateTimeField(auto_now_add = True, null ="True")
    

    def __str__(self):
        return self.books_borrowed.name

    @property
    def Day_till(self):
        today = date.today()
        days_till = today - self.date_of_borrow.date()
        days_till_stripped = str(days_till).split(",",1)[0]
        return days_till_stripped

    @property
    def Is_Past(self):
        today = date.today()
        days_till = today - self.date_of_borrow.date()
        days_till_stripped = str(days_till).split(",",1)[0]
        if days_till_stripped>=str(11):
            fine = 'Yes'
        else: 
            fine = 'No'
        return fine
        #if sum := int(self.date_of_borrow.date)+7:
        #    fine = "Yes"
        #else: 
        #   fine = "No"
        #return fine

    @property
    def charges(self):
        today = date.today()
        days_till = today - self.date_of_borrow.date()
        days_till_stripped = str(days_till).split(",",1)[0]
        if days_till_stripped % str(11) == int:
            charges=int+50
        else:
            charges=0
        return charges
 

 