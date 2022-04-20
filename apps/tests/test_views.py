import factory
from django.urls import reverse
from faker import Faker
from rest_framework import status
# from nose.tools import ok_, eq_
# from django.test import TestCase
from rest_framework.test import APITestCase

from .factories import PlanFactory
from ..models import Plans

fake = Faker()


# Create your tests here.

class TestPlanListTestCase(APITestCase):

    def setUp(self) -> None:
        self.url = reverse('plans')
        self.plan_data = factory.build(dict, FACTORY_CLASS=PlanFactory)

    def test_post_request_with_no_data_fails(self):
        response = self.client.post(self.url, {})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_request_with_valid_data_succeeds(self):
        response = self.client.post(self.url, self.plan_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        plan = Plans.objects.get(pk=response.data.get('id'))
        self.assertEqual(plan.name, self.plan_data.get('name'))
        self.assertEqual(plan.amount, self.plan_data.get('amount'))


class TestPlanDetailTestCase(APITestCase):
    """
    Tests /users detail operations.
    """

    def setUp(self):
        self.plan = PlanFactory()
        self.url = reverse('plans', kwargs={'pk': self.plan.pk})

    def test_get_request_returns_a_given_plan(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_request_updates_a_plan(self):
        name = fake.name()
        payload = {
            'name': name,
            'amount': fake.random_int(min=10, max=100),
            'is_active': True
        }
        response = self.client.put(self.url, payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        user = Plans.objects.get(pk=self.plan.id)
        self.assertEqual(user.name, name)
