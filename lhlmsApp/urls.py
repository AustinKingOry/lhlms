from django.urls import path
from .import views

urlpatterns = [
    path('login/', views.loginPage, name = 'login'),
    path('register/', views.registerPage, name = 'register'),
    path('logout/', views.logoutUser, name = 'logout'),

    path('', views.home, name = 'home'),
    path('books/', views.books, name = 'books'),
    path('staff/', views.staff, name = 'staff'),
    path('students/', views.students, name = 'students'),
    path('book_order/', views.Order, name = 'book_order'),
    path('contact/', views.Contact, name = 'contact'),
    path('thanks/', views.Thanks, name = 'thanks'),
   

    path('create_borrow/', views.createBorrow, name = 'create_borrow'),
    path('create_order/', views.createOrder, name = 'create_order'),

    #
    path('update_borrow/<str:pk>/', views.updateBorrow, name = 'update_borrow'),
    path('update_order/<str:pk>/', views.updateOrder, name = 'update_order'),
    path('update_student/<str:pk>/', views.updateStudent, name = 'update_student'),
    path('update_staff/<str:pk>/', views.updateStaff, name = 'update_staff'),
    path('update_book/<str:pk>/', views.updateBook, name = 'update_book'),
    #path('update_author/<str:pk>/', views.updateAuthor, name = 'update_author'),

    path('delete_order/<str:pk>/', views.deleteOrders, name = 'delete_order'),
    path('delete_borrow/<str:pk>/', views.deleteBorrow, name = 'delete_borrow'),
    path('delete_student/<str:pk>/', views.deleteStudent, name = 'delete_student'),
    path('delete_staff/<str:pk>/', views.deleteStaff, name = 'delete_staff'),
    #

    path('add_student/', views.addStudent, name = 'add_student'),
    path('add_book/', views.addBook, name = 'add_book'),
    path('add_staff/', views.addStaff, name = 'add_staff'),
    path('add_publisher/', views.addPublisher, name = 'add_publisher'),
    path('add_author/', views.addAuthor, name = 'add_author'),
]

#{% url 'update_order' order.id %}
