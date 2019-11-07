from django.forms import ModelForm

from commenting.models import Commentss

class CommitModelFrom(ModelForm):
    class Meta:
        model = Commentss
        fields = ['comment']

