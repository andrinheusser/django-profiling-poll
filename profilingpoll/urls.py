from django.conf.urls import patterns, url

from .views import poll_list, poll_detail, question, get_email, result


urlpatterns = patterns('',
    url(r'^$', poll_list, name='profilingpoll_poll_list'),
    url(r'^(?P<slug>[\w-]+)/$', poll_detail, name='profilingpoll_poll_detail'),
    url(r'^(?P<poll__slug>[\w-]+)/(?P<id>\d+)/$', question, name='profilingpoll_question'),
    url(r'^(?P<slug>[\w-]+)/finished/$', get_email, name='profilingpoll_get_email'),
    url(r'^result/(?P<hash>[\S^/\?=#]+)/$', result, name='profilingpoll_result'),
)