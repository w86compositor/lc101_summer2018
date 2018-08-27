week = ["Sunday", "Monday", "Tuesday",
        "Wednesday", "Thursday", "Friday", "Saturday"]

vac_starts = "Saturday"
vac_starts.strip().capitalize()
duration = 23


if any(vac_starts in s for s in week) and type(duration) == int:
    end_of_vacation = (week.index(vac_starts) + duration) % 7
    print("you are coming back from vacation on", week[end_of_vacation])
else:
    print("Please enter a valid day of the calendar and check if you have entered a valid number")


# This first implementation was not correct completely
# for day in week:
#     if vac_starts == day and type(duration) == int:
#         print("yes it does, the day is:", day)
#         print("number of days:", duration)
#     else:
#         print("What the heck is this")
# print("Me cago en tu madre")

# if (vac_starts == day and type(duration) == int):
#     print("yes")
#     end_of_vacation = (week.index(vac_starts) + duration) % 7
#     print("you are coming back from vacation on", week[end_of_vacation])
#     break
# else:
#     print("Please enter a valid day of the calendar")
#     print("Please enter also a valid number")
#     break
