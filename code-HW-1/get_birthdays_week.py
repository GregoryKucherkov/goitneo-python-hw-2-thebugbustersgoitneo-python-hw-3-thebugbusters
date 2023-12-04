from collections import defaultdict

from datetime import datetime

week = ('Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
        'Sunday' 
        )

def get_birthdays_per_week(users):
    
    birthday_list = defaultdict(list)
    today = datetime.today().date() 

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()  # date type conversion
        birthday_this_year = birthday.replace(year=today.year) 
         

        delta_days = (birthday_this_year - today).days

        if delta_days <= 7:
            day = week[birthday.weekday()]
            if birthday.weekday() >= 5: 
                birthday_list['Monday'].append(name)
            else:
                birthday_list[day].append(name)    
            
        elif birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)

        if birthday.weekday() == 5 or birthday.weekday() == 6:
            pass

    for day, names in birthday_list.items():
        print(f"{day}: {', '.join(names)}")   
    

users = [{'name': 'Rikardo', 'birthday': datetime(2023, 12, 2)}, 
         {'name': 'Huan', 'birthday': datetime(2023, 12, 10)},
        {'name': 'Fedir', 'birthday': datetime(2023, 11, 17)} ] 
get_birthdays_per_week(users)






   
