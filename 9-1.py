class Car:
    pass

    def __init__(self, color: str, count_passenger_seats: int, is_baby_seat: bool):
        self.color = color
        self.count_passenger_seats = count_passenger_seats
        self.is_baby_seat = is_baby_seat
        self.is_busy = False

    def __str__(self):
        is_baby_seat = 'with one baby seat' if self.is_baby_seat else 'without baby seat'
        return f'Your choice is car of {self.color} color with {self.count_passenger_seats} seats {is_baby_seat}.'


BMW = Car('black', 5, False)
Mazda = Car('red', 4, True)
Audi = Car('green', 5, False)

i = input('Type car model:')
if i == 'BMW':
    print(BMW)
elif i == 'Mazda':
    print(Mazda)
elif i == 'Audi':
    print(Audi)
else:
    print(Car(input('Castom choise!!!'  'Color:'), int(input('Seats:')),
          is_baby_seat=True if input('Baby seat, type Y if needs:') == 'Y' else False))
