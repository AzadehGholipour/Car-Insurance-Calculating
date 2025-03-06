from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("form/", views.form, name="form"),
    path("save_application", views.save_application, name="save_application"),
    path("profile/<int:user_id>/", views.profile, name="profile"),
    path("post/", views.upload_post, name="upload_post"),
    path("check-auth-status/", views.check_auth_status, name="check_auth_status"),
    path("posts/", views.posts, name="posts")
]