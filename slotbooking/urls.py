from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework_nested import routers

from authentication import views
from authentication.views import EmployeeViewSet

router = routers.SimpleRouter()
router.register(r'employees', EmployeeViewSet)


urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'slotbooking.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^api/v1/', include(router.urls)),
                       #url(r'^$', views.register, name='register'),

                       url(r'^$', views.index, name='index'),
                       )
