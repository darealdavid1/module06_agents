# my_tool.py
# Author: David Leatherman


class AppointmentLookup:
    """Tool that tracks available appointment slots by day."""

    def __init__(self, schedule):
        self.schedule = schedule
        self.bookings = 0

    def find_day(self, text):
        """Return the day mentioned in the user message, or None."""
        text_lower = text.lower()
        for day in self.schedule:
            if day.lower() in text_lower:
                return day
        return None

    def get_open_slots(self, day):
        """Look up the open times on a specific day.

        Args:
            day: The day to check, like Monday.
        """
        found = self.find_day(day)
        if found is None:
            return "Which day? I can check Monday, Wednesday, or Friday."
        slots = self.schedule.get(found, [])
        if slots:
            return f"Open times on {found.lower()}: {', '.join(slots)}."
        return f"There are no open times on {found}."

    def book_appointment(self, day, time):
        """Record an approved booking."""
        self.bookings += 1
