from django.db import models

class ship_main(models.Model):
        name = models.CharField(max_length=128, default=''),
        unique_name = models.CharField(max_length=128, unique=True),
        builder = models.ForeignKey('Builder'),
        ordered = models.DateField(),
        laid_down = models.DateField(),
        launched = models.DateField(),
        fate = models.DateField(),
        ship_class = models.CharField(max_length=128),
        displacement_norm = models.IntegerField(),
        displacement_deep = models.IntegerField(),
        length = models.IntegerField(),
        beam = models.IntegerField(),
        draught = models.IntegerField(),
        power = models.ForeignKey('Power'),
        propulsion = models.ForeignKey('Propulsion'),
        speed_surf = models.IntegerField(),
        speed_sub = models.IntegerField(),
        endurance = models.ForeignKey('Endurance'),
        crew_peace = models.IntegerField(),
        crew_war = models.IntegerField(),
        commanders = models.ForeignKey('Commanders'),
        armament = models.ManyToManyField('Armament', through='ArmamentQuantity'),
        armour = models.ForeignKey('Armour'),
        devices = models.ForeignKey('Devices'),
        story = models.TextField(),
        pictures = models.ForeignKey('Pictures'),
    
        def __str__(self):              # __unicode__ on Python 2
                return (self.name, self.unique_name, self.ship_class)


class Builder(models.Model):
    name = models.CharField(max_length=128),

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Power(models.Model):
    power = models.IntegerField(),
    boilers = models.IntegerField(),
    boilers_type = models.CharField(max_length=128),

    def __str__(self):              # __unicode__ on Python 2
        return self.boilers_type

class Propulsion(models.Model):
    shafts = models.IntegerField(),
    steam_turbines = models.IntegerField(),

class Endurance(models.Model):
    range1 = models.IntegerField(),
    speed1 = models.IntegerField(),
    range2 = models.IntegerField(),
    speed2 = models.IntegerField(),
    range3 = models.IntegerField(),
    speed3 = models.IntegerField(),

class Commanders(models.Model):
    first_name = models.CharField(max_length=128),
    second_name = models.CharField(max_length=128),
    birthdate = models.DateField(),
    income_date = models.DateField(),
    withdraw_date = models.DateField,

def __str__(self):              # __unicode__ on Python 2
        return (self.first_name, self.second_name)

class ArmamentQuantity(models.Model):
    quantity = models.IntegerField(),
    armament_type = models.ForeignKey('Armaments'),
    ship_main = models.ForeignKey('ship_main'),

class Armaments(models.Model):
    device_type = models.CharField(max_length=128),
    service_start_date = models.DateField(),
    service_end_date = models.DateField(),
    manufacturer = models.ForeignKey('Manufacturer'),
    number_built = models.IntegerField(),
    weight = models.IntegerField(),
    length = models.IntegerField(),
    calibre = models.IntegerField(),
    recoil = models.IntegerField(),
    rate_of_fire = models.IntegerField(),
    velocity = models.IntegerField(),
    max_firing_range = models.CharField(max_length=256),
    story = models.TextField(),

    def __str__(self):              # __unicode__ on Python 2
        return (self.device_type, self.max_firing_range, self.story)

class Armour(models.Model):
    belt = models.IntegerField(),
    deck = models.IntegerField(),
    barbettes = models.IntegerField(),
    gun_turrets = models.IntegerField(),
    conning_tower = models.IntegerField(),
    bulkheads = models.IntegerField(),
    magazines = models.IntegerField(),

class Devices(models.Model):
    device_type = models.CharField(max_length=128),
    description = models.TextField(),

    def __str__(self):              # __unicode__ on Python 2
        return (self.device_type, self.description)

class Pictures(models.Model):
    picture_name = models.CharField(max_length=128),
    picture = models.ImageField(upload_to='/ships_main', max_length=200),
    picture_source = models.URLField(),

    def __str__(self):              # __unicode__ on Python 2
        return self.picture_name



