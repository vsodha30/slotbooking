from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers

from authentication.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    confirm_password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Employee
        fields = ('id', 'email', 'username', 'created_at', 'updated_at',
                  'first_name', 'last_name', 'role', 'password', 'confirm_password',)

        read_only_fields = ('created_at', 'updated_at',)

        def create(self, validated_data):
            return Employee.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.username = validated_data.get('username', instance.username)
            instance.role = validated_data.get('role', instance.role)
            #  If these keys are present in the arrays dictionary, we will use the new value.
            # Otherwise, the current value of the instance object is used. Here, instance is of type Account.


            instance.save()

            password = validated_data.get('password',validated_data, None)
            confirm_password = validated_data.get('confirm_password', None)
            # Here None because we donot take password always it is not necessary
            # But whenever comes in form of Json you need to update it
            # Don't have to set to previous value of instance when no value i.e instance.password

            if password and confirm_password and password == confirm_password:
                instance.set_password(password)
                instance.save()

            update_session_auth_hash(self.context.get('request'), instance)
            #When a user's password is updated, their session authentication hash must be explicitly updated.
            # If we don't do this here, the user will not be authenticated on their next request and will have to log in again.
            # This is becoz session will have old password while user will be sending new password with each request


            return instance






