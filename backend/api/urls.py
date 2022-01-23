from django.urls import path, include
from api import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
  path('', views.api_root),
  path('messages/', views.MessageList.as_view(), name='message-list'),
  path('messages/<int:pk>/', views.MessageDetail.as_view(), name='message-detail'),
  path('users/', views.UserList.as_view(), name='user-list'),
  path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
  path('users/login/', obtain_auth_token, name='login')
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
  path('api-auth/', include('rest_framework.urls')),
]