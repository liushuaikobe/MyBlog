# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse

from manage.models import kobe_meta
from browse.models import kobe_category

from manage.forms import ImgForm

import ImageFile

def manage(request):
	tab = request.GET.get('tab')
	# get the meta data of blog
	bn_queryset = kobe_meta.objects.filter(meta_key = 'blog_name')
	np_queryset = kobe_meta.objects.filter(meta_key = 'num_of_pages')
	meta = {'blog_name':bn_queryset[0].meta_value,
			'num_of_pages':np_queryset[0].meta_value}
	# judge which tab is required
	# common settings
	if not tab:
		if request.method == 'GET':
			return render_to_response('admin_settings.html', meta, RequestContext(request))
		else:
			# Check the form data is enough
			if 'blogname' in request.POST and 'numofpages' in request.POST:
				blogname = request.POST['blogname']
				numofpages = request.POST['numofpages']
				# ensure the form data isn't null
				if not blogname.strip() or not numofpages.strip():
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

	# post new articles
	elif tab == 'post':
		return render_to_response('admin_post.html', RequestContext(request))

	# article management
	elif tab == 'artmanage':
		return render_to_response('admin_articlemanage.html', RequestContext(request))

	# category management
	elif tab == 'catemanage':
		cate_list = kobe_category.objects.all()
		meta['category_list'] = []
		for cate in cate_list:
			cate_meta = {}
			cate_meta['no'] = cate.id
			cate_meta['name'] = cate.cate_name
			cate_meta['art_num'] = cate.cate_art_num
			meta['category_list'].append(cate_meta)
		# meta['next_no'] = max([cate.id for cate in cate_list]) + 1
		meta['next_no'] = ''
		return render_to_response('admin_catemanage.html', meta, RequestContext(request))

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
			return HttpResponse("error")
		return HttpResponse("success")
	else:
		return HttpResponse("error")

def receive_img(request):
	if request.method = 'POST':
		form = ImgForm(request.POST, request.FILES)
		if form.is_valid():
			f = request.FILES["imagefile"]
			parser = ImageFile.Parser()  
            for chunk in f.chunks():  
                parser.feed(chunk)  
            img = parser.close()  
            img.save("")  



