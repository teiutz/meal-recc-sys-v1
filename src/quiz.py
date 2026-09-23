def ask_choice(question, options, allow_multiple=True):
    print("\n" + question)

    for key, label in options.items():
        print(f"{key}. {label}")

    answer = input("\nYour choice: ").strip()

    if allow_multiple:
        return [item.strip() for item in answer.split(",") if item.strip() in options]
    else:
        return answer if answer in options else None


def build_profile_from_quiz():
    profile = {"hard_filters": {}, "preferences": {}}

    # 1. Goal
    goal_options = {
        "1": "Lose weight",
        "2": "Build muscle",
        "3": "Eat healthier",
        "4": "Quick and easy meals",
    }

    goal = ask_choice("What is your main goal?", goal_options, allow_multiple=False)

    if goal == "1":
        profile["preferences"]["diet_is_low_calorie"] = 8
        profile["preferences"]["diet_is_low_fat"] = 5
        profile["preferences"]["meal_type_is_dessert"] = -8

    elif goal == "2":
        profile["preferences"]["diet_is_high_protein"] = 10
        profile["preferences"]["meal_type_is_complete_meal"] = 6
        profile["preferences"]["diet_is_low_protein"] = -8

    elif goal == "3":
        profile["preferences"]["diet_is_healthy"] = 8
        profile["preferences"]["ingredient_has_vegetables"] = 6
        profile["preferences"]["cooking_is_fried"] = -6

    elif goal == "4":
        profile["preferences"]["duration_is_quick_meal"] = 8
        profile["preferences"]["complexity_is_easy"] = 6
        profile["preferences"]["duration_is_long_cook"] = -8

    # 2. Dietary restrictions
    restriction_options = {
        "1": "Vegetarian",
        "2": "Vegan",
        "3": "Gluten-free",
        "4": "Dairy-free",
        "5": "Low sodium",
        "6": "None",
    }

    restrictions = ask_choice(
        "Do you have any dietary restrictions? Choose one or more separated by commas.",
        restriction_options,
        allow_multiple=True,
    )

    if not isinstance(restrictions, list):
        restrictions = []

    if "1" in restrictions:
        profile["hard_filters"]["diet_is_vegetarian"] = 1

    if "2" in restrictions:
        profile["hard_filters"]["diet_is_vegan"] = 1

    if "3" in restrictions:
        profile["hard_filters"]["diet_is_gluten_free"] = 1

    if "4" in restrictions:
        profile["hard_filters"]["diet_is_dairy_free"] = 1

    if "5" in restrictions:
        profile["hard_filters"]["diet_is_low_sodium"] = 1

    # 3. Preferred cuisines
    cuisine_options = {
        "1": "Mediterranean",
        "2": "Italian",
        "3": "Mexican",
        "4": "Asian",
        "5": "Indian",
        "6": "Middle Eastern",
    }

    cuisines = ask_choice(
        "Which cuisines do you usually like? Choose one or more separated by commas.",
        cuisine_options,
        allow_multiple=True,
    )
    if not isinstance(cuisines, list):
        cuisines = []

    cuisine_mapping = {
        "1": "cuisine_is_mediterranean",
        "2": "cuisine_is_italian",
        "3": "cuisine_is_mexican",
        "4": "cuisine_is_asian",
        "5": "cuisine_is_indian",
        "6": "cuisine_is_middle_eastern",
    }

    for choice in cuisines:
        profile["preferences"][cuisine_mapping[choice]] = 6

    # 4. Preferred proteins
    protein_options = {
        "1": "Chicken",
        "2": "Beef",
        "3": "Fish",
        "4": "Seafood",
        "5": "Eggs",
        "6": "Tofu / legumes",
    }

    proteins = ask_choice(
        "Which protein sources do you prefer? Choose one or more separated by commas.",
        protein_options,
        allow_multiple=True,
    )
    if not isinstance(proteins, list):
        proteins = []

    protein_mapping = {
        "1": "ingredient_has_chicken",
        "2": "ingredient_has_beef",
        "3": "ingredient_has_fish",
        "4": "ingredient_has_seafood",
        "5": "ingredient_has_eggs",
        "6": "ingredient_has_legumes",
    }

    for choice in proteins:
        profile["preferences"][protein_mapping[choice]] = 5

    # 5. Avoided foods
    avoid_options = {
        "1": "Pork",
        "2": "Seafood",
        "3": "Dairy",
        "4": "Desserts",
        "5": "Fried food",
        "6": "None",
    }

    avoided = ask_choice(
        "Are there foods you prefer to avoid? Choose one or more separated by commas.",
        avoid_options,
        allow_multiple=True,
    )

    avoid_mapping = {
        "1": "ingredient_has_pork",
        "2": "ingredient_has_seafood",
        "3": "ingredient_has_dairy",
        "4": "meal_type_is_dessert",
        "5": "cooking_is_fried",
    }

    for choice in avoided:
        if choice in avoid_mapping:
            profile["preferences"][avoid_mapping[choice]] = -8

    return profile
