from django.conf.urls import url
from signin.views import signinForm

urlpatterns= [
    url(r'$', signinForm, name='signin')
]