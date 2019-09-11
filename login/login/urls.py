
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/logout', auth_views.LogoutView.as_view(template_name = 'userlogin.html') , name="logut"),
    path('', include("blog.urls")),
]
