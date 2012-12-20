from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.simple.redirect_to', {'url': '/home',}),
    (r'^home$', 'web.home.render_home'),
    (r'^create_book$', 'web.books.render_create_book'),
    (r'^register$', 'web.register.render_register'),
    (r'^basket$', 'web.checkout.render_basket'),
    (r'^account$', 'web.account.render_account'),
    (r'^book$', 'web.book.render_book'),
    (r'^login$', 'web.login.render_login'),
    (r'^create_book$', 'web.books.render_create_book')
)
