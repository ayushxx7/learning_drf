from django.urls import path, include
from rest_framework import routers
from dj_rest.example import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.regsiter(r'groups', views.GroupViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLS for the browsable API.

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framwork.urls'), namespace='rest_framwork')
]
