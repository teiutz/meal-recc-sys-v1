import pandas as pd
import numpy as np


def recommend_for_user(candidate_df, user_profile, k):
    filtered_df = candidate_df.copy()

    # Apply hard constraints
    for feature, required_value in user_profile["hard_filters"].items():

        if feature in filtered_df.columns:

            filtered_df = filtered_df[filtered_df[feature] == required_value]

    # Compute weighted preference score
    score = 0

    for feature, weight in user_profile["preferences"].items():

        if feature in filtered_df.columns:

            score += filtered_df[feature] * weight

    filtered_df = filtered_df.copy()

    filtered_df["score"] = score

    recommendations = filtered_df.sort_values("score", ascending=False).head(k)

    return recommendations


def show_top_k_reccs(k, candidate_df):
    recommendations = candidate_df.sort_values("score", ascending=False).head(k)

    return recommendations
