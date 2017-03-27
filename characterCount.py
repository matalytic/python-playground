#ABSWP_CH 5

import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pformat(count)

"""
phone_number = '7 1 8 2 0 0 2 4 3 2'
count = {}

for digit in phone_number:
    count.setdefault(digit, 0)
    count[digit] = count[digit] + 1

print(count)
"""