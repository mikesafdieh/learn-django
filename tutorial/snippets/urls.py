from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from rest_framework.schemas import get_schema_view

from snippets import views
from snippets.views import SnippetViewSet, UserViewSet


##################################
### ViewSet based with routers ###
##################################

# NOTE: This must be created BEFORE we create an instance of the DefaultRouter()!!!
# auto-generated schema view
schema_view = get_schema_view(title='Pastebin API')

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('schema/', schema_view),
]

# NOTE: Default router creates the API root for us, so we don't need the one
# we created anymore


#####################
### ViewSet based ###
#####################

'''
from snippets.views import api_root

# this binds the ViewSet classes we created in views.py into a set of concrete views
snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = format_suffix_patterns([
    path('', api_root),
    path('snippets/', snippet_list, name='snippet-list'),
    path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
    path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail')
])
'''


###################
### Class based ###
###################

'''
urlpatterns = [
	path('', views.api_root),
	path('snippets/', views.SnippetList.as_view(), name='snippet-list'),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
    path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-highlight'),
	path('users/', views.UserList.as_view(), name='user-list'),
	path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
'''


######################
### Function based ###
######################

'''
urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
]
urlpatterns = format_suffix_patterns(urlpatterns)
'''

# for extending our API endpoints to include the content type 
# ex: "http://example.com/api/items/4.json" - ('.json' here is the content type)
