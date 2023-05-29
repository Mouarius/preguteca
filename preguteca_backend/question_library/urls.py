from django.urls import include, path
from rest_framework import routers

from . import views

app_name = "question_library"

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path("", views.category_list, name="category list"),
    path('', include(router.urls)),
    path(
        "category/<str:category_name>", views.category_details, name="category_details"
    ),
    path('api-auth/', include('rest_framework.urls', namespace="rest_framework"))
]
