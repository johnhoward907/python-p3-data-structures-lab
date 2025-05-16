spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    spiciest=[]
    for food in spicy_foods:
        if food["heat_level"] > 5:
            spiciest.append(food)
            return spiciest

def print_spicy_foods(spicy_foods):
    for food in  spicy_foods:
        name= food["name"]
        cuisine=food["cuisine"]
        heat= "🌶" *food["heat_level"]
        print (f"{name} ({cuisine}) | Heat Level: {heat}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
             return food

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
         name= food["name"]
         cuisine=food["cuisine"]
         heat= "🌶" *food["heat_level"]
         if food["heat_level"] > 5:
             print (f"{name} ({cuisine}) | Heat Level: {heat}")


def get_average_heat_level(spicy_foods):
    total_heat=0
    for food in spicy_foods:
        total_heat+=food["heat_level"]
    average = total_heat//len(spicy_foods)
    return average

def create_spicy_food(spicy_foods, new_spicy_food):
    spicy_foods.append(new_spicy_food)
    return spicy_foods
