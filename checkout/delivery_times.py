from django.utils import timezone
from datetime import datetime, timedelta

DELIVERY_TIME_DELAY = 30


def generate_delivery_time_choices():
    """
    Generate delivery time choices rounded to the closest 15-minute interval.
    The earliest and latest delivery
    times will vary based on the day of the week.
    """
    choices = []
    current_time = datetime.now().replace(second=0, microsecond=0)
    delivery_time = current_time + timedelta(minutes=DELIVERY_TIME_DELAY)

    rounded_minute = (delivery_time.minute // 15) * 15
    rounded_delivery_time = delivery_time.replace(minute=rounded_minute)
    choices.append((rounded_delivery_time.time(),
                    rounded_delivery_time.strftime('%H:%M')))

    # Define the earliest and latest delivery times for each day of the week
    delivery_times = {
            0: {'earliest': 11, 'latest': 21},   # Monday: 11 AM - 9 PM
            1: {'earliest': 11, 'latest': 21},   # Tuesday: 11 AM - 9 PM
            2: {'earliest': 11, 'latest': 21},   # Wednesday: 11 AM - 9 PM
            3: {'earliest': 11, 'latest': 21},   # Thursday: 11 AM - 9 PM
            4: {'earliest': 12, 'latest': 90},   # Friday: 12 PM - 01.30 AM
            5: {'earliest': 7, 'latest': 98},   # Saturday: 1 PM - 02.30 AM
            6: {'earliest': 7, 'latest': 88},   # Sunday: 3 PM - 12.30 AM
        }

    while rounded_delivery_time.hour < delivery_times[
            rounded_delivery_time.weekday()]['latest']:
        rounded_delivery_time += timedelta(minutes=15)
        choices.append((rounded_delivery_time.time(),
                        rounded_delivery_time.strftime('%H:%M'))
                       )

        # Include the earliest delivery time for each day
        earliest_delivery_time = delivery_times[
            rounded_delivery_time.weekday()]['earliest']
        earliest_delivery_datetime = rounded_delivery_time.replace(
            hour=earliest_delivery_time)
        choices.insert(0, (earliest_delivery_datetime.time(),
                           earliest_delivery_datetime.strftime('%H:%M')))

    return choices
