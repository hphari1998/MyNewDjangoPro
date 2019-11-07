from django.shortcuts import render,HttpResponse, HttpResponsePermanentRedirect

from commenting.models import Commentss

from commenting.forms import CommitModelFrom

def listCreate_commit(request):
    comments= Commentss.objects.all().order_by('-created_at')
    if request.method == 'POST':
        comit_form = CommitModelFrom(request.POST, request.FILES)
        if comit_form.is_valid():
            comit_obj= comit_form.save(commit=False)
            comit_obj.author = request.user
            comit_obj.save()
            return HttpResponsePermanentRedirect('/comments/')
    else:
        comit_form = CommitModelFrom()
    return render(request, 'comment/cmnt.html', {'comments':comments, 'form':comit_form})


def edit_commit(request, id):
    comnt= Commentss.objects.get(id=id)
    return render(request, 'comment/edit.html', {'comnt':comnt})

    
    # if request.method == 'POST':
    #     comit_form = CommitModelFrom(request.POST, request.FILES)
    #     print(comit_form)
    #     if comit_form.is_valid():
    #         comit_obj= comit_form.save(commit=False)
    #         comit_obj.author = request.user
    #         comit_obj.save()
    #         return HttpResponsePermanentRedirect('/comments/')
    # else:
    #     comit_form = CommitModelFrom()
    #, 'form':comit_form})
