from django.shortcuts import render, HttpResponseRedirect, Http404
from .forms import PlacesForm

from .models import Place

# ip geolocation
# import pygeoip
# from pygeoip import GeoIP


import uuid
def get_ref_id():
	ref_id = str(uuid.uuid4())[:11].replace('-', '').lower()
	try:
		id_exists = Place.object.get(ref_id=ref_id)
		get_ref_id()
	except:
		return ref_id



# "standard" form of catch-all ips
def get_ip(request):
	try:
		x_forward = request.META.get("HTTP_X_FORWORDED")
		if x_forward:
			ip = x_forward.split(',')[0]
		else:
			ip = request.META.get("REMOTE_ADDR")
	except:
		ip = ""
	return ip


def share(request, ref_id):

	print request

	# iwent = "IWENT!"
	iwent = request.GET.get('iwent')


	try:
		place_obj = Place.objects.get(ref_id=ref_id)
		template = "share.html"
		# ref_url = "http://hellowhereareyougoing.com/?ref=%s" %(ref_id)
		ref_url = "http://127.0.0.1:8000/?ref=%s" %(ref_id)
		context = {"ref_id": ref_id, "ref_url": ref_url, "iwent": iwent}
		return render(request, template, context)
	except:
		raise Http404



def home(request):

	# geolocation code:
		# gi = pygeoip.GeoIP('GeoIP.dat')
		# gi.country_code_by_name('google.com')
		# gi.country_code_by_addr('64.233.161.99')
		# gi.country_name_by_addr('64.233.161.99')
 
		# gi = pygeoip.GeoIP('GeoIPCity.dat')
		# gi.record_by_addr('ip_address')

	# validates if form is valid or not
	form = PlacesForm(request.POST or None)

	# if valid, continues
	if form.is_valid():
		new_place = form.save(commit=False)
		
		ip_address = get_ip(request)
		# code that gets stuff from the form inputs
		iwent_input = form.cleaned_data['iwent']
		iam_input = form.cleaned_data['iam']
		igo_input = form.cleaned_data['igo']

		# creates stugg in the DB
		new_place_old, created = Place.objects.get_or_create(
			ip_address=ip_address,
			iwent=iwent_input,
			iam=iam_input,
			igo=igo_input)

		# does something if object was created in DB
		if created:
			new_place_old.ref_id = get_ref_id()
			new_place_old.ip_address = get_ip(request)
			new_place_old.save()
		# redirect here
		return HttpResponseRedirect("/%s" %(new_place_old.ref_id))

	context = {"form": form}
	template = "home.html"
	return render(request, template, context)




# def home(request):
# 	# print request.POST['iwent'], request.POST['name']

# 	# validates if form is valid or not
# 	form = PlacesForm(request.POST or None)
# 	# if valid, continues

# 	if form.is_valid():
# 		# code that gets stuff from the form inputs
# 		# ip = request.META['REMOTE_ADDR']


# 		iwent_input = form.cleaned_data['iwent']
# 		iam_input = form.cleaned_data['iam']
# 		igo_input = form.cleaned_data['igo']

# 		# linea que crea en DB la informacion
# 		new_place, created = Place.objects.get_or_create(iwent=iwent_input, iam=iam_input, igo=igo_input)

# 		# does something if object was created in DB
# 		if created:
# 			print "created object!"


# 	context = {"form": form}
# 	template = "home.html"





# 	# Place.ip = request.META['REMOTE_ADDR']

# 	# obj = form.save(commit=False)
# 	# obj.ip_address = request.META['REMOTE_ADDR']
# 	# obj.save()





# 	return render(request, template, context)