from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.simple.redirect_to', {'url': '/home',}),
    (r'^home$', 'web.home.render_home'),
    (r'^account$', 'web.account.render_account_test'),
    (r'^book$', 'web.book.render_book'),
    (r'^login$', 'web.login.render_login'),
    (r'^register$', 'web.register.render_register')
)
