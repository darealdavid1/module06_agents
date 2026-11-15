# my_assistant.py
# Author: David Leatherman

HANDOFF_WORDS = ["cancel", "reschedule", "urgent"]
MAX_TOOL_ROUNDS = 3


class AppointmentAssistant:
    """Assistant managing appointment slot queries."""

    def __init__(self, name, instructions, tools, model):
        self.name = name
        self.instructions = instructions
        self.tools = tools
        self.model = model
        self.history = []

    def respond(self, user_message):
        self.history.append({"role": "user", "content": user_message})
        reply = self.choose_reply(user_message)
        self.history.append({"role": "assistant", "content": reply})
        return reply

    def choose_reply(self, user_message):
        text = user_message.lower()
        if self.needs_human(text):
            return "I can't change a booking. I'm passing you to the front desk."
        return self.model_reply()

    def needs_human(self, text):
        for word in HANDOFF_WORDS:
            if word in text:
                return True
        return False

    def model_reply(self):
        rounds = 0
        while rounds < MAX_TOOL_ROUNDS:
            tool_list = self.tools.tool_list()
            decision = self.model.decide(self.instructions, self.history, tool_list)

            if decision is None:
                return "Sorry, I can't answer that right now. Please try again later."

            if "text" in decision:
                return decision["text"]

            name = decision["tool"]
            arguments = decision["arguments"]
            result = self.tools.run(name, arguments, self.history)

            self.history.append(
                {
                    "role": "tool",
                    "tool_name": name,
                    "arguments": arguments,
                    "content": result,
                }
            )
            rounds += 1
        return "Sorry, I couldn't finish that. I'm passing you to the front desk."
