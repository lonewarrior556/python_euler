# -*- coding: utf-8 -*-

sequence = []
for n in range(1, 12):
    tot = 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10
    sequence.append(tot)

print sequence
