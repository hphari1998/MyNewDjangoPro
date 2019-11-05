from django.conf.urls import url

from myarticle.views import list_article

urlpatterns = [
    url(r'^$', list_article),
]