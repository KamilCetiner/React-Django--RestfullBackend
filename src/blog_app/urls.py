from django.urls import path 
from .views import post_list,post_create, post_get_update_delete

urlpatterns = [
    
    path('list/',post_list,name='list'),
    path('create/',post_create,name='create'),
    path('<int:id>/detail/',post_get_update_delete,name='detail')

]