from django.shortcuts import render, HttpResponse, HttpResponsePermanentRedirect

from commenting.models import Comment

from commenting.forms import CommitModelFrom

def listCreate_commit(request):
    if request.method == 'POST':
        comit_form = CommitModelFrom(request.POST, request.FILES)
        if comit_form.is_valid():
            comit_obj= comit_form.save(commit=False)
            comit_obj.author = request.user
            comit_obj.save()
            return HttpResponsePermanentRedirect('/articles/view/{}/'.format(
                comit_obj.article.id
            ))
    return HttpResponsePermanentRedirect(request, '/articles/', )


def edit_commit(request, id):
    comnt= Comment.objects.get(id=id)
    if request.method == 'POST':
        form = CommitModelFrom(request.POST)
        if form.is_valid():
            comnt.comment = form.cleaned_data['comment']
            comnt.save()
            return HttpResponsePermanentRedirect('/articles/view/{}/'.format(
                comnt.article.id
            ))
    comit_form = CommitModelFrom(instance=comnt)
    return render(request, 'comment/edit.html', {'form':comit_form})

def del_commit(request, aid):
    comnt = Comment.objects.get(id=aid)
    comnt.delete()
    return HttpResponsePermanentRedirect('/comments/')

