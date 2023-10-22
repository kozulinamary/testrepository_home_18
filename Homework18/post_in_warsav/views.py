from django.shortcuts import render
from django.views.generic.list import ListView



from .models import Post
def post_view(request):
    context = {}
    context["all_posts"] = Post.objects.all()
    return render(request, "all_posts_func.html", context)


class PostListView(ListView):
    model = Post
    template_name = "all_posts_class.html"
