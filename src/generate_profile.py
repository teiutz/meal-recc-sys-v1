from explain_reccs import show_reccommendations
from quiz import ask_choice, build_profile_from_quiz
import pandas as pd

candidate_df = pd.read_csv("notebooks/datasets/v1_recipe_dataset.csv")

quiz_user = build_profile_from_quiz()

# recommendations = recommend_for_user(
#     candidate_df=candidate_df, user_profile=quiz_user, k=20
# )

show_reccommendations(quiz_user, candidate_df)
