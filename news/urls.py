from django.urls import path
from .views import PostList, PostDetail, PostSearch, PostCreate, PostDelete, PostUpdate, ArticleCreate

urlpatterns = [
   path('', PostList.as_view()),
   path('<int:pk>', PostDetail.as_view()),
   path('posts/search/', PostSearch.as_view()),
   path('posts/create', PostCreate.as_view()),
   path('<int:pk>/edit', PostUpdate.as_view()),
   path('posts/<int:pk>/delete', PostDelete.as_view()),
   path('articles/create/', ArticleCreate.as_view()),

]
