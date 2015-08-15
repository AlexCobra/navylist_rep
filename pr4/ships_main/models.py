from django.db import models

class ship_main(models.Model):
    name = models.CharField(max_length=128),
    builder = models.ForeignKey(Builder),
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
    power = models.ForeignKey(Power),
    propulsion = models.ForeignKey(Propulsion),
    speed_surf = models.IntegerField(),
    speed_sub = models.IntegerField(),
    endurance = models.ForeignKey(Endurance),
    crew_peace = models.IntegerField(),
    crew_war = models.IntegerField(),
    commanders = models.ForeignKey(Commanders),
    armament = models.ForeignKey(Armament),
    armour = models.ForeignKey(Armour),
    devices = models.ForeignKey(Devices),
    story = models.TextField(),
    pictures = models.ForeignKey(Pictures),
    
    def __str__(self):              # __unicode__ on Python 2
        return self.name

# Create your models here.
