#             self.id, "Вы пока что слишком молоды для нашего бота. До свидания!."
#             self.id, "Вам бы на покой уже, а не в боте сидеть. До свидания!."
#         )

def chk_min(age):
    try:
        age = int(age)
        if age < 18:
            return 'young'
        elif age > 90:
            return 'old'
        else: return 'pass'
    except:
        return 'error'

def chk_max(age_min, age):
    try:
        age = int(age)
        if age < age_min:
            return 'smaller'
        elif age > 90:
            return 'old'
        else: return 'pass'
    except:
        return 'error'