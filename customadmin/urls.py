from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from customadmin import views

app_name = "customadmin"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("create-user/", views.create_user, name='create-user'),
    path("create-item/", views.create_item, name='create-item'),
    path("delete-object/<int:id>/<str:object_type>", views.delete_object, name='delete-object'),
    path("edit-object/<int:id>/<str:object_type>", views.edit_object, name='edit-object'),
]
