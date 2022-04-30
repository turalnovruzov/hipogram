from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from hipogram.posts.forms import CreatePostForm
from hipogram.tags.models import Tag

from .models import Post


def post_list_view(request):
    posts = Post.objects.all().order_by("-creation_datetime")
    return render(request, "post_list.html", {'posts': posts})

class ListPostsView(ListView):
    template_name = 'post_list.html'
    model = Post
    ordering = '-creation_datetime'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()

        tag_name = self.request.GET.get('tag', None)
        if tag_name is not None:
            queryset = queryset.filter(tags__name=tag_name)
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all() \
                             .annotate(num_posts=Count('posts')) \
                             .order_by('-num_posts')
        return context

class CreatePostView(LoginRequiredMixin, CreateView):
    template_name = 'post_create.html'
    form_class = CreatePostForm
    success_url = reverse_lazy('posts:create')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.save()
        return super().form_valid(form)
