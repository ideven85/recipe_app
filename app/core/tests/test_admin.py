from django.contrib.auth import get_user_model
from django.test import TestCase,Client
from django.urls import reverse


class AdminSiteTests(TestCase):
    """
    Tests for django admin
    """
    def setUp(self):
        self.client=Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password='test123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='user@example.com',
            password='test123pass',
            name='Test User'
        )

    def test_users_list(self):
        """Tests that users are listed on page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)
        self.assertContains(res,self.user.name)
        self.assertContains(res,self.user.email)


