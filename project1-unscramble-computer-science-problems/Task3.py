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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


# PART A
def is_bangalore_call(call):
    return call[0][0:5] == "(080)"


def extract_area_code(call):
    if call.startswith("140"):  # Telemarketers
        return "140"
    elif call.startswith("("):  # Fixed lines
        return call.split(sep=")")[0] + ")"
    else:  # Mobile numbers
        return call[:4]


bangalore_called_prefix = []

for call in calls:
    if is_bangalore_call(call):
        bangalore_called_prefix.append(extract_area_code(call[1]))

    bng_called_prefix_resum = list(set(bangalore_called_prefix))
    bng_called_prefix_resum.sort()

print("\n The numbers called by people in Bangalore have codes:")
for related_prefix in bng_called_prefix_resum:
    print(related_prefix)


# PART B
total_calls_from_bangalore_to_bangalore = 0

for call_prefix in bangalore_called_prefix:
    if call_prefix == "(080)":
        total_calls_from_bangalore_to_bangalore += 1


print(
    "\n {} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(
        round(
            total_calls_from_bangalore_to_bangalore
            / len(bangalore_called_prefix)
            * 100,
            2,
        )
    )
)
