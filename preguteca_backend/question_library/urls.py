from django.urls import include, path
from . import views

app_name = "question_library"

urlpatterns = [
    path("", views.category_list, name="category list"),
    path(
        "category/<str:category_name>", views.category_details, name="category_details"
    ),
]
