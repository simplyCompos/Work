import sys
import datetime
message = input(" ")
date = datetime.datetime.now()
print(date, message, file=sys.stderr)
