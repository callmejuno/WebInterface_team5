from django.contrib import admin
from .models import Employee
from .models import Department
from .models import Location

admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Location)
