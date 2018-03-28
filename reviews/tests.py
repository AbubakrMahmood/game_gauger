from django.test import TestCase
from reviews.models import Review
from reviews.views import user_login
from django.core.urlresolvers import reverse



class ReviewMethodTests(TestCase):
    def test_ensure_ratings_are_valid(self):
        upper = Review(rating=6)
        upper.save()
        self.assertEqual((upper.rating<=5),True)

        lower = Review(rating=0)
        lower.save()
        self.assertEqual((lower.rating>0),True)

class RegisterViewTests(TestCase):
    def test_user_login_error_message(self):
        response= self.client.get(reverse('views')
        self.assertContains(response, "Invalid login details sipplied.")



