from django.urls import path
from .views import PostList, PostDetail, PostSearch, PostCreate, PostDelete, PostUpdate, ArticleCreate

urlpatterns = [
   path('', PostList.as_view(), name='post_list'),
   path('<int:pk>', PostDetail.as_view(),name='post_detail'),
   path('post/search/', PostSearch.as_view(), name="post_search"),
   path('post/create', PostCreate.as_view(), name="post_create"),
   path('<int:pk>/edit', PostUpdate.as_view(), name='post_update'),
   path('post/<int:pk>/delete', PostDelete.as_view(), name="post_delete"),
   path('articles/create/', ArticleCreate.as_view(), name="article_create"),

]
