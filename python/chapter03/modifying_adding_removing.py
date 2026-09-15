"""
3-4. Guest List: If you could invite anyone, living or deceased, to dinner,
who would you invite? Make a list that includes at least three people you’d
like to invite to dinner. Then use your list to print a message to each person,
inviting them to dinner.
"""
friend_names = ["steven", "davis", "cliff"]

print(f"Hello {friend_names[0]}, I want invite you to have a dinner.")
print(f"Hello {friend_names[1]}, I want invite you to have a dinner.")
print(f"Hello {friend_names[2]}, I want invite you to have a dinner.")

"""
3-5. Changing Guest List: You just heard that one of your guests can’t
make the dinner, so you need to send out a new set of invitations. You’ll
have to think of someone else to invite.
Start with your program from Exercise 3-4. Add a print() call at the end of
your program, stating the name of the guest who can’t make it.
Modify your list, replacing the name of the guest who can’t make it with the
name of the new person you are inviting.
Print a second set of invitation messages, one for each person who is still in
your list.
"""
print("-" * 40)
friend_names = ["steven", "davis", "cliff"]

print(f"Hello {friend_names[0]}, I want invite you to have a dinner.")
print(f"Hello {friend_names[1]}, I want invite you to have a dinner.")
print(f"Hello {friend_names[2]}, I want invite you to have a dinner.")
print(f"{friend_names[2]} can’t make the dinner")

friend_names[2] = "james"

print(f"Hello {friend_names[2]}, I want invite you to have a dinner.")

"""
3-6. More Guests: You just found a bigger dinner table, so now more space
is available. Think of three more guests to invite to dinner.
Start with your program from Exercise 3-4 or 3-5. Add a print() call to the
end of your program, informing people that you found a bigger table.
Use insert() to add one new guest to the beginning of your list.
Use insert() to add one new guest to the middle of your list.
Use append() to add one new guest to the end of your list.
Print a new set of invitation messages, one for each person in your list.
"""
print("-" * 40)
friend_names = ["steven", "davis", "cliff"]

print(f"Hello {friend_names[0]}, I want invite you to have a dinner.")
print(f"Hello {friend_names[1]}, I want invite you to have a dinner.")
print(f"Hello {friend_names[2]}, I want invite you to have a dinner.")
print(f"{friend_names[2]} can’t make the dinner")

friend_names[2] = "james"

print(f"Hello {friend_names[2]}, I want invite you to have a dinner.")

print("Hello everyone, I found a bigger table")

friend_names.insert(0,"George")
friend_names.insert(2, "Amy")
friend_names.append("Kim")

print(f"Hello {friend_names[0]}, I want invite you to have a dinner.")
print(f"Hello {friend_names[2]}, I want invite you to have a dinner.")
print(f"Hello {friend_names[4]}, I want invite you to have a dinner.")

"""
3-7. Shrinking Guest List: You just found out that your new dinner table
won’t arrive in time for the dinner, and now you have space for only two
guests.
Start with your program from Exercise 3-6. Add a new line that prints a
message saying that you can invite only two people for dinner.
Use pop() to remove guests from your list one at a time until only two names
remain in your list. Each time you pop a name from your list, print a
message to that person letting them know you’re sorry you can’t invite
them to dinner.
Print a message to each of the two people still on your list, letting them
know they’re still invited.
Use del to remove the last two names from your list, so you have an empty
list. Print your list to make sure you actually have an empty list at the end of
your program.
"""
print("-" * 40)
friend_names = ["steven", "davis", "cliff"]

print(f"Hello {friend_names[0]}, I want invite you to have a dinner.")
print(f"Hello {friend_names[1]}, I want invite you to have a dinner.")
print(f"Hello {friend_names[2]}, I want invite you to have a dinner.")
print(f"{friend_names[2]} can’t make the dinner")

friend_names[2] = "james"

print(f"Hello {friend_names[2]}, I want invite you to have a dinner.")

print("Hello everyone, I found a bigger table")

friend_names.insert(0,"George")
friend_names.insert(2, "Amy")
friend_names.append("Kim")

print(f"Hello {friend_names[0]}, I want invite you to have a dinner.")
print(f"Hello {friend_names[2]}, I want invite you to have a dinner.")
print(f"Hello {friend_names[4]}, I want invite you to have a dinner.")

# 3.7
print("Sorry everyone, I can invite only two people for dinner.")

friend_names.pop(5)
friend_names.pop(4)
friend_names.pop(3)
friend_names.pop(2)

print(f"Hello {friend_names[0]}, I want invite you to have a dinner.")
print(f"Hello {friend_names[1]}, I want invite you to have a dinner.")

del friend_names[1]
del friend_names[0]

print(friend_names)