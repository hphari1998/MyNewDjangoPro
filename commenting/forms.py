from django.forms import ModelForm, CharField, ValidationError

from commenting.models import Comment


class CommitModelFrom(ModelForm):

    class Meta:
        model = Comment
        fields = ['comment', 'article']
    

    def clean_article(self):
        article_id = self.cleaned_data.get('article', None)
        if not article_id:
            raise ValidationError("id is required")
        return article_id
