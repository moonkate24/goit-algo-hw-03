import random

def get_numbers_ticket(minimum, maximum, quantity):
    if not (1 <= minimum <= maximum <= 1000 and quantity <= maximum - minimum + 1):
        return []
    
    numbers = set()
    while len(numbers) < quantity:
        numbers.add(random.randint(minimum, maximum))
    
    return sorted(list(numbers))


lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Your lottery numbers:", lottery_numbers)
