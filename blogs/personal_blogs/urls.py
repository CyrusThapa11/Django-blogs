from django.urls import path
from . import views

urlpatterns = [
    # path("",views.index,name="starting-page"),
    # path("", views.StartingPageView.as_view(), name="starting-page"),
    # path("posts",views.posts,name="posts"),
    # path("posts", views.AllPostView.as_view(), name="posts"),
    # path("posts/<slug:slug>",views.post_detail,name="post-detail")
    # path("posts/<slug:slug>", views.SinglePostView.as_view(),
    #      name="post-detail-page"),
    # path("read-later", views.ReadLaterView.as_view(), name="read-later")


    # path("", views.starting_page, name="starting-page"),
    # path("posts", views.posts, name="posts"),
    # path("posts/<slug:slug>", views.post_detail, name="post-detail"),

    path("", views.StartingPageView.as_view(), name="starting-page"),
    path("posts", views.AllPostsView.as_view(), name="posts-page"),
    path("posts/read-later", views.ReadLaterView.as_view(), name="read-later"),
    path("posts/<slug:slug>", views.SinglePostView.as_view(),
         name="post-detail"),  # /posts/my-first-post

]
