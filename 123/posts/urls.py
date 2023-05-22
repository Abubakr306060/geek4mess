from django.urls import path
from posts import views

urlpatterns = [
    # path("", views.get_index, name="index-page"),
    path("", views.IndexView.as_view(), name="index-page"),
    path("contacts/", views.get_contacts, name="contacts-page"),
    path("about/", views.get_about, name="about-page"),
    # path("posts/<int:pk>", views.get_post, name="post-detail"),
    path("posts/<int:pk>", views.PostDetailView.as_view(), name="post-detail"),
    path("posts/update/<int:pk>", views.update_post, name="post-update"),
    path("posts/delete/<int:pk>", views.delete_post, name="post-delete"),
    path("post/create/", views.PostCreateView.as_view(), name="post-create"),
    path("post/delete/<int:pk>", views.PostDeleteView.as_view(), name="post-delete"),
    path("post/update/<int:pk>", views.PostUpdateView.as_view(), name="post-update"),
]