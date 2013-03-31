from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

from browse.views import display_archive
from manage.views import settings, post, artmanage, catemanage
from manage.views import ajax_modify_category, ajax_del_category, ajax_add_category
from upload.views import uploadframe, ajax_del_img

urlpatterns = patterns('',
    # manage pages index
    url(r'^manage/settings/$', settings),
    url(r'^manage/post/$', post),
    url(r'^manage/artmanage/$', artmanage),
    url(r'^manage/catemanage/$', catemanage),
    # ajax urls
    url(r'^manage/catemanage/modifycate/', ajax_modify_category),
    url(r'^manage/catemanage/delcate/', ajax_del_category),
    url(r'^manage/catemanage/addcate/', ajax_add_category),
    url(r'^manage/post/uploadframe/$', uploadframe),
    url(r'^manage/post/delimg/$', ajax_del_img),
    # built-in admin
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)