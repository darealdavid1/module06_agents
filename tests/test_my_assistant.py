from booking_queue import BookingQueue
from fake_model import FakeModel
from my_assistant import AppointmentAssistant
from my_tool import AppointmentLookup
from my_toolbox import MyToolbox


def make_bot(model):
    tool = AppointmentLookup({"Monday": ["9:00 am", "2:30 pm"]})
    queue = BookingQueue(tool)
    tools = MyToolbox(tool, queue)
    return AppointmentAssistant("Robin", "Be helpful.", tools, model)


def ask_for_tool(name, arguments):
    return {"tool": name, "arguments": arguments}


def test_handoff_happens():
    bot = make_bot(FakeModel([]))
    assert "front desk" in bot.respond("Please cancel my appointment")


def test_made_up_detail_is_refused():
    model = FakeModel(
        [
            ask_for_tool(
                "request_booking",
                {"day": "Monday", "time": "9:00 am", "client_name": "Bob"},
            ),
            {"text": "What is your name?"},
        ]
    )
    bot = make_bot(model)
    bot.respond("Book Monday at 9:00 am")
    assert "has not provided their name" in bot.history[1]["content"]


def test_request_waits_in_queue():
    model = FakeModel(
        [
            ask_for_tool(
                "request_booking",
                {"day": "Monday", "time": "9:00 am", "client_name": "Dana Cruz"},
            ),
            {"text": "Sent to front desk."},
        ]
    )
    bot = make_bot(model)
    bot.respond("My name is Dana Cruz, book Monday at 9:00 am")
    assert len(bot.tools.booking_queue.waiting()) == 1
