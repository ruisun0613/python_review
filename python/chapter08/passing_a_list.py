"""
8-9. Messages: Make a list containing a series of short text messages. Pass
the list to a function called show_messages(), which prints each text message.
"""
messages = [
    "Hello!",
    "See you soon.",
    "Good luck!"
]

def show_messages(messages):
    for message in messages:
        print(message)

show_messages(messages)
"""
8-10. Sending Messages: Start with a copy of your program from Exercise
8-9. Write a function called send_messages() that prints each text message and
moves each message to a new list called sent_messages as it’s printed. After
calling the function, print both of your lists to make sure the messages were
moved correctly.
"""
messages = [
    "Hello!",
    "See you soon.",
    "Good luck!"
]

sent_messages = []

def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    while messages:
        omit_message = messages.pop()
        print(f"Printing message:{omit_message}")
        sent_messages.append(omit_message)
    print(messages)
    print(sent_messages)

send_messages(messages, sent_messages)
"""
8-11. Archived Messages: Start with your work from Exercise 8-10. Call
the function send_messages() with a copy of the list of messages. After calling
the function, print both of your lists to show that the original list has
retained its messages.
"""
messages = [
    "Hello!",
    "See you soon.",
    "Good luck!"
]

sent_messages = []

def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    while messages:
        omit_message = messages.pop()
        print(f"Printing message:{omit_message}")
        sent_messages.append(omit_message)


send_messages(messages[:], sent_messages)
print(messages)
print(sent_messages)