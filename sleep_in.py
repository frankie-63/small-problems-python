print('Please input day of week from Capital letter:')
weekday_input = input()
print('Please input is it vacation today or not (Yes or No):')
vacation_input = input()

if weekday_input == 'Saturday' or 'Sunday':
    weekday = False
else:
    weekday = True

if vacation_input == 'Yes':
    vacation = True
else:
    vacation = False


def sleep_in(w, v):
    if not w or v:
        return True
    else:
        return False


print('You may sleep today - ', sleep_in(weekday, vacation))
