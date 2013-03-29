from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

from browse.views import display_archive
from manage.views import manage
from manage.views import ajax_modify_category, ajax_del_category, ajax_add_category
from upload.views import uploadframe, ajax_del_img

urlpatterns = patterns('',
    # Examples:
    url(r'^$', manage),
    url(r'^modifycate/', ajax_modify_category),
    url(r'^delcate/', ajax_del_category),
    url(r'^addcate/', ajax_add_category),
    url(r'^uploadframe/$', uploadframe),
    url(r'^delimg/$', ajax_del_img),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
