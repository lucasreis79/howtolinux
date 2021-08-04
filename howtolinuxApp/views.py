from typing import List
from django.views.generic import DetailView, ListView, TemplateView
from .models import Post
from django.db.models import Q

class PostListView(ListView):
    model = Post
    template_name = 'blog.html'
    def get_queryset(self):
        search = self.request.GET.get('search', None)
        if search is not None:
            return Post.objects.filter(Q(distro__icontains=search) | Q(interface__icontains=search) | Q(title__icontains=search))
        else:
            return Post.objects.all()

class PostDetailView(DetailView):
    model = Post
    template_name = 'detailed.html'

class TemplateView(TemplateView):
    template_name = 'index.html'