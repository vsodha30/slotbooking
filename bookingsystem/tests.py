from datetime import datetime, timedelta

from django.core.serializers import json
from django.test import TestCase
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase

from authentication.models import Employee
from authentication.tests import create_employee
from bookingsystem.models import Booking
from bookingsystem.serializers import BookingSerializer


def create_booking(start_date, end_date, room_booked, email, username, role):
    employee = Employee.objects.create(email=email, username=username, role=role)
    employee.set_password("password123")
    employee.save()
    booking_serializer = BookingSerializer(data={'start_date': start_date, 'end_date': end_date, 'room_booked': room_booked})
    booking_serializer.is_valid(raise_exception=True)
    booking = booking_serializer.save(booker_of_slot=employee)
    return booking


class BookingModelTests(TestCase):

    def test_booking_model_unicode(self):

        start_date = datetime.now()
        end_date = start_date + timedelta(hours=1)
        room_booked = 1
        email = "abc@gmail.com"
        username = "abc"
        role = "Software Developer"

        booking = create_booking(start_date, end_date, room_booked, email, username, role)

        offset_strip_end = booking.end_date.astimezone(timezone.utc).replace(tzinfo=None)
        self.assertEqual(offset_strip_end, end_date)
        offset_strip_start =  booking.start_date.astimezone(timezone.utc).replace(tzinfo=None)
        self.assertEqual(offset_strip_start, start_date)
        self.assertEqual(booking.room_booked, room_booked)
        print (booking.booker_of_slot.username+" "+Booking.__unicode__(booking))
        self.assertEqual(booking.booker_of_slot.email, email)


class BookingViewTests(APITestCase):



    def test_booking_create(self):
        username = "abc"
        email = "abc@gmail.com"
        role = "Software Developer"
        password = "password123"
        employee = create_employee(email, username, role)
        employee.set_password(password)
        employee.save()

        url = '/api/v1/book/'
        data = { 'start_date': "2016-06-01T03:30:00.000Z",
                 'end_date': "2016-06-01T04:30:00.000Z",
                 'room_booked': "1"
                 }
        #print start_date.isoformat()
        self.client.login(username=username, password=password)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        #print(Booking.objects.get())


    def test_booking_list(self):
        username = "abc"
        email = "abc@gmail.com"
        role = "Software Developer"
        password = "password123"
        employee = create_employee(email, username, role)
        employee.set_password(password)
        employee.save()

        url1 = '/api/v1/book/'
        data = { 'start_date': "2016-06-01T03:30:00.000Z",
                 'end_date': "2016-06-01T04:30:00.000Z",
                 'room_booked': "1"
                 }
        self.client.login(username=username, password=password)
        response1 = self.client.post(url1, data, format='json')

        url = '/api/v1/book/'
        params = { 'room_number': 1,
                   'selected_date': "2016-06-01T03:30:00.000Z",
                   }

        response = self.client.get(url, params)
        print(Booking.objects.get())
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_booking_delete(self):
        username = "abc"
        email = "abc@gmail.com"
        role = "Software Developer"
        password = "password123"
        employee = create_employee(email, username, role)
        employee.set_password(password)
        employee.save()

        url1 = '/api/v1/book/'
        data = {'start_date': "2016-06-01T03:30:00.000Z",
                'end_date': "2016-06-01T04:30:00.000Z",
                'room_booked': "1"
                }
        self.client.login(username=username, password=password)
        response1 = self.client.post(url1, data, format='json')
        identity = Booking.objects.latest(field_name='id').id

        url = '/api/v1/book/' + str(identity) + '/'

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)













