# my_main.py
# Author: David Leatherman

from booking_queue import BookingQueue
from my_assistant import AppointmentAssistant
from my_tool import AppointmentLookup
from my_toolbox import MyToolbox
from ollama_model import OllamaModel

MODEL_NAME = "granite4.1:3b"

INSTRUCTIONS = """You are Robin, a scheduling assistant.
Answer in one short sentence.
Only state facts that appear in these instructions or in tool results.
If the client only says hello, greet them and ask how you can help.
If you do not know, say you do not know and offer to pass the client to the front desk."""

SCHEDULE = {
    "Monday": ["9:00 am", "2:30 pm"],
    "Wednesday": ["10:00 am", "1:00 pm", "4:00 pm"],
    "Friday": ["8:30 am", "11:00 am"],
}

tool = AppointmentLookup(SCHEDULE)
queue = BookingQueue(tool)
tools = MyToolbox(tool, queue)
model = OllamaModel(MODEL_NAME)

bot = AppointmentAssistant("Robin", INSTRUCTIONS, tools, model)

print("Type a message, or type quit to stop.")
user_message = input("You: ")
while user_message != "quit":
    print(f"{bot.name}: {bot.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(bot.history)}")

print("Front desk review")
for request in queue.waiting():
    number = request["number"]
    print(
        f"Request {number}: {request['client_name']}, {request['day']} at {request['time']}"
    )
    answer = input("Approve? yes or no: ")
    if answer == "yes":
        print(queue.approve(number))
    else:
        print(queue.reject(number))

print(f"Total bookings approved: {tool.bookings}")
