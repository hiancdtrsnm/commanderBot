from datetime import timezone, datetime, timedelta
from config import battles

def transform_orders(orders):
    return orders

async def next_battle():
    global  battles
    times = []
    now = datetime.now(timezone.utc)
    for battle in battles:
        hour, minutes = map(int, battle.split(':'))
        t = datetime(now.year, now.month, now.day, hour, minutes, tzinfo=timezone.utc)
        if now > t:
            t += timedelta(days=1)

        times.append(t)

    next_battle = min(times)

    return next_battle