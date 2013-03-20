# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

def manage(request):
	action = request.GET.get('action')
	if not action:
		return render_to_response('admin_settings.html',context_instance = RequestContext(request))
	elif action == 'post':
		return render_to_response('admin_post.html', context_instance = RequestContext(request))


def post(request):
	return render_to_response('admin_post.html',context_instance = RequestContext(request))