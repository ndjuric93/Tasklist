from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from rest_framework import mixins, viewsets
from rest_framework.response import Response

class LoginViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        print(user)
        if user is not None:
            print(user)
            if user.is_active:
                login(request, user)
                return Response('Success')
        return Response('Not success')
