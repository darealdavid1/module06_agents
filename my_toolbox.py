# my_toolbox.py
# Author: David Leatherman


class MyToolbox:
    """Checks tool requests for the appointment assistant."""

    def __init__(self, schedule_tool, booking_queue):
        self.schedule_tool = schedule_tool
        self.booking_queue = booking_queue

    def tool_list(self):
        return [
            self.schedule_tool.get_open_slots,
            self.booking_queue.request_booking,
        ]

    def run(self, name, arguments, history):
        if name == "get_open_slots":
            day = self.clean(arguments, "day")
            if day == "":
                return "The day is missing. Ask the client which day."
            if not self.customer_said(history, day):
                return "The client has not mentioned that day. Ask them for it."
            return self.schedule_tool.get_open_slots(day)

        if name == "request_booking":
            day = self.clean(arguments, "day")
            time = self.clean(arguments, "time")
            client_name = self.clean(arguments, "client_name")
            if day == "" or time == "" or client_name == "":
                return "I need the day, the time, and the client's full name. Ask the client for missing details."
            if not self.customer_said(history, day):
                return "The client has not mentioned that day. Ask them."
            if not self.customer_said(history, time):
                return "The client has not mentioned that time. Ask them."
            if not self.customer_said(history, client_name):
                return "The client has not provided their name. Ask them."
            return self.booking_queue.request_booking(day, time, client_name)

        return f"There is no tool named {name}."

    def clean(self, arguments, key):
        return str(arguments.get(key, "")).strip()

    def customer_said(self, history, text):
        for message in history:
            if message["role"] == "user" and text.lower() in message["content"].lower():
                return True
        return False
