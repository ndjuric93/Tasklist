from rest_framework import serializers

from tasklist.models import Task

class TaskSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    done_by = serializers.CharField(source='done_by.username', read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'title', 'user', 'description', 'done_by')
