from django.contrib import admin

from django.urls import path , include
from rest_framework import routers
from notes.views import NoteViewSet

notes_router = routers.SimpleRouter()
notes_router.register(
    r'notes', 
    NoteViewSet,
    basename='notes'
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include(notes_router.urls)),
]

