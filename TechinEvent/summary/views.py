from .models import summaryModel, CommentModel
from .forms import SearchForm, CommentForm
from django.shortcuts import render, redirect
from django.http import Http404


def summaryListView(request):
    dataset = summaryModel.objects.all()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            summary = summaryModel.objects.get(summary_title=title)
            return redirect(f'/summary/{summary.id}')
    else:
        form = SearchForm()
        context = {
            'dataset': dataset,
            'form': form,
        }
    return render(request, 'summaryapp/listview.html', context)


def summaryDetailView(request, _id):
    try:
        data = summaryModel.objects.get(id=_id)
        comments = CommentModel.objects.filter(summary=data)
    except summaryModel.DoesNotExist:
        raise Http404('Data does not exist')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment = CommentModel(your_name=form.cleaned_data['your_name'],
                                   comment_text=form.cleaned_data['comment_text'],
                                   summary=data)
            Comment.save()
            return redirect(f'/summary/{_id}')
    else:
        form = CommentForm()

    context = {
        'data': data,
        'form': form,
        'comments': comments,
    }
    return render(request, 'summaryapp/detailview.html', context)
