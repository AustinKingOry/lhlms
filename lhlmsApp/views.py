from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
#@login_required(login_url='login')

from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage

from .models import *
from .forms import *
from .filters import *

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.info(request, 'username or password incorrect')
    mixture = {}
    return render(request, 'apps/login.html', mixture)

def logoutUser(request):
    logout(request)
    return redirect('/')

def registerPage(request):
    
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = createUserForm()

        if request.method == 'POST':
            form = createUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
            return redirect('/login')

    mixture = {'form':form}
    return render(request, 'apps/register.html', mixture)

def home(request):
    student = Student.objects.all()
    orders = Book_orders.objects.all()
    books = Books.objects.all()

    total_students = student.count()

    total_books = Books.objects.all().count()
    
    bk_borrow = Book_borrowed.objects.all().order_by('-id')
    total_books_borrowed = bk_borrow.count()

   

    #borrowList = Book_borrowed.objects.values_list('stud_name', flat=True).order_by('stud_name').distinct()
    

    total_orders = orders.count()
    delivered = orders.filter(status = 'Delivered Order').count()
    pending = orders.filter(status = 'Pending Order').count()

    myfilter = borrowFilter(request.GET, queryset = bk_borrow)
    bk_borrow = myfilter.qs

    mixture ={'total_students':total_students,'total_books':total_books, 'pending':pending, 'delivered':delivered, 'orders':orders, 'total_orders':total_orders,'bk_borrow':bk_borrow, 'total_books_borrowed':total_books_borrowed, 'myfilter':myfilter} 

    return render(request, 'apps/dashboard.html', mixture)

def books(request):
    books = Books.objects.all().order_by('-id')
    total_books = books.count()

    myfilter = bookFilter(request.GET, queryset = books)
    books = myfilter.qs

    mixture = {'total_books':total_books,'books':books, 'myfilter':myfilter }
    return render(request, 'apps/books.html', mixture)

def Order(request):
    books = Books.objects.all()
    total_books = books.count()
    
    orders = Book_orders.objects.all().order_by('-id')
    total_orders = orders.count()
    delivered = orders.filter(status = 'Delivered Order').count()
    pending = orders.filter(status = 'Pending Order').count()

    myfilter = orderFilter(request.GET, queryset = orders)
    orders = myfilter.qs

    mixture = {'total_books':total_books,'books':books, 'pending':pending, 'delivered':delivered, 'orders':orders, 'total_orders':total_orders, 'myfilter':myfilter} 
    return render(request, 'apps/book_order.html', mixture)

def staff(request):
    staff = Staff.objects.all().order_by('-id')
    total_staff = staff.count()

    myfilter = staffFilter(request.GET, queryset = staff)
    staff = myfilter.qs

    mixture = {'staff':staff, 'total_staff':total_staff, 'myfilter':myfilter}

    return render(request, 'apps/staff.html', mixture)

def students(request):

    students = Student.objects.all().order_by('-id')
    total_students = students.count()
    
    myfilter = studentFilter(request.GET, queryset = students)
    students = myfilter.qs
    mixture = {'total_students':total_students, 'students':students, 'myfilter':myfilter}

    return render(request,'apps/students.html', mixture)

def createBorrow(request):
    form = Book_borrowedForm()


    if request.method == 'POST':
        #print('Printing POST', request.POST)
        form = Book_borrowedForm(request.POST)
        if form.is_valid():
            form.save()
            

            return redirect('/')

    mixture = {'form':form}
    return render(request, 'apps/borrow_form.html', mixture)

@login_required(login_url='login')
def createOrder(request):

    form = Book_ordersForm()
    if request.method == 'POST':
        form = Book_ordersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/book_order')

    mixture = {'form':form}
    return render(request, 'apps/order_form.html', mixture)

@login_required(login_url='login')
def updateOrder(request, pk):
    order = Book_orders.objects.get(id=pk)
    form = Book_ordersForm(instance=order)
       
    if request.method == 'POST':
        form = Book_ordersForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/book_order')

    mixture = {'form':form}
    return render(request, 'apps/order_form.html', mixture)

@login_required(login_url='login')
def updateBorrow(request, pk):
    borrow = Book_borrowed.objects.get(id=pk)
    form = Book_borrowedForm(instance=borrow)

    if request.method == 'POST':
        form = Book_borrowedForm(request.POST, instance=borrow)
        if form.is_valid():
            form.save()
            return redirect('/')

    mixture = {'form':form}
    return render(request, 'apps/order_form.html', mixture)

@login_required(login_url='login')
def updateStudent(request, pk):
    student = Student.objects.get(id=pk)
    form = StudentForm(instance=student)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('/students')

    mixture = {'form':form}
    return render(request, 'apps/order_form.html', mixture)

@login_required(login_url='login')
def updateStaff(request, pk):
    staff = Staff.objects.get(id=pk)
    form = StaffForm(instance=staff)

    if request.method == 'POST':
        form =  StaffForm(request.POST, instance=staff)
        if form.is_valid():
            form.save()
            return redirect('/staff')

    mixture = {'form':form}
    return render(request, 'apps/order_form.html', mixture)

@login_required(login_url='login')
def addStudent(request):

    form = StudentForm()
    if request.method == 'POST':
        #print('Printing POST', request.POST)
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/students')

    mixture = {'form':form}

    return render(request, 'apps/add_student.html', mixture)

@login_required(login_url='login')
def addBook(request):

    form = BooksForm()
    if request.method == 'POST':
        #print('Printing POST', request.POST)
        form = BooksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/staff')

    mixture = {'form':form}

    return render(request, 'apps/add_book.html', mixture)

@login_required(login_url='login')
def addPublisher(request):

    form = PublisherForm()
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/books')

    mixture = {'form':form}

    return render(request, 'apps/add_publisher.html', mixture)

@login_required(login_url='login')
def addAuthor(request):

    form = AuthorForm()
    if request.method == 'POST':
        #print('Printing POST', request.POST)
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/books')

    mixture = {'form':form}

    return render(request, 'apps/add_author.html', mixture)

@login_required(login_url='login')
def addStaff(request):

    form = StaffForm()
    if request.method == 'POST':
        #print('Printing POST', request.POST)
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    mixture = {'form':form}

    return render(request, 'apps/add_staff.html', mixture)

@login_required(login_url='login')
def deleteOrders(request, pk):
    order = Book_orders.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/book_order')

    mixture = {'item':order}

    return render(request, 'apps/delete_order.html', mixture)

@login_required(login_url='login')
def deleteBorrow(request, pk):
    bk_borrow = Book_borrowed.objects.get(id=pk)
    if request.method == "POST":
        bk_borrow.delete()
        return redirect('/')

    mixture = {'item':bk_borrow}

    return render(request, 'apps/delete_borrow.html', mixture)

@login_required(login_url='login')
def deleteStudent(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == "POST":
        student.delete()
        return redirect('/students')

    mixture = {'item':student}

    return render(request, 'apps/delete_student.html', mixture)

@login_required(login_url='login')
def deleteStaff(request, pk):
    staff = Staff.objects.get(id=pk)
    if request.method == "POST":
        staff.delete()
        return redirect('/staff')

    mixture = {'item':staff}

    return render(request, 'apps/delete_staff.html', mixture)

@login_required(login_url='login')
def updateBook(request, pk):
    books = Books.objects.get(id=pk)
    form = BooksForm(instance=books)

    if request.method == 'POST':
        form = BooksForm(request.POST, instance=books)
        if form.is_valid():
            form.save()
            return redirect('/books')

    mixture = {'form':form}
    return render(request, 'apps/order_form.html', mixture)

@login_required(login_url='login')
def Contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            #form.save()
            #messages.success(request, 'email has been sent sucessfully ')
            # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            EmailMessage(
                'Contact Form Submission from {}'.format(name),
                message,
               '<mandelasiganga014@outlook.com>', # Send from (your website)
               ['mandelasiganga014@outlook.com'], # Send to (your admin email)
               [],
               reply_to=[email] # Email from the form to get back to
           ).send()

            return redirect('/thanks')
    else:
        form = ContactForm()
    return render(request, 'apps/contact.html', {'form': form})
    
def Thanks(request):
    return render(request, 'apps/thanks.html')

