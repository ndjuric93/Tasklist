from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import permissions

from tasklist.models import Task
from tasklist.serializers import TaskSerializer

from tasklist.permissions import IsOwnerOrReadOnly

class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsOwnerOrReadOnly, permissions.IsAuthenticated)

    def perform_create(self, serializer):
        serializer.validated_data['user_id'] = self.request.user.id
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        """
        PATCH function marks done_by foreign key by user that did it.
        """
        task = Task.objects.get(pk=kwargs['pk'])
        task.done_by = self.request.user
        task.save()
        return Response(TaskSerializer(task).data)
