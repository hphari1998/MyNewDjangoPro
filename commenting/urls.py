from django.conf.urls import url

from commenting.views import listCreate_commit, edit_commit, del_commit

urlpatterns = [
    url(r'^$', listCreate_commit, name="comit"),
    url(r'^delete/(?P<id>[0-9]+)/$', del_commit, name='delete'),
    url(r'^edit/(?P<id>[0-9]+)/$', edit_commit, name='edits'),
]