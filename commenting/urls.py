from django.conf.urls import url

from commenting.views import listCreate_commit,edit_commit

urlpatterns = [
    url(r'^$', listCreate_commit, name="comit"),
    url(r'^(?P<id>[0-9])/edit/$', edit_commit, name='edits'),
]