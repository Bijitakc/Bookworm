from django.contrib import admin
from django.urls import path,include
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/',include(("user.urls", "user"),namespace="user")),
    path('api/',include(("api.urls" ,"api"),namespace="api"))
]

schemapatterns = [
    path('schema/',get_schema_view(
        title="Bookworm",
        description="App for bookworms",
        version="1.0.0"),
        name='openapi'
    )
]

urlpatterns +=schemapatterns