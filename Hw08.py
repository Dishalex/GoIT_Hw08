from datetime import datetime, timedelta
from collections import defaultdict

employees = [{"name": "Angel", "birthdate": "6.07.2000"},
             {"name": "Mike", "birthdate": datetime(1985, 6, 30)},
             {"name": "Sandra", "birthdate": datetime(1989, 7, 7)},
             {"name": "Nik", "birthdate": datetime(1913, 7, 1)},
             {"name": "Piter", "birthdate": datetime(1990, 7, 2)},
             {"name": "Kurka", "birthdate": datetime(1970, 7, 5)}]

def get_period() -> tuple[int, int]:
    current_date = datetime.now()
    start_period = current_date + timedelta(days=5-current_date.weekday())
    return start_period.date(), (start_period + timedelta(6)).date()

start, end = get_period() # Отримання періоду винесено за межі циклу, щоб не обчислювати багато разів одне і те ж

def check_epl(list_of_emp: list) -> None:
    result = defaultdict(list)
    current_year = datetime.now().year
    for employee in list_of_emp:
        bd = employee["birthdate"]
        if not isinstance(bd, datetime):
            bd = datetime.strptime(bd, "%d.%m.%Y")
        bd = bd.date().replace(year=current_year)
        
        if start <= bd <= end:
            if bd.weekday() in (5, 6):
                result[bd + timedelta(days=(7-bd.weekday()))].append(employee["name"])
            else:
                result[bd].append(employee["name"])
    return result

if __name__ == "__main__":
    
    for key, value in sorted(check_epl(employees).items()):
        print(f'{key.strftime("%A")}', end = ': ')
        print(*value, sep=', ')
