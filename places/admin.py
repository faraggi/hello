from django.contrib import admin

# Register your models here.

from .models import Place

class PlaceAdmin(admin.ModelAdmin):
	list_display = ['ip_address', 'iwent', 'iam', 'igo']
	class Meta:
		model = Place

admin.site.register(Place, PlaceAdmin)