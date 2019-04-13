from django.test import TestCase
from ..models import User


class UserTest(TestCase):

    def setUp(self):
        new_user = User(username='omar-tester', email='metesteremail@gmail.com', password='dynamo2020')
        new_user.set_password('dynamo2020')
        new_user.save()

    def test_user(self):
        user = User.objects.get(username='omar-tester')
        self.assertEqual(user.username, 'omar-tester')
