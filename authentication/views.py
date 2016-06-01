from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from rest_framework import permissions, viewsets, status, views
from rest_framework.response import Response
import json
# maybe some problem with import of Response and status

from authentication.models import Employee
from authentication.permissions import IsEmployeeOwner
from authentication.serializers import EmployeeSerializer


def index(request):
    return render(request, 'index.html')

class EmployeeViewSet(viewsets.ModelViewSet):
    #lookup_field = 'id'             #maybe 'username'
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get_permissions(self):
        # if self.request.method in permissions.SAFE_METHODS:          # I think u can only get all employees list when u are admin .... so later change the permission to IsAdmin
        #     return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        # return (permissions.IsAuthenticated(), IsEmployeeOwner(),)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=True):
            Employee.objects.create_user(**serializer.validated_data)

            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)


class LoginView(views.APIView):
    def post(self, request, format=None):
        data = json.loads(request.body)

        employeename = data.get('username', None)               # get username from data that came from front-end
        password = data.get('password', None)

        employee = authenticate(username=employeename, password=password)
        # keep attention as it was causing problem becoz USERNAME_FIELD was "email" in models and
        # here for authentication u r giving "username"

        if employee is not None:
            if employee.is_active:
                login(request, employee)
                serialized = EmployeeSerializer(employee)
                return Response(serialized.data)
            # else:
            #     return Response({
            #         'status': 'Unauthorized',
            #         'message': 'This account has been disabled.'
            #     }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({
                'status': 'Unauthorized',
                'message': 'Username or Password Incorrect'
            },status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        logout(request)

        return Response({}, status=status.HTTP_204_NO_CONTENT)







