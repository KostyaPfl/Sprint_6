from datetime import datetime, timedelta
import random


def generate_after_tomorrow_date():
    today = datetime.now().date()
    after_tomorrow = today + timedelta(days=3)
    after_tomorrow_formatted = after_tomorrow.strftime("%d.%m.%Y")
    return str(after_tomorrow_formatted)

def generate_phone_number():
    return f"+7{random.randint(1000000000, 9999999999)}"



