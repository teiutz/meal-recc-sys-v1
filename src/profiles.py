# USER #1
gym_user = {
    "hard_filters": {},
    "preferences": {
        "diet_is_high_protein": 3,
        "ingredient_has_chicken": 2,
        "ingredient_has_beef": 2,
        "cuisine_is_mexican": 4,
        "meal_type_is_complete_meal": 2,
        "meal_type_is_dessert": -5,
    },
}


# USER #2
vegan_student = {
    "hard_filters": {"diet_is_vegan": 1},
    "preferences": {
        "ingredient_has_tofu": 9,
        "ingredient_has_legumes": 8,
        "ingredient_has_vegetables": 10,
        "cuisine_is_asian": 3,
        "duration_is_quick_meal": 4,
        "complexity_is_budget_friendly": 4,
    },
}


# USER #3
low_sodium_user = {
    "hard_filters": {"diet_is_low_sodium": 1},
    "preferences": {
        "meal_type_is_complete_meal": 3,
        "diet_is_low_calorie": 6,
        "diet_is_low_fat": 5,
        "ingredient_has_chicken": 3,
        "diet_is_healthy": 9,
        "meal_type_is_soup": 2,
        "meal_type_is_salad": 4,
        "ingredient_has_vegetables": 5,
        "cuisine_is_mediterranean": 4,
        "cuisine_is_greek": 3,
        # dislikes
        "cooking_is_fried": -8,
    },
}


# USER #4
gf_muscle_mass = {
    "hard_filters": {"diet_is_gluten_free": 1},
    "preferences": {
        "diet_is_high_protein": 3,
        "ingredient_has_rice": 2,
        "ingredient_has_potatoes": 2,
        "meal_type_is_complete_meal": 2,
        "meal_type_is_dessert": -3,
    },
}


# USER #5
gourmand_weight_loss = {
    "hard_filters": {"diet_is_healthy": 1},
    "preferences": {
        "diet_is_low_calorie": 3,
        "taste_is_savory": 3,
        "cuisine_is_french": 2,
        "cuisine_is_italian": 2,
        "ingredient_has_mushrooms": 2,
        "ingredient_has_cheese": 1,
        "meal_type_is_dessert": -2,
    },
}
