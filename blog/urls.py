from django.conf.urls import include, url
from django.contrib import admin
from core import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
    url(r'(?P<article_id>\d+)/$', views.article, name='article'),
    url(r'^admin/', include(admin.site.urls)),
]
