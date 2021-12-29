car_disc = {
    "color": "Red",
    "model": "Mustang",
    "year":1964
}
print(car_disc.get("color"))

car_disc["seats"] = 4

car_disc["year"] = 2018

print(car_disc)

for key in car_disc:
    print(key)
    print(car_disc[key])

new_car_disc = car_disc

new_car_disc = car_disc.copy()

for key in sorted(car_disc):
    print(key)
    print(car_disc[key])

my_car = {
    "car1": {
        "model" : "chiron"
    },
    "car2" : {
        "model" : "hurron"
    }
}
print (my_car)

