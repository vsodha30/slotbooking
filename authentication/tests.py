from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from authentication.models import Employee
from authentication.views import LoginView


def create_employee(email, username, role):
    employee = Employee.objects.create(email=email, username=username, role=role)
    return employee


class AngularIndexRenderedTests(TestCase):

    def test_index_template_rendered(self):
        url = '/#/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.templates[0].name, 'index.html')
        self.assertEqual(response.templates[1].name, 'stylesheets.html')
        self.assertEqual(response.templates[2].name, 'navbar.html')
        self.assertEqual(response.templates[3].name, 'javascripts.html')


class EmployeeModelTests(TestCase):

    def test_employee_creation(self):
        employee = create_employee("abc@gmail.com", "abc", "Software Developer")
        self.assertEqual(employee, Employee.objects.get(username="abc"))
        self.assertEqual(Employee.__unicode__(employee), "abc@gmail.com")


class EmployeeViewSetCallTests(APITestCase):

    def test_successful_employees_creation(self):
        url = '/api/v1/employees/'
        data = {'username': 'abc', 'password': 'password123', 'email': 'abc@gmail.com', 'role': 'CEO'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Employee.objects.count(), 1)
        self.assertEqual(Employee.objects.get().username, 'abc')

    def test_unsuccessful_employees_creation_without_username(self):
        url = '/api/v1/employees/'
        data = {'password': 'password123', 'email': 'abc@gmail.com', 'role': 'CEO'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Employee.objects.count(), 0)
        self.assertEqual(response.content, '{"username":["This field is required."]}')

        # self.assertEqual(Employee.objects.get().username, 'abc')

    def test_unsuccessful_employees_creation_without_email(self):
        url = '/api/v1/employees/'
        data = {'username': 'abc', 'password': 'password123', 'role': 'CEO'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Employee.objects.count(), 0)
        self.assertEqual(response.content, '{"email":["This field is required."]}')

        #     self.assertEqual(Employee.objects.get().username, 'abc')
        #


    def test_successful_employees_creation_without_password(self):
        url = '/api/v1/employees/'
        data = {'username': 'abc', 'email': 'abc@gmail.com', 'role': 'CEO'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Employee.objects.count(), 0)


    def test_unsuccessful_employees_creation_without_role(self):
        url = '/api/v1/employees/'
        data = {'username': 'abc', 'password': 'password123', 'email': 'abc@gmail.com'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Employee.objects.count(), 0)
        self.assertEqual(response.content, '{"role":["This field is required."]}')


class AuthenticationViewTests(APITestCase):

    def test_successful_login(self):
        employee = create_employee("abc@gmail.com", "abc", "Software Developer")
        employee.set_password("password123")
        employee.save()
        url = '/api/v1/auth/login/'
        data = {'username': 'abc', 'password': 'password123'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 200)

        #response = client.post(url, data)
        #client = APIClient()
        #self.assertTrue(client.login(username="abc", password="password123"))

    def test_unsuccessful_login(self):
        employee = create_employee("abc@gmail.com", "abc", "Software Developer")
        employee.set_password("password123")
        employee.save()
        url = '/api/v1/auth/login/'
        data = {'username': 'abc', 'password': 'wrongpassword'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 401)

    def test_successful_logout(self):
        employee = create_employee("abc@gmail.com", "abc", "Software Developer")
        employee.set_password("password123")
        employee.save()
        url1 = '/api/v1/auth/login/'
        data1 = {'username': 'abc', 'password': 'password123'}
        response1 = self.client.post(url1, data1, format='json')
        #print (response1.cookies)

        url2 = '/api/v1/auth/logout/'
        response2 = self.client.post(url2)
        self.assertEqual(response2.status_code, 204)
        #print (response1.cookies)







