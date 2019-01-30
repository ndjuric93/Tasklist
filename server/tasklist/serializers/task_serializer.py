from rest_framework import serializers

from tasklist.models import Task

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'done_by')
