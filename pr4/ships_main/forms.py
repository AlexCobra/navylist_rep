from django import forms
from ships_main.models import ship_main, Builder, Power, Propulsion, Endurance, Commanders, ArmDevices, Armour, Devices, Pictures, Armaments, Class, Type


class ShipmainForm(forms.ModelForm):
	class Meta:
		model = ship_main	
		fields = '__all__'
