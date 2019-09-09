from django.conf.urls import url, include
from user_managment.views import *

urlpatterns = [
    url(r'^get_user_by_id/(?P<id>\d+)/$', get_user_by_id),
    url(r'^get_users_by_name', find_users_by_name),
    url(r'^add_user', add_user),
    url(r'^edit_user', edit_users),
    url(r'^edit_contact_info', edit_contact_info),
    url(r'^add_contact_info', add_additional_contact_info),
    url(r'^delete_user/(?P<id>\d+)/$', delete_user),
    ]