from rest_framework import serializers

from authentication.serializers import EmployeeSerializer
from bookingsystem.models import Booking


class BookingSerializer(serializers.ModelSerializer):
    booker_of_slot = EmployeeSerializer(read_only=True)            # this is used when we want the all the fields of employee described in employeeserializer

    class Meta:
        model = Booking
        fields = ('id', 'room_booked', 'start_date', 'end_date', 'booker_of_slot',)
        read_only_fields = ('id')

