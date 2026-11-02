# my_assistant.py
# Author: David Leatherman

ESCALATION_KEYWORDS = ["book", "cancel", "reschedule", "urgent"]


class AppointmentAssistant:
    """Assistant managing appointment slot queries."""

    def __init__(self, name, schedule_tool):
        self.name = name
        self.schedule_tool = schedule_tool
        self.history = []

    def respond(self, user_message):
        self.history.append({"role": "user", "content": user_message})
        reply = self.choose_reply(user_message)
        self.history.append({"role": "assistant", "content": reply})
        return reply

    def choose_reply(self, user_message):
        text = user_message.lower()
        if any(word in text for word in ESCALATION_KEYWORDS):
            return (
                "I can't change the schedule. I'm passing you to the front desk."
            )
        if "hello" in text:
            return f"Hello! I'm {self.name}. Ask me which times are open on a day."
        if (
            "open" in text
            or "available" in text
            or "times" in text
            or "schedule" in text
        ):
            day = self.schedule_tool.find_day(user_message)
            if day is None:
                return "Which day? I can check Monday, Wednesday, or Friday."
            slots = self.schedule_tool.get_open_slots(day)
            if slots:
                return f"Open times on {day.lower()}: {', '.join(slots)}."
            return f"There are no open times on {day}."
        return "I'm not sure how to help with that. I can list open times."