from django.contrib import admin

# Register your models here.
#sunt mihnea7, iar parola e betivul #10
from .models import Cooler, CPU, SSD, Calculator, PlacaGrafica

admin.site.site_header="Arda"
admin.site.site_title="Master Room"
admin.site.index_title="Welcome to the Command Deck"
class CoolerAdmin(admin.ModelAdmin):
    list_display=('frecventa', 'pret')
    search_fields=('frecventa',)
    fieldsets=(
        ('Titlul I', {
            'fields': ('frecventa',)
        }
        ),
        (
            'Titlul II', {
                'fields': ('pret',)
            }
        )
    )
class CalculatorAdmin(admin.ModelAdmin):
    search_fields=('RAM',)
    list_filter=['RAM']
admin.site.register(Cooler)
admin.site.register(CPU)
admin.site.register(SSD)
admin.site.register(Calculator)
admin.site.register(PlacaGrafica)