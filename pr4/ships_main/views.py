from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from ships_main.models import ship_main

class ShipCreate(CreateView):
        model = ship_main
        fields = ['name', 'unique_name', 'builder', 'oredered', 'laid_down', 'launched', 'fate', 'ship_class', 'ship_type', 'displacement_norm', 'desplacement_deep', 'length', 'beam', 'draught', 'power', 'propulsion', 'speed_surf', 'speed_sub', 'endurance', 'crew_peace', 'crew_war', 'commanders', 'armament', 'armour', 'devices', 'story', 'pictures']
class ShipUpdate(UpdateView):
        model = ship_main
        fields = ['name', 'unique_name', 'builder', 'oredered', 'laid_down', 'launched', 'fate', 'ship_class', 'ship_type', 'displacement_norm', 'desplacement_deep', 'length', 'beam', 'draught', 'power', 'propulsion', 'speed_surf', 'speed_sub', 'endurance', 'crew_peace', 'crew_war', 'commanders', 'armament', 'armour', 'devices', 'story', 'pictures']
class ShipDelete(DeleteView):
        model = ship_main
        success_url = reverse_lazy('shipinfo')
        
def shipinfo(request):
	return render(request, 'ships/rnavy/shipinfo.html', {"shipinfo":shipinfo.objects.all()})

#def ship(request, ship_name_url):
#	context = RequestContext(request)
#	ship_name = ship_name_url.replace('_', ' ')
#	context_dict = {'ship_name': ship_name}
#	try:
#		ship = Ship_main.objects.get(unique_name=ship_name)
#		context_dict['ship'] = ship
#	except Ship_main.DoesNotExist:
#		pass
#	return render_to_response('ships/rnavy/shipinfo.html', context_dict, context)

#def rnavy_index(request):
#	context = RequestContext(request)
#	ship_class_list = ship_main.

def index(request):
	return render(request, 'ships/index.html')

def rnavy_index(request):
	context = RequestContext(request)
	ship_list = ship_main.objects.order_by ('unique_name')[:20]
	context_dict = {'ships': ship_list}
	return render_to_response('ships/rnavy/index.html', context_dict, context)
# Create your views here.
