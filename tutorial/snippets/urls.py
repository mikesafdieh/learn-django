from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views

### Class based ###

urlpatterns = [
	path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
	path('users/', views.UserList.as_view()),
	path('users/<int:pk>/', views.UserDetail.as_view()),
	path('', views.api_root),
	path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view()),
]


'''
### Function based ###

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
]
'''

# for extending our API endpoints to include the content type 
# ex: "http://example.com/api/items/4.json" - ('.json' here is the content type)
urlpatterns = format_suffix_patterns(urlpatterns)