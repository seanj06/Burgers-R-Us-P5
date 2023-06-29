from django.test import TestCase
from datetime import date, time
from .delivery_times import generate_delivery_time_choices


class TestDeliveryTimeChoices(TestCase):
    """
    Unit Tests for delivery_time_choices function
    """

    def test_generate_delivery_time_choices(self):
        delivery_date = date.today()
        choices = generate_delivery_time_choices(delivery_date)

        self.assertIsInstance(choices, list)
        self.assertTrue(len(choices) > 0)

        for choice in choices:
            time_obj, time_str = choice
            self.assertIsInstance(time_obj, time)
            self.assertIsInstance(time_str, str)
            self.assertEqual(time_str, time_obj.strftime('%H:%M'))

        opening_hours = {
            0: {'start': '11:00', 'end': '21:00'},   # Monday
            1: {'start': '11:00', 'end': '21:00'},   # Tuesday
            2: {'start': '11:00', 'end': '21:00'},   # Wednesday
            3: {'start': '11:00', 'end': '21:00'},   # Thursday
            4: {'start': '12:00', 'end': '01:30'},   # Friday
            5: {'start': '12:00', 'end': '02:30'},   # Saturday
            6: {'start': '12:00', 'end': '00:30'},   # Sunday
        }

        current_day = delivery_date.weekday()
        opening_hours_day = opening_hours.get(current_day)
        if opening_hours_day:
            start_time_str = opening_hours_day['start']
            end_time_str = opening_hours_day['end']
            start_time = time.fromisoformat(start_time_str)
            end_time = (
                time.fromisoformat(end_time_str) if end_time_str else None
                )

            for choice in choices:
                time_obj, _ = choice
                self.assertGreaterEqual(time_obj, start_time)
                if end_time:
                    self.assertLessEqual(time_obj, end_time)
