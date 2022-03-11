from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.welcome, name='welcome'),
    re_path(r'^logout/$', views.logout, name='logout'),
    re_path(r'^jobs/new/$', views.new_job, name='new_job'),
    re_path(r'^dashboard/$', views.dashboard, name='dashboard'),
    re_path(r'^jobs/(?P<id>\d+)/$', views.view_job, name='view_job'),
    re_path(r'^jobs/edit/(?P<id>\d+)/$', views.edit_job, name='edit_job'),
    re_path(r'^dashboard/jobs/remove/$', views.remove_job, name='remove_job'),
    re_path(r'^dashboard/jobs/giveup/$', views.giveup_job, name='giveup_job'),
    re_path(r'^process/signup/$', views.process_signup, name='process_signup'),
    re_path(r'^process/signin/$', views.process_signin, name='process_signin'),
    re_path(r'^jobs/user/add/(?P<id>\d+)/$', views.add_user_job, name='add_user_job'),
    re_path(r'^jobs/giveup/(?P<id>\d+)/$', views.giveup_the_job, name='giveup_the_job'),
    re_path(r'^dashboard/user/jobs/add/$', views.add_job_to_user, name='add_job_to_user'),
    re_path(r'^dashboard/jobs/new/process/$', views.process_new_job, name='process_new_job'),
    re_path(r'^process/jobs/edit/(?P<id>\d+)/$', views.process_job_edit, name='process_job_edit'),
]