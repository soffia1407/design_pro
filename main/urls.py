from django.urls import path
from .views import register_view, login_view, home_view, profile_view, create_request_view, delete_request_view, logout_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('create-request/', create_request_view, name='create_request'),
    path('delete-request/<int:request_id>/', delete_request_view, name='delete_request'),
    path('', home_view, name='home'),
]