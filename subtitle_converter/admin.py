from django.contrib import admin

# Register your models here.
from .models import BtnCounter

class BtnCounterAdmin(admin.ModelAdmin):
    readonly_fields = ["visit_counter"]
admin.site.register(BtnCounter, BtnCounterAdmin)