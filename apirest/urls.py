from django.contrib import admin

from django.urls import path , include 
from rest_framework import routers, permissions
from notes.views import NoteViewSet
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)



schema_view = get_schema_view(
    openapi.Info(
        title="Notes API rest",
        default_version='v1',
        description="Test description",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

notes_router = routers.SimpleRouter()
notes_router.register(
    r'notes', 
    NoteViewSet,
    basename='notes'
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("api/token/", TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("", include("notes.urls")),
]

