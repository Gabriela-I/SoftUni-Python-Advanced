number_of_cars = int(input())
cars_in_parking_lot = set()
for _ in range(number_of_cars):
    command, number = input().split(', ')
    if command == 'IN':
        cars_in_parking_lot.add(number)
    else:
        cars_in_parking_lot.remove(number)
if not cars_in_parking_lot:
    print("Parking Lot is Empty")
else:
    for cars in cars_in_parking_lot:
        print(cars)