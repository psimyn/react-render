from django.conf.urls import patterns, url

urlpatterns = patterns('example_app.views',
    url(r'^$', 'index', name='index'),
    url(r'^\?no-js$', 'index', name='index-no-js'),
    url(r'^comment/$', 'comment', name='comment'),
)
