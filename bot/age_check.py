def chk_min(age):
    try:
        age = int(age)
        if age < 18:
            return 'young'
        elif age > 90:
            return 'old'
        else:
            return 'pass'
    except:
        return 'error'


def chk_max(age_min, age):
    try:
        age = int(age)
        if age < age_min:
            return 'smaller'
        elif age > 90:
            return 'old'
        else:
            return 'pass'
    except:
        return 'error'
