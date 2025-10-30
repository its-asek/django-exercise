def check_pesel(pesel: str) -> str:
    if len(pesel) != 11:
        return "That is not a correct PESEL"

    yy = int(pesel[:2])
    mm = int(pesel[2:4])
    dd = int(pesel[4:6])
    pppp = int(pesel[6:10])
    k = int(pesel[10])

    year = yy
    if 80 <= mm <= 99:
        year += 1800
    elif 0 <= mm <= 19:
        year += 1900
    elif 20 <= mm <= 39:
        year += 2000
    elif 40 <= mm <= 59:
        year += 2100
    elif 60 <= mm <= 79:
        year += 2200

    month_map = {
        1: "Jenuary",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
    }

    month_mm = mm % 20

    day = dd

    gender = "female" if pppp % 2 == 0 else "male"

    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    control_number = sum(int(pesel[i]) * weights[i] for i in range(10)) % 10

    if control_number != k:
        return "Number has right amount of digits, but it is not a PESEL, because control number is not right.\n"
    if day > 31:
        return "Number has right amount of digits, but it is not a PESEL, because day of birth is not right.\n"
    if month_mm < 1 or month_mm > 12:
        return "Number has right amount of digits, but it is not a PESEL, because month number is not right.\n"

    return f"\n{pesel}\n{day} {month_map[month_mm]} {year}\n{gender}\nControl number: {control_number}"
