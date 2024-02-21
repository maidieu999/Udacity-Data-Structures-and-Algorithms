"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

telephone_time = dict()

for call in calls:
    # call[0] is the caller (making a call), call[1] is the receiver (answering the call), call[3] is the duration
    for call_element in [0, 1]:
        if call[call_element] not in telephone_time:
            telephone_time[call[call_element]] = 0
        telephone_time[call[call_element]] += int(call[3])

max_time = max(telephone_time.values())
max_phone = max(telephone_time, key=telephone_time.get)

print(f"{max_phone} spent the longest time, {max_time} seconds, on the phone during September 2016.")
