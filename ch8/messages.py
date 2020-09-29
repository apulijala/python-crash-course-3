"""
8-9. Messages: Make a list containing a series of short text messages. Pass the list 
to a function called show_messages(), which prints each text message.

# Have you done testing to see if it breaks and done it in all possible ways
"""

def show_messages(messages):
    print("All Mantras are: ")
    print(messages)
    for message in messages:
        print(message)

"""
8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. Write a 
function called send_messages() that prints each text message and moves each message 
to a new list called sent_messages as it’s printed. 
After calling the function, print both of your lists to make sure the messages 

    this is for anna 
were moved correctly.
"""
def copy_after_show(guru_mantras, recited_mantras):
    print(guru_mantras)
    while guru_mantras: # Empty arrays is false . 
        recited_mantras.append(guru_mantras.pop())
    print("Guru Mantras: ")
    print(guru_mantras)
    return recited_mantras.reverse()
    # return recited_mantras # as order is important. 

    







