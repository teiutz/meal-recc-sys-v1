# Meal Reccommender System

This project involves the processing of a dataset in order to make it suitable as a component in a **Personalized meal recommender system**.

The dataset should model the meals inside it through structured semantic features so a recommendation score can be computed.


# The dataset

Original Dataset: https://www.kaggle.com/datasets/realalexanderwei/food-com-recipes-with-ingredients-and-tags

- over 500,000 recipes
- columns such as `name`, `description`, `ingredients`, `steps`, `tags`

# Transforming tags into feature columns

The tag values contained details about _cuisines_, _dietary properties_, _meal types_, _ingredient groups_, etc. Therefore, relevant info was extracted from them.

The tag transformation and other dataset preprocessing takes place in `preprocessing.py`

# Content-Based Recommendation

- Each recipe from the processed dataset is represented through a collection of binary semantic features.
- User profiles are represented through weighted preferences associated with an identical semantic feature space.
- The recommendation process evaluates how well a recipe aligns with a user profile by **analyzing the overlap between recipe features and user preferences**.


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
