# Create your views here.
from browse.models import kobe_posts
from manage.models import kobe_meta
from manage.views import meta, page

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse

def display_all(request):
	page1_lst = page.page(1).object_list
	art_list = []
	for post in page1_lst:
		tmpDic = {}
		tmpDic['id'] = post.id
		tmpDic['title'] = post.post_title
		tmpDic['time'] = post.post_date
		tmpDic['view'] = post.post_view_num
		art_list.append(tmpDic)
	return render_to_response('index.html', dict(meta, **{'art_list':art_list, 'crt_page':1, 'ttl_page':page.num_pages}),RequestContext(request))

def display_time(request):
	return render_to_response('time.html',meta,RequestContext(request))

def display_category(request):
	return render_to_response('category.html',meta,RequestContext(request))

def display_rank(request):
	return render_to_response('rank.html',meta,RequestContext(request))