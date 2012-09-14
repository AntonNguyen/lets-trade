from django.conf.urls import patterns, include, url
from api.api import UserResource

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

user_resource = UserResource()

urlpatterns = patterns('',
	url(r'^api/', include(user_resource.urls)),
    # Examples:
    # url(r'^$', 'lets_trade.views.home', name='home'),
    # url(r'^lets_trade/', include('lets_trade.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
