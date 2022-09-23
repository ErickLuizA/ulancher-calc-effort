from datetime import datetime


def handle_calc(time, now=datetime.now()):
    time = time.strip()

    has_start = time.find("s=") != -1
    has_end = time.find("e=") != -1

    is_number = time.isdigit()

    result = 0

    if is_number:
        result = int(time) / 60

    if has_start and not has_end:
        start = time.split("s=")[1]

        if not len(start) == 5:
            return result

        start = datetime.strptime(start, "%H:%M")

        minutes = (now - start).seconds / 60

        result = minutes / 60

    if has_start and has_end:
        start = time.split("s=")[1].split("e=")[0].strip()
        end = time.split("e=")[1]

        if not len(start) == 5 or not len(end) == 5:
            return result

        start = datetime.strptime(start, "%H:%M")
        end = datetime.strptime(end, "%H:%M")

        minutes = (end - start).seconds / 60

        result = minutes / 60

    return round(result, 2)
