from my_assistant import AppointmentAssistant
from my_tool import AppointmentLookup


def make_assistant():
    schedule = {"Monday": ["9:00 am", "2:30 pm"]}
    return AppointmentAssistant("Robin", AppointmentLookup(schedule))


def test_tool_retrieves_slots():
    tool = AppointmentLookup({"Monday": ["9:00 am"]})
    assert tool.get_open_slots("Monday") == ["9:00 am"]


def test_valid_day_query():
    bot = make_assistant()
    reply = bot.respond("What times are open on Monday?")
    assert "9:00 am" in reply


def test_missing_day_prompts_user():
    bot = make_assistant()
    reply = bot.respond("What is available?")
    assert "Which day?" in reply


def test_booking_escalates_to_human():
    bot = make_assistant()
    reply = bot.respond("Please book me for Monday at 9")
    assert "front desk" in reply


def test_unsupported_query_safe_reply():
    bot = make_assistant()
    reply = bot.respond("Do you validate parking?")
    assert "not sure" in reply