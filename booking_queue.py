# booking_queue.py
# Author: David Leatherman


class BookingQueue:
    """Bookings waiting for the front desk to approve."""

    def __init__(self, schedule_tool):
        self.schedule_tool = schedule_tool
        self.requests = []

    def request_booking(self, day, time, client_name):
        """Ask the front desk to book an appointment.

        Args:
            day: The day, like Monday.
            time: The time, like 9:00 am.
            client_name: The full name of the client.
        """
        number = len(self.requests) + 1
        request = {
            "number": number,
            "day": day,
            "time": time,
            "client_name": client_name,
            "status": "waiting",
        }
        self.requests.append(request)
        return f"Request {number} to book {day} at {time} for {client_name} was sent to the front desk."

    def waiting(self):
        result = []
        for req in self.requests:
            if req["status"] == "waiting":
                result.append(req)
        return result

    def find(self, number):
        for req in self.requests:
            if req["number"] == number:
                return req
        return None

    def approve(self, number):
        req = self.find(number)
        if req is None:
            return f"There is no request {number}."
        if req["status"] != "waiting":
            return f"Request {number} is already {req['status']}."
        req["status"] = "approved"
        self.schedule_tool.book_appointment(req["day"], req["time"])
        return f"Request {number} approved."

    def reject(self, number):
        req = self.find(number)
        if req is None:
            return f"There is no request {number}."
        if req["status"] != "waiting":
            return f"Request {number} is already {req['status']}."
        req["status"] = "rejected"
        return f"Request {number} rejected."
