from django.db import models

# Create your models here.
class kobe_admin(models.Model):
	user_email = models.EmailField()
	user_nicename = models.CharField(max_length = 50)
	user_registered = models.DateTimeField(auto_now = True)
	user_pass = models.CharField(max_length = 70)

	def __unicode__(self):
		return user_nicename

admin.site.register(kobe_admin)