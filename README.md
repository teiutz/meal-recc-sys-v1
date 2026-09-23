# Meal Reccommender System

This project involves the processing of a dataset in order to make it suitable as a component in a **Personalized Meal Recommending System**.

The dataset should model the meals inside it through structured semantic features so a recommendation score can be computed.


# The dataset

Original Dataset: https://www.kaggle.com/datasets/realalexanderwei/food-com-recipes-with-ingredients-and-tags

- over 500,000 recipes
- columns such as `name`, `description`, `ingredients`, `steps`, `tags`

# Transforming tags into feature columns

The tag values contained details about cuisines, dietary properties, meal types, ingredient groups, cooking methods, etc. Therefore, relevant info was extracted from them.

Instead of using the original tags directly, they are mapped into a smaller and more consistent semantic feature space.

Some examples of the resulting features are:

`ingredient_has_chicken`
`ingredient_has_tofu`
`meal_type_is_breakfast`
`meal_type_is_complete_meal`
`cuisine_is_italian`
`cuisine_is_thai`
`diet_is_high_protein`
`diet_is_vegan`
`cooking_is_grilled`
`duration_is_quick_meal`

A recipe can contain multiple features at the same time.

The tag transformation and other dataset preprocessing takes place in preprocessing.py, while the mappings used to construct the feature space are defined in mappings.py.

# Content-Based Recommendation

- Each recipe from the processed dataset is represented through a collection of binary semantic features.
- User profiles are represented through weighted preferences associated with an identical semantic feature space.
- The recommendation process evaluates how well a recipe aligns with a user profile by **analyzing the overlap between recipe features and user preferences**.
- Positive weights represent preferences, while negative weights can be used for features the user dislikes.
- Dietary restrictions can be applied as hard constraints before the recommendation score is calculated.

# Recommendation Score

- After applying the required dietary constraints, each remaining recipe receives a score based on its features and the corresponding weights from the user profile.

Conceptually, the score is computed as:
`recipe score = sum(recipe feature × user preference weight)`

- Recipes with a larger positive overlap with the user's preferences therefore receive higher scores.
- The scoring and ranking logic can be found in `scoring.py`.


# Explainable Recommendations

- Since the recommendation score is based on explicit semantic features, the system can also show which preferences contributed to a recommendation.

- For example, a recipe could be recommended because it matches preferences such as:
`high protein`,
`chicken`,
`grilled`,
`mediterranean`,
`quick meal`

- The explanation logic is implemented in `explain_reccs.py`.

# Notebooks

- The notebooks document the development and experimentation process from the original dataset to the final recommendation results.

  - `feature_engineering_and_recommendations.ipynb` contains the earlier feature engineering and recommendation experiments.

  - `final_dataset_statistics.ipynb` explores the resulting dataset and feature distributions.

  - `final_meal_recc_sys.ipynb` contains the final end-to-end version of the recommendation prototype and example recommendation results.

# File Structure
```
├── 📁 data
├── 📁 notebooks
│   ├── 📄 feature_engineering_and_recommendations.ipynb
│   ├── 📄 final_dataset_statistics.ipynb
│   └── 📄 final_meal_recc_sys.ipynb
├── 📁 outputs
├── 📁 src
│   ├── 🐍 explain_reccs.py
│   ├── 🐍 generate_profile.py
│   ├── 🐍 mappings.py
│   ├── 🐍 preprocessing.py
│   ├── 🐍 profiles.py
│   ├── 🐍 quiz.py
│   └── 🐍 scoring.py
├── ⚙️ .gitignore
├── 📝 README.md
└── 📄 requirements.txt
```




The main components inside `src` are:

- `mappings.py` contains the mappings used to transform the original Food.com tags into the semantic feature space.

- `preprocessing.py` contains the functions used to parse, clean and transform the original dataset using those mappings.

- `profiles.py` contains predefined user profiles used for testing different recommendation scenarios.

- `quiz.py` contains the questions and preference options used to build a user profile.

- `generate_profile.py` transforms the answers from the quiz into the weighted user preference representation expected by the recommendation system.

- `scoring.py` applies constraints, computes recipe scores and ranks recipes according to a user profile.

- `explain_reccs.py` uses the matched recipe and user features to provide an explanation for the generated recommendations.

---

The general flow of the system is:
```
Original Food.com Dataset
        ↓
mappings.py
        ↓
preprocessing.py
        ↓
Processed Recipe Feature Space
        ↓
quiz.py
        ↓
generate_profile.py
        ↓
Weighted User Profile
        ↓
scoring.py
        ↓
Ranked Recommendations
        ↓
explain_reccs.py
        ↓
Recommendations + Explanations
```

`profiles.py` provides predefined user profiles that can be used instead of the quiz-generated profiles when testing the recommendation system.


The notebooks document this process from the original dataset to the final recommendation results. For the complete end-to-end development and recommendation workflow, see notebooks/final_meal_recc_sys.ipynb.


# Running the Project

Install the required dependencies with:
```bash
pip install -r requirements.txt
```
The notebooks can be run using **Jupyter Notebook** or **JupyterLab**.

The dataset itself is not stored in the repository and needs to be downloaded separately from the source linked above.

