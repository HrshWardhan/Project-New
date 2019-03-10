from django.conf.urls import url
from .import views
from django.contrib.auth.views import login,logout,password_reset,password_reset_done

urlpatterns = [
    url(r'^login/$', login, {'template_name':'accounts/login.html'}),
    url(r'^register/$', views.register, name='register'),
    url(r'^accounts/profile/$', views.profile, name='profile' ),
    url(r'^accounts/profile/edit/$', views.profileedit, name='profileedit' ),
    url(r'^accounts/profile/password/$', views.changepassword, name='change_password'),
    url(r'^accounts/logout/$',logout,{'template_name':'accounts/logout.html'})
]