from django.urls import path
from usuarios.views import login_view,  register
from django.contrib.auth import views as LogoutView


urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', register, name='register'),
]
