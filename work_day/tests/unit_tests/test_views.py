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
        self.country = Country.objects.create(name='Peru')
        self.city = City.objects.create(country=self.country, name='Arequipa')
        self.professional = Professional.objects.create(
            user=user, city=self.city, phone='999999999', id_number='11111111',
        )
        cv = Curriculum.objects.create(owner=self.professional)
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
    def test_index_view_doesnt_require_login(self):
        response = self.client.get(reverse('index'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_home_view_without_login(self):
        response = self.client.get(reverse('home'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')

    def test_home_view_with_login(self):
        self.client.login(username='testUser', password='123456')
        response = self.client.get(reverse('home'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_view_user_profile_without_login(self):
        response = self.client.get(reverse('user_profile'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')

    def test_view_own_user_profile_with_login(self):
        self.client.login(username='testUser', password='123456')
        response = self.client.get(reverse('user_profile'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/profile.html')

    def test_view_professionals_without_login(self):
        response = self.client.get(reverse('professionals'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')

    def test_view_professionals_with_login(self):
        self.client.login(username='testUser', password='123456')
        response = self.client.get(reverse('professionals'), follow=True)
        print(response.context['professionals'][0])
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'professionals.html')
        self.assertEqual(len(response.context['professionals']), 1)

    def test_view_my_posts_receive_offers_list(self):
        self.client.login(username='testUser', password='123456')
        response = self.client.get(reverse('my_posts'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'my_posts.html')
        self.assertEqual(len(response.context['offers']), 0)