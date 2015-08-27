from django.contrib import admin
from ships_main.models import ship_main, Builder, Power, Propulsion, Endurance, Commanders, ArmamentQuantity, Armaments, Armour, Devices, Pictures

admin.site.register(ship_main)
admin.site.register(Builder)
admin.site.register(Power)
admin.site.register(Propulsion)
admin.site.register(Endurance)
admin.site.register(Commanders)
admin.site.register(ArmamentQuantity)
admin.site.register(Armaments)
admin.site.register(Armour)
admin.site.register(Devices)
admin.site.register(Pictures)

# Register your models here.
