from django.contrib import admin
from .models import Employee, Department,Role
# Register your models here.

admin.site.register(Department)
admin.site.register(Role)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('eid','ename','eemail','salary','dept','role','phone','hire_date')
    ordering = ('eid',)
