from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/signup/createprofile', views.create_profile.as_view(), name='create_profile'),
    path('accounts/logout_index', views.logout_index, name='logout_index'),
    path('posts/', views.post_index, name='post_index'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/update/', views.PostUpdate.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDelete.as_view(), name='post_delete'),
    path('post/create/', views.post_create, name='post_create'),
    path('post/form', views.post_form, name='post_form'),
    path('posts/<int:post_id>/like', views.like_post, name='like_post'),
    path('posts/<int:post_id>/like_index', views.like_index, name='like_index'),
    path('posts/<int:post_id>/comment', views.add_comment, name='add_comment'),
    path('posts/<int:post_id>/comment_index', views.comment_index, name='comment_index'),
    path('profile/<int:user_id>/', views.profile, name='profile'),
    path('profile/user/', views.user_profile, name='user_profile'),
    path('follow/<int:user_id>/', views.follow, name='follow'),
    path('posts/following/', views.following_index, name='following_index'),
]