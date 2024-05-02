quarterly_sickdays_2024 = [45, 55, 68, 34]
days_in_2024 = 366

sick_days = 0
for sum in quarterly_sickdays_2024:
    sick_days += sum

print("Frank was sick for {} days".format(sick_days))
print("Frank danced for {} days".format(days_in_2024 - sick_days))
if sick_days > 100:
    print("Frank, what's wrong with you man? Are you dying? Or is it that you don't like dancing anymore?")

