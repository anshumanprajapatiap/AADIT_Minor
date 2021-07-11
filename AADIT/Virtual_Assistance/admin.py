from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(user_type, Topics, proftype, departmentincollege, \
    faculty_general_information, facultycabinoffice, user_detail)
    
class ViewAdmin(ImportExportModelAdmin):
    pass


@admin.register(notice_data)
class ViewAdmin(ImportExportModelAdmin):
    pass
