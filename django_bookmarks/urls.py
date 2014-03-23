from django.conf.urls import patterns, include, url

from django.contrib import admin
from bookmarks.views import main_page, user_page
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'django_bookmarks.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', main_page),
    url(r'user/(\w+)/$', user_page),
)
