from django.db import models
from django.contrib import admin

# Create your models here.
class kobe_admin(models.Model):
	user_email = models.EmailField()
	user_nicename = models.CharField(max_length = 50)
	user_registered = models.DateTimeField(auto_now = True)
	user_pass = models.CharField(max_length = 70)

	def __unicode__(self):
		return self.user_nicename

admin.site.register(kobe_admin)

class kobe_meta(models.Model):
	'''blog_name:To be a tough man'''
	meta_key = models.CharField(max_length = 50)
	meta_value = models.CharField(max_length = 50)

	def __unicode__(self):
		return self.meta_key

admin.site.register(kobe_meta)