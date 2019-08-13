from django.views.generic import TemplateView

from blog.models import Post, Comment


class HomePage(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context['post_list'] = Post.objects.all()
        context['comments'] = Comment.objects.all()
        return context
