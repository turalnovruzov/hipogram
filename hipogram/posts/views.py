from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from hipogram.posts.forms import CreatePostForm

from .models import Post

def post_list_view(request):
    posts = Post.objects.all().order_by("-creation_datetime")
    return render(request, "post_list.html", {'posts': posts})

class ListPostsView(ListView):
    template_name = 'post_list.html'
    queryset = Post.objects.all().order_by("-creation_datetime")
    context_object_name = "posts"
    paginate_by = 2

class CreatePostView(LoginRequiredMixin, CreateView):
    template_name = 'post_create.html'
    form_class = CreatePostForm
    success_url = reverse_lazy('posts:create')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.save()
        return super().form_valid(form)
