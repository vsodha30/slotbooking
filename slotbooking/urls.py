from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework_nested import routers

from authentication import views
from authentication.views import EmployeeViewSet, LoginView, LogoutView
from bookingsystem.views import BookingViewSet, EmployeeBookingsViewSet

router = routers.SimpleRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'book', BookingViewSet)
router.register(r'mybookings', EmployeeBookingsViewSet)

# slotbookersrouter = routers.NestedSimpleRouter(
#     router, r'mybookings', lookup='Employee'     # if works then maybe lookup takes a model name to lookup
# )
# slotbookersrouter.register(r'bookings', EmployeeBookingsViewSet)


urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'slotbooking.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^api/v1/', include(router.urls)),
                       url(r'^api/v1/auth/login/$', LoginView.as_view(), name='login'),
                       url(r'^api/v1/auth/logout/$', LogoutView.as_view(), name='logout'),
                       #url(r'^api/v1/', include(router.urls)),
                       #url(r'^api/v1/', include(slotbooker_router.urls)),
                       url(r'^$', views.index, name='index'),
                       )
