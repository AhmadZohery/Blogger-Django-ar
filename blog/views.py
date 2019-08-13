from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from .forms import NewComment

from blog.models import Post


class ListPosts(ListView):
    model = Post


class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['commentform'] = NewComment
        return context

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = NewComment(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.post = post
            obj.author = self.request.user
            obj.save()
            return redirect('blog:post_detail', post.pk)


