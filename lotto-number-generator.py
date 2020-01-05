# Author	Cory Pollard
# Date 		2020.01.05
# Purpose       A simple python script to generete lotto numbers for Lottery West Saturday night draw
# Notes
# Revisions  
# Version       0.1


#!/usr/bin/python
import random

lotterynumbers = []
supplementary1 = []
supplementary2 = []

x = 0
y = 1 
z = 2

# Six randomly drawn numbers
while x < 6:
    lotterynumbers.append(random.randint(1, 45))
    x += 1
 
lotterynumbers.sort()

# supplementary number one
while y < 2: 
    supplementary1.append(random.randint(1, 45))
    y += 2
    
supplementary1.sort()

# supplementary number two
while z < 3: 
    supplementary2.append(random.randint(1, 45))
    z += 3
    
supplementary2.sort()

#print('Saturday Night Lotto'.center(2, '*'))
print('Saturday Night Lotto')

print "Your lucky numbers are: "
print lotterynumbers
print "Supplementary are: "
print supplementary1+supplementary2
