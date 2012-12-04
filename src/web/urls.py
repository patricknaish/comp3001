from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.simple.redirect_to', {'url': '/home',}),
    (r'^home$', 'web.home.render_home'),
    (r'^register$', 'web.register.render_register')
)
