# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse

from forms import ImgForm

import ImageFile,time,os

def uploadframe(request):
	data = {'form':ImgForm()}
	if request.method == 'POST':
		form = ImgForm(request.POST, request.FILES)
		if form.is_valid():
			f = request.FILES["imagefile"]

			img_path = 'static/uploads_imgs/'
			img_name = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time())) + '.' +f.name.split('.')[-1:][0]

			parser = ImageFile.Parser()
			for chunk in f.chunks():  
				parser.feed(chunk)  
			img = parser.close()
			img.save(img_path + img_name)
			data['path'] = 'http://' + request.get_host() + '/' + img_path + img_name
	return render_to_response('uploadframe.html', data, RequestContext(request))

def ajax_del_img(request):
	if 'img_id' in request.POST:
		try:
			os.remove('static/uploads_imgs/' + request.POST['img_id'])
		except Exception, e:
			print e
			return HttpResponse('error')
		return HttpResponse('success')
	return HttpResponse('error')
