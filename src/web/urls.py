from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.simple.redirect_to', {'url': '/home',}),
    (r'^home$', 'web.home.render_home'),
    (r'^register$', 'web.register.render_register'),
    (r'^account$', 'web.account.render_account'),
    (r'^book$', 'web.book.render_book'),
    (r'^login$', 'web.login.render_login')
)
