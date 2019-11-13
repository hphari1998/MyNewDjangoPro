from django.conf.urls import url
from signup.views import signupForm

urlpatterns= [
    url(r'$', signupForm, name='signup')
]