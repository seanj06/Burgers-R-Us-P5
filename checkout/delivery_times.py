from django.utils import timezone
from datetime import datetime, timedelta, time

DELIVERY_TIME_DELAY = 30

OPENING_HOURS = {
    0: {'start': '11:00', 'end': '23:00'},   # Monday
    1: {'start': '11:00', 'end': '23:00'},   # Tuesday
    2: {'start': '11:00', 'end': '23:00'},   # Wednesday
    3: {'start': '11:00', 'end': '23:00'},   # Thursday
    4: {'start': '12:00', 'end': '01:30'},   # Friday
    5: {'start': '12:00', 'end': '02:30'},   # Saturday
    6: {'start': '12:00', 'end': '00:30'},   # Sunday
}


def generate_delivery_time_choices(delivery_date):
    """
    Generates delivery time choices
    rounded to the closest 15-minute interval.
    """
    choices = []
    current_time = datetime.now().replace(second=0, microsecond=0)
    delivery_time = current_time + timedelta(minutes=DELIVERY_TIME_DELAY)
    current_day = delivery_time.weekday()

    if current_day in OPENING_HOURS:
        opening_hours = OPENING_HOURS[current_day]
        start_time = datetime.strptime(opening_hours['start'], '%H:%M').time()
        end_time_str = opening_hours['end']
        if end_time_str:
            end_time = datetime.strptime(end_time_str, '%H:%M').time()
            end_time = datetime.combine(delivery_date, end_time)
        else:
            end_time = None

        rounded_minute = (delivery_time.minute // 15) * 15
        rounded_delivery_time = delivery_time.replace(minute=rounded_minute)

        # Skip delivery time options before the opening time
        if rounded_delivery_time.time() < start_time:
            rounded_delivery_time = rounded_delivery_time.replace(
                hour=start_time.hour, minute=start_time.minute
            )

        if end_time is not None and end_time < datetime.combine(
                delivery_date, start_time):
            end_time = datetime.combine(
                delivery_date + timedelta(days=1), end_time.time()
            )

        while end_time is None or rounded_delivery_time <= end_time:
            choices.append(
                (rounded_delivery_time.time(),
                 rounded_delivery_time.strftime('%H:%M'))
            )
            rounded_delivery_time += timedelta(minutes=15)

    if choices:
        return choices
