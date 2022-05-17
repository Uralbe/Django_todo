from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from todo.views import TodoViewSet

todo_rauter=DefaultRouter()
todo_rauter.register("todo", TodoViewSet, "todo")

urlpatterns=[
    path("", include(todo_rauter.urls)),
    path('auth/', obtain_auth_token),
]