from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/signup/createprofile', views.create_profile.as_view(), name='create_profile'),
    path('post/<int:post_id>/add_photo/', views.add_photo, name='add_photo'),
    path('posts/', views.post_index, name='post_index'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/create/', views.PostCreate.as_view(), name='post_create'),
    path('post/<int:pk>/update/', views.PostUpdate.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDelete.as_view(), name='post_delete'),
    # path('posts/<int:post_id>/like', views.like_post, name='like_post'),
    path('posts/<int:post_id>/comment', views.add_comment, name='add_comment'),

]