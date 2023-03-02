import datetime
user_input = input(
    "Enter your Goal and a Date for the Countdown separated by colon\n")
input_list = user_input.split(':')

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.datetime.today()

countdown = deadline_date - today_date
print(f"{countdown.days} Days left to {goal}\n")
