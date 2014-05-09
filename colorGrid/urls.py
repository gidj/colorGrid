from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'colorGrid.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'colorGrid.views.index'),
    url(r'^grid/', 'colorGrid.views.grid'),
)
