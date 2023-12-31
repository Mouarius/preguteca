from django.urls import path, include

from . import views

app_name = "question_library"

urlpatterns = [
    path(
        "api/",
        include(
            [
                path("home_page/", views.HomePageView.as_view()),
                path("categories/<str:name>", views.CategoryDetail.as_view()),
                path("categories/", views.CategoryList.as_view()),
                path("video_entries/<int:pk>", views.VideoEntryDetail.as_view()),
                path("video_entries/", views.VideoEntryList.as_view()),
                path("video_posts/", views.VideoPostList.as_view()),
                path("text_posts/", views.TextPostList.as_view()),
                path("pages/", views.MenuPageList.as_view())
            ]
        ),
    ),
    path("", views.DefaultView.as_view()),
]
