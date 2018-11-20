from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers

from tutorial.quickstart import views


######################
### For quickstart ###
######################

'''
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
'''


####################
### For snippets ###
####################

urlpatterns = [
	path('api-auth/', include('rest_framework.urls')), # for user auth
	# NOTE: we can name the url whatever we want - it's the `include('rest_framework.urls')` that
	# gives us all the auth features (such as login/logout) out of the box.

    path('', include('snippets.urls')),
]