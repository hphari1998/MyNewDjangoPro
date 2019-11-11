from django.conf.urls import url

from myarticle.views import list_article, view_article, create_article

urlpatterns = [
    url(r'^$', list_article, name='list'),
    url(r'^view/(?P<id>[0-9]+)/$', view_article, name='detail'),
    url(r'^create/$', create_article, name='create'),

]