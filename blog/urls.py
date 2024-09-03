from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.PostListView.as_view(), name='blog-home'),
    path("about/", views.about, name="blog-about"),
    path("contactus/", views.contactUs, name="blog-contact"),
    path("post/<int:pk>/", views.PostDetailView.as_view(), name="post-detail")
]