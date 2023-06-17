from django.utils import timezone
from datetime import datetime, timedelta

DELIVERY_TIME_DELAY = 30

OPENING_HOURS = {
    0: {'start': '11:00', 'end': '21:00'},   # Monday
    1: {'start': '11:00', 'end': '21:00'},   # Tuesday
    2: {'start': '11:00', 'end': '21:00'},   # Wednesday
    3: {'start': '11:00', 'end': '21:00'},   # Thursday
    4: {'start': '12:00', 'end': '01:30'},   # Friday
    5: {'start': '13:00', 'end': '02:30'},   # Saturday
    6: {'start': '15:00', 'end': '00:30'},   # Sunday
}


def generate_delivery_time_choices():
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
        end_time = datetime.strptime(
            opening_hours['end'], '%H:%M'
            ).time() if opening_hours['end'] else None

        if current_time < delivery_time.replace(
            hour=start_time.hour, minute=start_time.minute
                ):
            return [("Closed", "Sorry, we are closed for delivery")]

        rounded_minute = (delivery_time.minute // 15) * 15
        rounded_delivery_time = delivery_time.replace(minute=rounded_minute)

        # Skip delivery time options before the opening time
        if rounded_delivery_time.time() < start_time:
            rounded_delivery_time = rounded_delivery_time.replace(
                hour=start_time.hour, minute=start_time.minute
                )

        while end_time is None or rounded_delivery_time.time() <= end_time:
            choices.append(
                (rounded_delivery_time.time(),
                 rounded_delivery_time.strftime('%H:%M'))
            )
            rounded_delivery_time += timedelta(minutes=15)

    return choices
