# my_tool.py
# Author: David Leatherman


class AppointmentLookup:
    """Tool that tracks available appointment slots by day."""

    def __init__(self, schedule):
        self.schedule = schedule

    def find_day(self, text):
        """Return the day mentioned in the user message, or None."""
        text_lower = text.lower()
        for day in self.schedule:
            if day.lower() in text_lower:
                return day
        return None

    def get_open_slots(self, day):
        """Return available time slots for a given day, or None."""
        return self.schedule.get(day, None)
