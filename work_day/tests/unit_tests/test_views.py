import datetime

from django.test import (
    TestCase,
    Client
)
from django.urls import reverse
from django.utils import timezone

from work_day.models import *


class BaseTest(TestCase):
    def setUp(self):
        self.login_url = reverse('login')
        self.register_url = reverse('register')
        user = User.objects.create_user(
            username='testUser', password='123456'
        )
        country = Country.objects.create(name='Peru')
        city = City.objects.create(country=country, name='Arequipa')
        Professional.objects.create(
            user=user, city=city, phone='999999999', id_number='11111111',
        )
        return super().setUp()


class LoginTest(BaseTest):
    def test_can_access_page(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')

    def test_successful_login(self):
        response = self.client.post(
            self.login_url,
            {'username': 'testUser', 'password': '123456'},
            follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_authenticated)
        self.assertRedirects(response, reverse('home'))

    def test_cant_login_with_invalid_username(self):
        response = self.client.post(
            self.login_url,
            {'username': '', 'password': '123456'},
            follow=True
        )
        self.assertFalse(response.context['user'].is_authenticated)


class RegisterTest(BaseTest):
    def test_can_access_page(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')


class ViewsTest(BaseTest):
    def test_home_view_without_login(self):
        response = self.client.get(
            reverse('home'), follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')

    def test_home_view_with_login(self):
        self.client.login(username='testUser', password='123456')
        response = self.client.get(
            reverse('home'), follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
