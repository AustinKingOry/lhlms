from django.contrib import admin

# Register your models here.
from .models import *




admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(Publisher)
admin.site.register(Author_detail)
admin.site.register(Books)
admin.site.register(Book_orders)
admin.site.register(Book_borrowed)
