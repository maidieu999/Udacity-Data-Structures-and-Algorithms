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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

text_first_record = texts[0]
incoming_text_number, answering_text_number, time_text = text_first_record

call_last_record = calls[-1]
incoming_call_number, answering_call_number, time_call, during_call = call_last_record

print(f"First record of texts, {incoming_text_number} texts {answering_text_number} at time {time_text}")
print(f"Last record of calls, {incoming_call_number} calls {answering_call_number} at time {time_call}, lasting {during_call} seconds")
