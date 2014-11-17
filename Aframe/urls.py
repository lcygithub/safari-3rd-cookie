from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'Aframe.views.dianpu', name='home'),
    url(r'^sync_cookie/$', 'Aframe.views.cookie', name="cookie"),
    url(r'^set-cookie/$', 'Aframe.views.set_cookie', name="set_cookie"),
    url(r'^index/$', 'Aframe.views.index', name='index'),
    url(r'^window_open/$', 'Aframe.views.window_open', name='window_open'),
    url(r'^open_cookie/$', 'Aframe.views.open_cookie', name='open_cookie'),
    url(r'^dialog/$', 'Aframe.views.dialog', name='dialog')

    # url(r'^Aframe/', include('Aframe.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
