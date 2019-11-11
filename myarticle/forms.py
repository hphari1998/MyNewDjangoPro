from django.forms import ModelForm, CharField

from pagedown.widgets import AdminPagedownWidget

from myarticle.models import Article

from commenting.models import Comment

class ArticleModelForm(ModelForm):
    content = CharField(widget=AdminPagedownWidget())
    class Meta:
        model = Article
        fields = ['title', 'thumbnail', 'content']

class ArticleComment(ModelForm):
    class Meta:
        model = Comment
        fields = ['article','comment']
