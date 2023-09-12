from django.contrib import admin
from napp.models import Employee

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
	list_display=['EmpName','EmpId','Desg','Doj','Dep','Sal','Exp']

admin.site.register(Employee,EmployeeAdmin)