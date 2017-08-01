# ex9.py More Printing

days = "Mon \\ Tue \\ Wed \\ Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug" #os did not recognize \n for changing lines

print("Here are the days:")
print(days)
print("Here are the months")
print(months) # when using print("Here are the months, months"), the result returned new lines correctly

print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")
