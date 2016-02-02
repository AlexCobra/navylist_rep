from django.db import models
from django.core.urlresolvers import reverse

class ship_main(models.Model):
        name = models.CharField(max_length=128, default='')
        unique_name = models.CharField(max_length=128, unique=True)
        builder = models.ForeignKey('Builder', blank=True)
        ordered = models.DateField(blank=True, default='1000-01-01')
        laid_down = models.DateField(blank=True, default='1000-01-01')
        launched = models.DateField(blank=True, default='1000-01-01')
        fate = models.DateField(blank=True, default='1000-01-01')
        ship_class = models.ForeignKey('Class')
        ship_type = models.ForeignKey('Type', default='')
        displacement_norm = models.IntegerField(blank=True)
        displacement_deep = models.IntegerField(blank=True)
        length = models.DecimalField(blank=True, max_digits=5, decimal_places=2)
        beam = models.DecimalField(blank=True, max_digits=5, decimal_places=2)
        draught = models.DecimalField(blank=True, max_digits=5, decimal_places=2, null=True)
        power = models.ForeignKey('Power', blank=True, default='')
        propulsion = models.ForeignKey('Propulsion', blank=True, default='')
        speed_surf = models.DecimalField(blank=True, max_digits=5, decimal_places=2)
        speed_sub = models.DecimalField(blank=True, max_digits=5, decimal_places=2)
        endurance = models.ForeignKey('Endurance', blank=True)
        crew_peace = models.IntegerField(blank=True)
        crew_war = models.IntegerField(blank=True)
        commanders = models.ForeignKey('Commanders', blank=True, null=True, default='')
        armament = models.ForeignKey('Armaments', blank=True, null=True, default='')
        armour = models.ForeignKey('Armour', blank=True, null=True, default='')
        devices = models.ForeignKey('Devices', blank=True, null=True, default='')
        story = models.TextField(blank=True, null=True, default='')
        pictures = models.ForeignKey('Pictures', blank=True, null=True)
    
        def __str__(self):              # __unicode__ on Python 2
            return (self.unique_name)

        def get_absolute_url(self):
            return reverse('shipinfo', kwargs={'pk': self.pk})


class Builder(models.Model):
    name = models.CharField(max_length=128)
    founded = models.DateField(blank=True, default='1000-01-01')
    defunct = models.DateField(blank=True, default='1000-01-01')
    location = models.CharField(max_length=128, blank=True)
    

    def __str__(self):              # __unicode__ on Python 2
        return (self.name)

class Power(models.Model):
    power_description = models.TextField(blank=True)

class Propulsion(models.Model):
    shafts = models.IntegerField(blank=True, null=True)
    steam_turbines = models.IntegerField(blank=True, null=True)

class Endurance(models.Model):
    range1 = models.IntegerField(blank=True, null=True)
    speed1 = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)
    range2 = models.IntegerField(blank=True, null=True)
    speed2 = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)
    range3 = models.IntegerField(blank=True, null=True)
    speed3 = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)

class Commanders(models.Model):
    first_name = models.CharField(max_length=128, blank=True)
    second_name = models.CharField(max_length=128)
    birthdate = models.DateField(blank=True, default='1000-01-01')
    income_date = models.DateField(blank=True, default='1000-01-01')
    withdraw_date = models.DateField(blank=True, default='1000-01-01')

    def __str__(self):              # __unicode__ on Python 2
        return (self.second_name)

class ArmDevices(models.Model):
    device_type = models.CharField(max_length=128)
    service_start_date = models.DateField(blank=True, default='1000-01-01')
    service_end_date = models.DateField(blank=True, default='1000-01-01')
    manufacturer = models.ForeignKey('Builder', blank=True, null=True)
    number_built = models.IntegerField(blank=True, null=True)
    weight = models.DecimalField(blank=True, max_digits=5, decimal_places=2, null=True)
    length = models.DecimalField(blank=True, max_digits=5, decimal_places=2, null=True)
    calibre = models.DecimalField(blank=True, max_digits=5, decimal_places=2, null=True)
    recoil = models.DecimalField(blank=True, max_digits=5, decimal_places=2, null=True)
    rate_of_fire = models.DecimalField(blank=True, max_digits=5, decimal_places=2, null=True)
    velocity = models.DecimalField(blank=True, max_digits=5, decimal_places=2, null=True)
    max_firing_range = models.CharField(max_length=256, blank=True)
    story = models.TextField(blank=True)

    def __str__(self):              # __unicode__ on Python 2
        return (self.device_type)

class Armour(models.Model):
    belt = models.DecimalField(blank=True, max_digits=5, decimal_places=2)
    deck = models.DecimalField(blank=True, max_digits=5, decimal_places=2)
    barbettes = models.DecimalField(blank=True, max_digits=5, decimal_places=2)
    gun_turrets = models.DecimalField(blank=True, max_digits=5, decimal_places=2)
    conning_tower = models.DecimalField(blank=True, max_digits=5, decimal_places=2)
    bulkheads = models.DecimalField(blank=True, max_digits=5, decimal_places=2)
    magazines = models.DecimalField(blank=True, max_digits=5, decimal_places=2)

class Devices(models.Model):
    device_type = models.CharField(max_length=128)
    description = models.TextField(blank=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.device_type

class Pictures(models.Model):
    picture_name = models.CharField(max_length=128, blank=True)
    picture = models.ImageField(upload_to='/ships_main', max_length=200)
    picture_source = models.URLField()

    def __str__(self):              # __unicode__ on Python 2
        return self.picture_name

class Armaments(models.Model):
    ship_id = models.OneToOneField(ship_main)
    quantity = models.IntegerField()
    armament_type = models.ForeignKey('ArmDevices', blank=False)

class Class(models.Model):
        class_data = models.CharField(max_length=128)
        
        def __str__(self):              # __unicode__ on Python 2
            return self.class_data

class Type(models.Model):
        class_type = models.CharField(max_length=128)

        def __str__(self):              # __unicode__ on Python 2
            return self.class_type
