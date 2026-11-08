# my_assistant.py
# Author: David Leatherman

ESCALATION_KEYWORDS = ["book", "cancel", "reschedule", "urgent"]


class AppointmentAssistant:
    """Assistant managing appointment slot queries."""

    def __init__(self, name, instructions, schedule_tool, model):
        self.name = name
        self.instructions = instructions
        self.schedule_tool = schedule_tool
        self.model = model
        self.history = []

    def respond(self, user_message):
        self.history.append({"role": "user", "content": user_message})
        reply = self.choose_reply(user_message)
        self.history.append({"role": "assistant", "content": reply})
        return reply

    def choose_reply(self, user_message):
        text = user_message.lower()

        # 1. Handoff rules
        if any(word in text for word in ESCALATION_KEYWORDS):
            return "I can't change the schedule. I'm passing you to the front desk."

        # 2. Tool rules
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

        # 3. Model fallback (handles greetings and unexpected questions)
        return self.model_reply()

    def model_reply(self):
        """Ask the model for a reply. Give a safe answer if the model has none."""
        reply = self.model.reply(self.instructions, self.history)
        if reply is None:
            return "Sorry, I can't answer that right now. Please try again later."
        return reply
