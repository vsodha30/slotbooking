import datetime
from django.db import models

from authentication.models import Employee


class Booking(models.Model):
    ROOM_NUMBERS = (
        (1, 'Conference Room number 1'),
        (2, 'Conference Room number 2'),
        (3, 'Conference Room number 3'),
    )

   
    room_booked = models.IntegerField(choices=ROOM_NUMBERS, blank=False)
    # date_booked = models.DateField(blank=False)
    # slot_booked = models.IntegerField(choices=SLOT_NUMBERS, blank=False)
    start_date = models.DateTimeField(blank=False)
    end_date = models.DateTimeField(blank=False)
    booker_of_slot = models.ForeignKey(Employee, related_name='my_bookings', blank=False)
    #is_booking_open = models.BooleanField(default=True)

    class Meta:
        unique_together = ('room_booked', 'start_date')

    def __unicode__(self):
        reprsentation = str(self.room_booked) + " " + str(self.start_date) + " " + str(self.end_date) + " " + str(self.booker_of_slot_id)
        return reprsentation
