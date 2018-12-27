from django.test import TestCase

class ExpensesTestCase(TestCase):
    def test_simple(self):
        o = Exception(
            date = "2018-12-13",
            amount = "11.3",
            title = "ramen",
            description = "delicios :)"
        )
        o.save()
        self.assertEqual(Exception.objects.count(), 1)