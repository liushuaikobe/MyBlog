# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

from manage.models import kobe_meta

def manage(request):
	action = request.GET.get('action')
	error = False
	if not action:
		if request.method == 'GET':
			return render_to_response('admin_settings.html', RequestContext(request))
		else:
			# print request.raw_post_data
			if 'blogname' in request.POST and 'numofarticles' in request.POST:
				blogname = request.POST['blogname']
				numofarticles = request.POST['numofarticles']
				if not blogname and not numofarticles:
					return render_to_response('admin_settings.html', {'error':True}, RequestContext(request))
				else:
					kobe_meta.objects.filter(meta_key = 'blog_name').update(meta_value = blogname)
					kobe_meta.objects.filter(meta_key = 'num_of_pages').update(meta_value = int(numofarticles))
					return render_to_response('admin_settings.html', {'success':True}, RequestContext(request))
	elif action == 'post':
		return render_to_response('admin_post.html', RequestContext(request))
	elif action == 'artmanage':
		return render_to_response('admin_articlemanage.html', RequestContext(request))
	elif action == 'catemanage':
		return render_to_response('admin_catemanage.html', RequestContext(request))


def post(request):
	return render_to_response('admin_post.html', RequestContext(request))