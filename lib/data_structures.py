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
    names = [food['name'] for food in spicy_foods]
    return names
names_list = get_names(spicy_foods)
print(names_list)
    

def get_spiciest_foods(spicy_foods):
    spiciest_foods = [food for food in spicy_foods if food['heat_level'] > 5]
    return spiciest_foods
spiciest_foods_list = get_spiciest_foods(spicy_foods)
print(spiciest_foods_list)
def print_spicy_foods(spicy_foods):
       for food in spicy_foods:
        heat_level_emojis = '🌶' * food['heat_level']
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emojis}")
print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
     for food in spicy_foods:
        if food['cuisine'].lower() == cuisine.lower():
            return food
     return None
cuisine = "Thai"
spicy_food = get_spicy_food_by_cuisine(spicy_foods, cuisine)
if spicy_food:
    print(spicy_food)
else:
    print(f"No spicy food found with {cuisine} cuisine.")

def print_spiciest_foods(spicy_foods):
   for food in spicy_foods:
        if food['heat_level'] > 5:
            heat_level_emojis = '🌶' * food['heat_level']
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emojis}")
print_spiciest_foods(spicy_foods)

def get_average_heat_level(spicy_foods):
    total_heat = sum(food['heat_level'] for food in spicy_foods)
    num_foods = len(spicy_foods)
    
    if num_foods == 0:
        return 0
    
    avg_heat = total_heat / num_foods
    return int(avg_heat)
avg_heat = get_average_heat_level(spicy_foods)
print(f"Average Heat Level: {avg_heat}")

def create_spicy_food(spicy_foods, spicy_food):
     spicy_foods.append(spicy_food)
     return spicy_foods
new_spicy_food = {
    "name": "Sriracha Shrimp",
    "cuisine": "Fusion",
    "heat_level": 7,
}

updated_spicy_foods = create_spicy_food(spicy_foods, spicy_food)
print(updated_spicy_foods)

