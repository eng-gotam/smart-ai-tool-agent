

from datetime import datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError


def get_datetime(timezone: str = "Asia/Karachi") -> dict:
    """Retrieve the current date and time for a timezone."""

    print(f"[TOOL CALL] DateTime: {timezone}")

    try:
        now = datetime.now(ZoneInfo(timezone))

        return {
            "timezone": timezone,
            "date": now.strftime("%Y-%m-%d"),
            "time": now.strftime("%I:%M:%S %p"),
            "day": now.strftime("%A")
        }

    except ZoneInfoNotFoundError:
        return {
            "error": f"Invalid timezone: {timezone}"
        }
