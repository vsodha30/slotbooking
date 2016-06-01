from datetime import date, datetime, timedelta
from rest_framework import permissions, viewsets
from rest_framework.response import Response

from bookingsystem.models import Booking
from bookingsystem.permissions import IsBookingOwner
from bookingsystem.serializers import BookingSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def list(self, *args, **kwargs):
        selected_booking_date_json_string = self.request.QUERY_PARAMS.get('selected_date')
        selected_booking_date = datetime.strptime(selected_booking_date_json_string, '%Y-%m-%dT%H:%M:%S.%fZ')
        one_day_more_than_selected = selected_booking_date + timedelta(days=1)
        #string_date = "{:%Y-%m-%d}".format(selected_booking_date)

        # queryset = self.queryset.filter(room_booked=self.request.QUERY_PARAMS.get('room_number'), start_date__startswith=string_date)         # took a lot of time to figure it out correctly .. see if you can find a better way to do it
        queryset = self.queryset.filter(room_booked=self.request.QUERY_PARAMS.get('room_number'),
                                        start_date__gte=selected_booking_date).exclude(end_date__gte=one_day_more_than_selected)
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data)

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.IsAuthenticated(),)

        if self.request.method == 'POST':
            return (permissions.IsAuthenticated(),)

        return (permissions.IsAuthenticated(), IsBookingOwner(),)

    def perform_create(self, serializer):
        instance = serializer.save(booker_of_slot=self.request.user)   # this sets the field of serializer .... and once it is set the save method converts to model
        #instance = serializer.save(booker_of_slot=self.request.user, date_booked=date.today())                    # remove just for testing purposes
        return super(BookingViewSet, self).perform_create(serializer)

        ## I think this is right indentation not the one given in tutorial for perform_create

### This is used to get the user directly from the request ... rather than user typing his info which is bad
### Big doubt of where is it called .... self.request.user    or   self.request.employee ...... becoz we want to display all the fields of Employee field in serializer so we so this


# class EmployeeBookingsViewSet(viewsets.ViewSet):
#     queryset = Booking.objects.select_related('booker_of_slot').all()
#     serializer_class = BookingSerializer
#     #  comment the below section then the error comes .... but as it is does not return the list of mybookings
#
#     def list(self, request, employee_username=None):
#         queryset = self.queryset.filter(booker_of_slot__username=employee_username)             ## what exactly is being done....
#         serializer = self.serializer_class(queryset, many=True)
#
#         return Response(serializer.data)




