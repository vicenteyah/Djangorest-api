from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = (
            'id', 
            'title', 
            'comment', 
            'created_at', 
            'updated_at'
        )
        extra_kwargs = {
            "title": {"required": False, "allow_blank": True},
            "comment": {"required": False, "allow_blank": True},
        }

