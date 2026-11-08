# tests/test_my_assistant.py

from mock_model import MockModel
from my_assistant import AppointmentAssistant
from my_tool import AppointmentLookup


class SilentModel:
    """A model that never has an answer. It stands in for Ollama being switched off."""

    def reply(self, instructions, history):
        return None


def make_bot():
    """Build a fresh assistant with its own tools and a mock model for each test."""
    tool = AppointmentLookup({"Monday": ["9:00 am", "2:30 pm"]})
    return AppointmentAssistant("Robin", "Be helpful.", tool, MockModel())


def make_bot_with_silent_model():
    """Build an assistant whose model never answers."""
    tool = AppointmentLookup({"Monday": ["9:00 am", "2:30 pm"]})
    return AppointmentAssistant("Robin", "Be helpful.", tool, SilentModel())


def test_tool_retrieves_slots():
    tool = AppointmentLookup({"Monday": ["9:00 am"]})
    assert tool.get_open_slots("Monday") == ["9:00 am"]


def test_valid_day_query():
    bot = make_bot()
    reply = bot.respond("What times are open on Monday?")
    assert "9:00 am" in reply


def test_missing_day_prompts_user():
    bot = make_bot()
    reply = bot.respond("What is available?")
    assert "Which day?" in reply


def test_booking_escalates_to_human():
    bot = make_bot()
    reply = bot.respond("Please book me for Monday at 9")
    assert "front desk" in reply


def test_unsupported_query_safe_reply():
    bot = make_bot()
    reply = bot.respond("Do you validate parking?")
    assert "not sure" in reply


def test_safe_reply_when_the_model_has_no_answer():
    bot = make_bot_with_silent_model()
    assert "try again" in bot.respond("hello")
