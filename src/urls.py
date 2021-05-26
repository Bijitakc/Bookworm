from django.contrib import admin
from django.urls import path,include
#for non swagger
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
#for swagger
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/',include(("user.urls", "user"),namespace="user")),
    path('api/',include(("api.urls" ,"api"),namespace="api"))
]
#Using core api
# schemapatterns = [
#     path('coreapidocs/',include_docs_urls(title="Bookworm")),
#     path('schema/',get_schema_view(
#         title="Bookworm",
#         description="App for bookworms",
#         version="1.0.0"),
#         name='openapi'
#     )
# ]

schema_view = get_schema_view(
   openapi.Info(
      title="Bookworm",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

schemapatterns = [
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns +=schemapatterns