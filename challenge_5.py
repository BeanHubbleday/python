# Challenge 5

import datetime
from datetime import timedelta
doby=int(input("Enter your year of birth (YYYY): "))
dobm=int(input("Enter your month of birth (MM): "))
dobd=int(input("Enter your day of birth (DD): "))
dobdd = datetime.date(doby, dobm, dobd)
today = datetime.date.today()
diff = today - dobdd
secs = diff * 86400
print("You have been alive for", diff.days, "days, which equates to", secs, "seconds!")
