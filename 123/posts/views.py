from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy

from posts.models import Post, Comment
from django.views import generic
from posts.forms import CommentForm


# CRUD - Create Retrieve Update Delete
# Class retrieve list
class IndexView(generic.ListView):
    # model = Post
    queryset = Post.objects.filter(status=True)
    template_name = "posts/index.html"
    context_object_name = "posts"


# Class retrieve detail
class PostDetailView(generic.DetailView):
    model = Post
    context_object_name = "post"
    template_name = "posts/post_detail.html"

    # extra_context = {"form": CommentForm()}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            pre_saved_comment = form.save(commit=False)
            pre_saved_comment.post = post
            pre_saved_comment.save()
        return redirect("post-detail", pk)


    # def post(self, request, pk):
    #     post = Post.objects.get(pk=pk)
    #     username = request.POST.get("username")
    #     text = request.POST.get("comment_text")
    #     if username and text:
    #         comment = Comment.objects.create(username=username, text=text, post=post)
    #         comment.save()
    #     return redirect("post-detail", pk)


# Class Create operation
class PostCreateView(generic.CreateView):
    model = Post
    template_name = "posts/post_create.html"
    fields = ["title", "content", "category"]
    success_url = reverse_lazy("index-page")


# Class Delete operation
class PostDeleteView(generic.DeleteView):
    model = Post
    success_url = reverse_lazy("index-page")


# Class Update operation
class PostUpdateView(generic.UpdateView):
    model = Post
    template_name = "posts/update_post.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("index-page")


# Functional Create operation
def create_post(request):
    if request.method == "GET":
        return render(request, "posts/post_create.html")
    elif request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        category = request.POST.get("category")
        post = Post.objects.create(title=title, content=content, category=category)
        post.save()
        return reverse_lazy("index-page")


# CRUD - Retrieve
def get_index(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "posts/index.html", context=context)


def get_post(request, pk):
    # post = Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)
    return render(request, "posts/post_detail.html", {"post": post})


def update_post(request, pk):
    return render(request, "posts/update_post.html")


def delete_post(request, pk):
    return render(request, "posts/delete_post.html")


def get_contacts(request):
    context = {"title": "Контакты"}
    return render(request, "posts/contacts.html", context=context)


def get_about(request):
    context = {"title": "О нас"}
    return render(request, "posts/about.html", context=context)
