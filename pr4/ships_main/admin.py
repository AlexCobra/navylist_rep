from django.contrib import admin
from ships_main.models import ship_main, Builder, Power, Propulsion, Endurance, Commanders, Armaments, ArmDevices, Armour, Devices, Pictures, Class, Type

##class ArmamentQuantityInLine(admin.TabularInline):
##    model = ArmamentQuantity
##    extra = 1
##
##class ShipMainAdmin(admin.ModelAdmin):
##    list_diplay = ('name', 'unique_name', 'builder', 'ordered', 'laid_down', 'launched',
##                   'fate', 'ship_class', 'ship_type', 'displacement_norm', 'displacement_deep',
##                   'length', 'beam', 'draught', 'power', 'propulsion', 'speed_surf', 'speed_sub',
##                   'endurance', 'crew_peace', 'crew_war', 'commanders', 'armament', 'armour',
##                   'devices', 'story', 'pictures')
##    search_fields = ('name',)
##    inlines = [ArmamentQuantityInLine,]
##
##class ArmamentsAdmin(admin.ModelAdmin):
##    inline = (ArmamentQuantityInLine,)
    
admin.site.register(ship_main)
admin.site.register(Builder)
admin.site.register(Power)
admin.site.register(Propulsion)
admin.site.register(Endurance)
admin.site.register(Commanders)
admin.site.register(Armaments)
admin.site.register(ArmDevices)
admin.site.register(Armour)
admin.site.register(Devices)
admin.site.register(Pictures)
admin.site.register(Class)
admin.site.register(Type)

