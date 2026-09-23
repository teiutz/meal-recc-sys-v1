from scoring import recommend_for_user


def prettify_feature(feature):
    feature = feature.replace("ingredient_has_", "contains ")
    feature = feature.replace("meal_type_is_", "")
    feature = feature.replace("cuisine_is_", "")
    feature = feature.replace("diet_is_", "")
    feature = feature.replace("cooking_is_", "")
    feature = feature.replace("duration_is_", "")
    feature = feature.replace("complexity_is_", "")
    feature = feature.replace("taste_is_", "")

    feature = feature.replace("_", " ")

    return feature.capitalize()


def explain_recommendation(recipe_row, preferences, max_reasons=5):
    matched_preferences = []
    matched_avoidances = []

    for feature, weight in preferences.items():
        if feature not in recipe_row.index:
            continue

        if recipe_row[feature] != 1:
            continue

        readable_feature = prettify_feature(feature)

        if weight > 0:
            matched_preferences.append((readable_feature, weight))
        elif weight < 0:
            matched_avoidances.append((readable_feature, weight))

    matched_preferences = sorted(matched_preferences, key=lambda x: x[1], reverse=True)
    matched_avoidances = sorted(
        matched_avoidances, key=lambda x: abs(x[1]), reverse=True
    )

    explanation = []

    for feature, weight in matched_preferences[:max_reasons]:
        explanation.append(f"Matched preference: {feature} (+{weight})")

    for feature, weight in matched_avoidances[:max_reasons]:
        explanation.append(f"Contains avoided feature: {feature} ({weight})")

    return explanation


def show_reccommendations(user, candidate_df):
    recommendations = recommend_for_user(candidate_df, user, k=10)

    for index, row in recommendations.iterrows():
        print(row["name"])
        print(explain_recommendation(row, user["preferences"]))
        print("------------------------------------------------------------")
