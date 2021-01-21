from django.urls import path
from .views import post_list_create, post_get_update_delete


app_name = "blog_app"
urlpatterns = [
    path("list/", post_list_create, name="list"),
    path("<int:id>/detail/", post_get_update_delete, name="detail"),
]
