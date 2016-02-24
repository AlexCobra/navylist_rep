from django import forms
from ships_main.models import ship_main, Builder, Power, Propulsion, Endurance, Commanders, ArmDevices, Armour, Devices, Pictures, Armaments, Class, Type


class ShipmainForm(forms.ModelForm):
	name = forms.CharField(max_length=128, strip=True, help_text="Ship Name here")
	unique_name = forms.CharField(max_length=128, strip=True, help_text="Unique Ship Name")
	builder = forms.ModelChoiceField(queryset=Builder.objects.all(), to_field_name="name")
	ordered = forms.DateField()
	laid_down = forms.DateField()
	launched = forms.DateField()
	fate = forms.DateField()
	ship_class = forms.ModelChoiceField(queryset=Class.objects.all(), to_field_name="class_data")
	ship_type = forms.ModelChoiceField(queryset=Type.objects.all(), to_field_name="class_type")
	displacement_norm = forms.IntegerField()
	displacement_deep = forms.IntegerField()
	length = forms.DecimalField()
	beam = forms.DecimalField()
	draught = forms.DecimalField()
	power = forms.ModelChoiceField(queryset=Power.objects.all())
	propulsion = forms.ModelMultipleChoiceField(queryset=Propulsion.objects.all())
	speed_surf = forms.DecimalField()
	speed_sub = forms.DecimalField()
	endurance = forms.ModelChoiceField(queryset=Endurance.objects.all())
	crew_peace = forms.IntegerField()
	crew_war = forms.IntegerField()
	commanders = forms.ModelMultipleChoiceField(queryset=Commanders.objects.all(), to_field_name="second_name")
	armament = forms.ModelMultipleChoiceField(queryset=Armaments.objects.all(), to_field_name="armament_type")
	armour = forms.ModelChoiceField(queryset=Armour.objects.all())
	devices = forms.ModelMultipleChoiceField(queryset=Devices.objects.all(), to_field_name="device_type")
	story = forms.CharField(widget=forms.Textarea(), help_text="Story")
	picture = forms.ImageField()

	class Meta:
		
		fields = '__all__'
