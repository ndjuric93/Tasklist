from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from tasklist.models import Task
from tasklist.serializers import TaskSerializer

class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    # def create(self, request, *args, **kwargs):
    def perform_create(self, serializer):
        print('#####')
        print(self.request.user.id)
        print('#####')
        serializer.user = self.request.user.id
        serializer.save()

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        task = Task.objects.get(pk=kwargs['pk'])
        task.done = True
        task.save()
        return Response(TaskSerializer(task).data)
