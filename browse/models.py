from django.db import models
from django.contrib import admin

# Create your models here.
class kobe_posts(models.Model):
	post_title = models.CharField(max_length = 200)
	post_date = models.DateTimeField(auto_now = True)
	post_view_num = models.IntegerField()
	post_content = models.TextField()
	post_type = models.ForeignKey('kobe_type')
	post_cate = models.ForeignKey('kobe_category')

	def __unicode__(self):
		return self.post_title

admin.site.register(kobe_posts)

class kobe_type(models.Model):
	'''translate,reserved,Original'''
	type_name = models.CharField(max_length = 100)

	def __unicode__(self):
		return self.type_name

admin.site.register(kobe_type)

class kobe_category(models.Model):
	'''C++,Python,Java'''
	cate_name = models.CharField(max_length = 100)
	cate_art_num = models.IntegerField()

	def __unicode__(self):
		return self.cate_name

admin.site.register(kobe_category)