# -*- coding: cp936 -*-
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponse

from manage.models import kobe_meta
from manage.forms import ImgForm
from browse.models import kobe_category, kobe_type, kobe_posts

import ImageFile

# get the meta data of blog
bn_queryset = kobe_meta.objects.filter(meta_key = 'blog_name')
np_queryset = kobe_meta.objects.filter(meta_key = 'num_of_pages')
meta = {'blog_name':bn_queryset[0].meta_value, 'num_of_pages':np_queryset[0].meta_value}

# common settings
def settings(request):
	global meta
	if request.method == 'GET':
		return render_to_response('admin_settings.html', meta, RequestContext(request))
	else:
		# Check the form data is enough
		if 'blogname' in request.POST and 'numofpages' in request.POST:
			blogname = request.POST['blogname']
			numofpages = request.POST['numofpages']
			# ensure the form data isn't null
			if not blogname.strip() or not numofpages.strip():
				return render_to_response('admin_settings.html', dict(meta, **{'error':'The data can not be null.'}), RequestContext(request))
			# ensure the length of blog-name less than 50
			elif len(blogname) > 50:
				return render_to_response('admin_settings.html', dict(meta, **{'error':'The length of the blogname should less then 50.'}), RequestContext(request))
			# post to DB
			else:
				bn_queryset.update(meta_value = blogname)
				np_queryset.update(meta_value = numofpages)
				meta['blog_name'] = blogname
				meta['num_of_pages'] = numofpages
				return render_to_response('admin_settings.html', dict(meta, **{'success':True}), RequestContext(request))
		else:
			return render_to_response('admin_settings.html', meta, RequestContext(request))

# post new articles
def post(request):
	global meta
	cate_list = kobe_category.objects.all()
	type_list = kobe_type.objects.all()
	if request.method == 'POST':
		if 'articlename' in request.POST and 'articletype' in request.POST and 'articlecate' in request.POST and 'blogeditor' in request.POST:
			articlename = request.POST['articlename']
			articletype = request.POST['articletype']
			articlecate = request.POST['articlecate']
			article = request.POST['blogeditor']
			if articlename and articletype and articlecate and article:
				post = kobe_posts(post_title=articlename, post_view_num=0, post_content=article)
				post.post_type = kobe_type.objects.filter(type_name=articletype)[0]

				current_cate = kobe_category.objects.filter(cate_name=articlecate)
				current_cate.update(cate_art_num = (int(current_cate[0].cate_art_num) + 1))

				post.post_cate = current_cate[0]

				post.save()
	return render_to_response('admin_post.html', dict(meta, **{'category_list':cate_list, 'type_list':type_list}), RequestContext(request))

# article management
def artmanage(request):
	post_list = kobe_posts.objects.all()
	tmpList = []
	for post in post_list:
		tmpDic = {}
		tmpDic['no'] = post.id
		tmpDic['title'] = post.post_title
		tmpDic['time'] = post.post_date
		tmpDic['viewnum'] = post.post_view_num
		tmpList.append(tmpDic)
	# print tmpList
	return render_to_response('admin_articlemanage.html', dict(meta, **{'post_list':tmpList}), RequestContext(request))

# category management
def catemanage(request):
	global meta
	cate_list = kobe_category.objects.all()
	category_list = []
	for cate in cate_list:
		cate_meta = {}
		cate_meta['no'] = cate.id
		cate_meta['name'] = cate.cate_name
		cate_meta['art_num'] = cate.cate_art_num
		category_list.append(cate_meta)
	return render_to_response('admin_catemanage.html', dict(meta, **{'category_list':category_list, 'next_no':''}), RequestContext(request))


def editpost(request, post_id):
	global meta
	current_post = kobe_posts.objects.get(id = int(post_id))
	tmpDic = {}
	tmpDic['title'] = current_post.post_title
	tmpDic['type'] = current_post.post_type.type_name
	tmpDic['cate'] = current_post.post_cate.cate_name

	cate_list = kobe_category.objects.all()
	type_list = kobe_type.objects.all()

	tmpDic['content'] = current_post.post_content
	return render_to_response('admin_post.html', dict(meta, **{'default':tmpDic, 'category_list':cate_list, 'type_list':type_list}), RequestContext(request))

#-------------------------------------------#
# Handle Ajax Requests                      #  
#-------------------------------------------#
# Handle Ajax admin category
def ajax_modify_category(request):
	if 'cate_id' in request.POST and 'new_cate_name' in request.POST:
		try:		
			kobe_category.objects.filter(id = request.POST['cate_id']).update(cate_name = request.POST['new_cate_name'])
		except Exception,e:
			print e
			return HttpResponse('error')
		return HttpResponse('success')
	else:
		return HttpResponse('error')

def ajax_del_category(request):
	if 'cate_id' in request.POST:
		try :
			kobe_category.objects.get(id = request.POST['cate_id']).delete()
		except Exception,e:
			print e
			return HttpResponse('error')
		return HttpResponse('success')
	else:
		return HttpResponse('error')

def ajax_add_category(request):
	if 'new_cate_name' in request.POST:
		try:
			new_cate = kobe_category(cate_name = request.POST['new_cate_name'], cate_art_num = 0)
			new_cate.save()
		except Exception,e:
			print e
			return HttpResponse('error')
		return HttpResponse('success')
	else:
		return HttpResponse('error')

def ajax_del_post(request):
	if 'post_id' in request.POST:
		try:
			kobe_posts.objects.get(id = request.POST['post_id']).delete()
		except Exception,e:
			print e
			return HttpResponse('error')
		return HttpResponse('success')
	else:
		return HttpResponse('error')