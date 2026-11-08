# my_main.py
# Author: David Leatherman

from my_assistant import AppointmentAssistant
from my_tool import AppointmentLookup

SCHEDULE = {
    "Monday": ["9:00 am", "2:30 pm"],
    "Wednesday": ["10:00 am", "1:00 pm"],
    "Friday": ["11:00 am", "3:00 pm"],
}

tool = AppointmentLookup(SCHEDULE)
assistant = AppointmentAssistant("Robin", tool)

print("Type a message, or type quit to stop.")
user_message = input("You: ")
while user_message != "quit":
    print(f"{assistant.name}: {assistant.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(assistant.history)}")
