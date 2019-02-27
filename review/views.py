from django.shortcuts import render, get_object_or_404
from django.views import generic

from review.forms import ReviewForm, CommentForm
from review.models import comment, hindu


def sample(request):
    rev_form = ReviewForm()

    if request.POST:
        rev_form = ReviewForm(request.POST)

    if rev_form.is_valid():
        form1 = rev_form.save()


    context={'form1':rev_form}

    return render(request, "forms.html", context)


def sample1(request,post_id):
    post = get_object_or_404(hindu,pk = post_id)
    all_comment = post.comments.all()
    add_form = CommentForm()
    if request.POST:
        add_form = CommentForm(request.POST)
        if add_form.is_valid():
            form2 = add_form.save(commit=False)
            form2.post = post
            form2.save()
            add_form = CommentForm()

    context = {'form2': add_form,
               "comment":all_comment}
    return render(request, "return.html", context)


class Posts(generic.ListView):
    model = hindu
    template_name = 'list.html'


