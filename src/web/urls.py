from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.simple.redirect_to', {'url': '/home',}),
    (r'^home$', 'web.home.render_home'),
    (r'^create_book$', 'web.books.render_create_book'),
    (r'^register$', 'web.register.render_register'),
    (r'^basket/add$', 'web.checkout.render_basket_add'),
    (r'^basket$', 'web.checkout.render_basket'),
    (r'^account$', 'web.account.render_account'),
    (r'^book/(?P<book_isbn>(97(8|9))?\d{9}(\d|X))/image$', 'web.books.render_book_image'),
    (r'^book/(?P<book_isbn>(97(8|9))?\d{9}(\d|X))$', 'web.books.render_book'),
    (r'^login$', 'web.login.render_login'),
    (r'^login/forgotten$', 'web.register.render_forgot_password'),
    (r'^create_book$', 'web.books.render_create_book'),
    (r'^list_book$', 'web.books.render_create_listing'),
    (r'^json/book$', 'web.books.render_book_json'),
    (r'^help$', 'web.help.render_help'),
    (r'^user/logout$', 'web.logout.render_logout'),
    (r'^advsearch$', 'web.search.render_advanced_search'),
    (r'^inbox$', 'web.users.render_inbox'),
    (r'^message/(.*)$', 'web.users.render_message'),
    (r'^listing/(.*)$', 'web.books.render_listing'),
    (r'^user/(.*)$', 'web.users.render_user'),
    (r'^search', 'web.search.render_search'),
    (r'^predict', 'web.search.search_predict')
)

handler403 = "web.errors.permission_denied"
handler404 = "web.errors.page_not_found"
handler500 = "web.errors.server_error"
