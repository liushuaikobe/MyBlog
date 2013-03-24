# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

from manage.models import kobe_meta

def manage(request):
	action = request.GET.get('action')
	error = False
	if not action:
		bn_queryset = kobe_meta.objects.filter(meta_key = 'blog_name')
		np_queryset = kobe_meta.objects.filter(meta_key = 'num_of_pages')

		meta = {'blog_name':bn_queryset[0].meta_value,
				'num_of_pages':np_queryset[0].meta_value}

		if request.method == 'GET':
			return render_to_response('admin_settings.html', meta, RequestContext(request))
		else:
			# Check the form data is enough
			if 'blogname' in request.POST and 'numofpages' in request.POST:
				blogname = request.POST['blogname']
				numofpages = request.POST['numofpages']
				# ensure the form data isn't null
				if not blogname or not numofpages:
					meta['error'] = 'The data can not be null.'
					return render_to_response('admin_settings.html', meta, RequestContext(request))
				# ensure the length of blog-name less than 50
				elif len(blogname) > 50:
					meta['error'] = 'The length of the blogname should less then 50.'
					return render_to_response('admin_settings.html', meta, RequestContext(request))
				# post to DB
				else:
					bn_queryset.update(meta_value = blogname)
					np_queryset.update(meta_value = numofpages)
					meta['blog_name'] = blogname
					meta['num_of_pages'] = numofpages
					meta['success'] = True
					return render_to_response('admin_settings.html', meta, RequestContext(request))
			else:
				return render_to_response('admin_settings.html', meta, RequestContext(request))
	elif action == 'post':
		return render_to_response('admin_post.html', RequestContext(request))
	elif action == 'artmanage':
		return render_to_response('admin_articlemanage.html', RequestContext(request))
	elif action == 'catemanage':
		return render_to_response('admin_catemanage.html', RequestContext(request))


def post(request):
	return render_to_response('admin_post.html', RequestContext(request))