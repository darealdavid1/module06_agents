## Mini-Project: Tax Office Appointment Assistant

This assistant helps clients by answering queries about open appointment slots for a tax  office. The system is mock-based because it relies on static memory dictionary data and simple keyword matching rather than a live database or natural language processing. 

Requests containing modification words such as "book", "cancel", or "reschedule" are escalated to human front desk staff because managing calendar reservations and validating client identities requires authorized human oversight. 

If this system handled real customer data, the lack of authentication or concurrency controls could lead to data leaks or double-booking across concurrent user sessions.