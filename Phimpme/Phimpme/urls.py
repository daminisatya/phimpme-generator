from django.conf.urls import patterns, include, url
from django.contrib import admin
import Phimpme
from Phimpme.apps.usermgt import urls
from Phimpme.apps.orders import urls
from Phimpme.apps.defray import urls
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Phimpme.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'Phimpme.apps.orders.views.home', name='home'),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^cgi-bin/usermgt/', include(Phimpme.apps.usermgt.urls)),
    url(r'^cgi-bin/orders/', include(Phimpme.apps.orders.urls)),
    url(r'^cgi-bin/defray/', include(Phimpme.apps.defray.urls)),
)
