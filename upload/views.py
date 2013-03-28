# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse

from forms import ImgForm

import ImageFile,time

def uploadframe(request):
	form = ImgForm()
	return render_to_response('uploadframe.html', {'form':form},RequestContext(request))


def receive_img(request):
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

			return HttpResponse('http://' + request.get_host() + '/' + img_path + img_name)
