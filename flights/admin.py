from django.contrib import admin
from .models import Flight, Airport, Passenger

class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")  # Exibe esses campos no admin

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)  # Permite selecionar múltiplos voos para um passageiro

admin.site.register(Airport)  # Registra o modelo Airport no admin
admin.site.register(Flight, FlightAdmin)  # Registra o modelo Flight com configurações personalizadas
admin.site.register(Passenger, PassengerAdmin)  # Registra o modelo Passenger com filtro horizontal
