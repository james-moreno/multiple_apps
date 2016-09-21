from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = "index"),
    url(r'^add$', views.add_course, name = "add_course"),
    url(r'^remove/(?P<id>\d+)', views.remove, name = "remove"),
    url(r'^remove_confirm$', views.remove_confirm, name ="remove_confirm"),
    url(r'^keep$', views.keep, name="keep"),
    url(r'^users_courses$', views.users_courses_index, name = "users_courses_index"),
    url(r'^users_courses_add$', views.users_courses_add, name = "users_courses_add")
]
