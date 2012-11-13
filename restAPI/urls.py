from django.conf.urls.defaults import *
from tastypie.api import Api
from main.api import EntryResource, UserResource
from django.contrib import admin

admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(EntryResource())


urlpatterns = patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'app/login.html'}),
    url(r'^logout/$', 'main.views.logout_view'),
    (r'^admin/', include(admin.site.urls)),
    (r'^api/', include(v1_api.urls)),
)