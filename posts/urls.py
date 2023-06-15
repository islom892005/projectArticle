from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page
urlpatterns = [
    path('', cache_page(60 * 2)(Main.as_view()), name='main'),
    path('categories/', cache_page(60 * 2)(Categories.as_view()), name='categories'),
    path('add_new_post/', add_new_post, name='add_new_post'),
    path('post/<slug:post_slug>/', cache_page(60 * 2)(Show_post.as_view()), name='post'),
    path('category/<slug:category_slug>/', cache_page(60 * 2)(Category_posts.as_view()), name='category_posts'),
    path('log_in/', LoginUser.as_view(), name='log_in'),
    path('sign_up/', RegisterUser.as_view(), name='sign_up'),
    path('logout/', logout_user, name='logout')
    
]