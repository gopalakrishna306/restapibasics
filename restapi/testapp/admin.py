from django.contrib import admin
from testapp.models import student,token

# Register your models here.
class studentadmin(admin.ModelAdmin):
    model=student
    fields = ['name','age','sex','address']
    list_display = ['name','age','sex','address']

class tokenadmin(admin.ModelAdmin):
    model=token
    fields = ['name','tokenno']
    list_display =['name','tokenno']


admin.site.register(student,studentadmin)
admin.site.register(token,tokenadmin)
