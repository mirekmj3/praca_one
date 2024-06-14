from django.contrib import admin

# Register your models here.

from .models import SWATH
from import_export.admin import ImportExportModelAdmin

admin.site.register(SWATH, ImportExportModelAdmin)