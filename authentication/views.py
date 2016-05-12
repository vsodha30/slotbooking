
from rest_framework import permissions, viewsets, status
from rest_framework.response import Response

# maybe some problem with import of Response and status

from authentication.models import Employee
from authentication.permissions import IsEmployeeOwner
from authentication.serializers import EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    #lookup_field = 'id'             #maybe 'username'
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsEmployeeOwner(),)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            Employee.objects.create_user(**serializer.validated_data)

            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

        return Response({
            'status': 'Bad request',
            'message': 'Account could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)


