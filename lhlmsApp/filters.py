import django_filters
from django_filters import DateFilter,CharFilter

from .models import *

class orderFilter(django_filters.FilterSet):
    #start_date = DateFilter(field_name="date_of_order", lookup_expr='gte')
    #end_date = DateFilter(field_name="date_of_order", lookup_expr='lte')
    class Meta:
        model = Book_orders
        fields = '__all__'
        exclude = ['book_name', 'quantity', 'date_of_order']
     
class borrowFilter(django_filters.FilterSet):
    class Meta:
        model = Book_borrowed
        fields = '__all__'
        exclude = ['issue_fine','date_of_return']

class studentFilter(django_filters.FilterSet):
   name = CharFilter(field_name="name", lookup_expr='icontains')
   class Meta:
        model = Student
        fields = '__all__'
        exclude = ['date_joined','name', 'stream','reg_no']

class bookFilter(django_filters.FilterSet):
   name = CharFilter(field_name="name", lookup_expr='icontains')
   Genre = CharFilter(field_name="Genres", lookup_expr='icontains')
   class Meta:
        model = Books
        fields = '__all__'
        exclude = ['status','pages','author','name','publisher', 'Genres', 'in_stock']

class staffFilter(django_filters.FilterSet):
    name = CharFilter(field_name="name", lookup_expr='icontains')
    class Meta:
        model = Staff
        fields = '__all__'
        exclude = ['ID_no','reg_no','age','email','phone_no','name']


