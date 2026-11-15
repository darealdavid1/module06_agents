# Week 12 answers

## Exercise 1
1. The messages the customer typed: 
I want to change my shipping address, It's order A102, & 9 Pine Street, Tampa

2. How many tool requests were refused, and why: 
2 because the first used order A100 and the second used the address 123 Main St, Anytown, AN 12345. That wasnt typed by the user

3. If the customer now types "thanks", how many messages does Ollama receive on the next call?
Now 14 different messages. The system message, the 6 user and assistant entries, two for each of the 3 tool entries, and the new message.

4. Why does "Do you sell gift cards?" still go to a person, and why is that acceptable?
Because the payment rule looks for card anywhere in the message. A payment question could put card details in front of the user by accident.


# Exercise 3
Type a message, or type quit to stop.
You: i want to change my shipping address
Sunny: Your request to change the shipping address has been submitted and will be reviewed by staff for approval.
You: quit
Messages in this conversation: 3
Staff review
Request 1: A100 to 123 Main St, Anytown, AN 12345
Approve? yes or no: no
Request 1 rejected.
A100 14 Bay Road
A101 3 Gull Lane
A102 88 Pier Street