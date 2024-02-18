"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that  omakeutgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

call_senders = set([data[0] for data in calls])
call_receivers = set([data[1] for data in calls])

text_senders = set([data[0] for data in texts])
text_receivers = set([data[1] for data in texts])

numbers = []
for call in call_senders:
    if call not in call_receivers and call not in text_senders and call not in text_receivers:
        numbers.append(call)

numbers.sort()

print("These numbers could be telemarketers: ")
for num in numbers:
    print(num)





