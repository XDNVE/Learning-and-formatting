#Date and time formatting
from datetime import datetime
dt = datetime(2020, 9, 26, 4, 5, 6)
print('{:{date} {time}}'.format(dt, date='%Y-%m-%d', time='%H:%M:%S'))
print('{:{date} {time}}'.format(dt, date='%G-%m-%d', time='%H:%M:%S')) # %Y and %G has the same effetc prints full Year
print('{:{dfmt} {tfmt}}'.format(dt, dfmt='%d-%m-%Y', tfmt='%H:%M:%S%p'))
print('{:{dfmt} {tfmt}}'.format(dt, dfmt='%d-%m-%Y', tfmt='%H:%M:%S')) #k and H prints hours but k does not add 0 before Hour
print('{:{dfmt} {tfmt}}'.format(dt, dfmt='%d-%m-%Y', tfmt='%H:%M:%u')) #u and S prints seconds but u does not add 0 before Second
print('{:{dfmt} {tfmt}}'.format(dt, dfmt='%d-%m-%Y', tfmt='%H:%M:%w')) # %w and S both prints seconds
print('{:{dfmt} {tfmt}}'.format(dt, dfmt='%d-%m-%Y', tfmt='%H:%M:%S')) #l and H prints hours
print('{:{dfmt} {tfmt}}'.format(dt, dfmt='%d-%m-%Y', tfmt='%I:%M:%S')) # %I and H prints hours but l adds space before Hour
print('{:{dfmt} {tfmt}}'.format(dt, dfmt='%e-%m-%Y', tfmt='%H:%M:%S')) # %d and %e has the same effetc prints Date(26)
print('{:{dfmt} {tfmt}}'.format(dt, dfmt='%d-%h-%Y', tfmt='%H:%M:%S'))
print('{:{dfmt} {tfmt}}'.format(dt, dfmt='%d-%h-%y', tfmt='%H:%M:%S')) 
print('{:{dfmt} {tfmt}}'.format(dt, dfmt='%d-%h-%g', tfmt='%H:%M:%S')) # %y and %g and %C has prints (last 2 digits of year)
print('{:{dfmt} {tfmt}}'.format(dt, dfmt='%d-%b-%y', tfmt='%H:%M:%S')) # %b and %h has prints month name
print('{:{dfmt} {tfmt}}'.format(dt, dfmt='%d-%B-%y', tfmt='%H:%M:%S')) # B prints full month name
print('{:{day} {dfmt} {tfmt}}'.format(dt, day='%A' ,dfmt='%d-%h-%y', tfmt='%H:%M:%S')) # a prints day of the week
print('{:{day} {dfmt} {tfmt}}'.format(dt, day='%a' ,dfmt='%d-%h-%y', tfmt='%H:%M:%S')) #a prints day of the week 3Charecters
print('{:{dfmt} {tfmt}}'.format(dt, dfmt='%x', tfmt='%H:%M:%S'))       # %D and %x prints full Date in format(MM/DD/YY)
print('{:{dfmt} {tfmt}}'.format(dt, dfmt='%D', tfmt='%H:%M:%S'))       # %D and %x prints full Date in format(MM/DD/YY)
print('{:{dfmt} {tfmt}}'.format(dt, dfmt='%F', tfmt='%H:%M:%S'))       # D prints full Date in format(YYYY-MM-DD)
print('{:{day}}'.format(dt, day='%c'))                                 # %c prints complete date and time
print('{:{day}}'.format(dt, day='%P'))                                 # %p says am pm
print('{:{day}}'.format(dt, day='%p'))                                 # %p says Am Pm
print('{:{day}}'.format(dt, day='%r'))                                 # %r prints complete time with big AM PM
print('{:{day}}'.format(dt, day='%R'))                                 # %r prints time(HH:MM)
print('{:{day}}'.format(dt, day='%X'))
print('{:{day}}'.format(dt, day='%T'))                                 # %r and %X prints time(HH:MM:SS)

print('{:{day}}'.format(dt, day='%j'))
print('{:{day}}'.format(dt, day='%s'))
print('{:{day}}'.format(dt, day='%U'))
print('{:{day}}'.format(dt, day='%V'))
