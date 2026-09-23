import pandas as pd
import numpy as np
import ast


def parse_tags(value):
    if pd.isna(value):
        return []
    if isinstance(value, list):
        return value
    return ast.literal_eval(value)


def apply_tag_mapping(
    df, mapping, parsed_col="tags_parsed", prefix=None, prefix_rules=None
):
    # Function for creating the new feature column name
    def final_col_name(feature):
        # if there are prefix rules,
        # verify if feature starts with a prefix existing in the prefix rules
        # if yes,return the column with the prefix set in `prefix_rules`
        if prefix_rules:
            for starts_with, rule_prefix in prefix_rules.items():
                if feature.startswith(starts_with):
                    return f"{rule_prefix}_{feature}"

        # if there are no prefix rules, just attach the prefix from the `prefix` parameter
        if prefix is not None:
            return f"{prefix}_{feature}"

        return feature

    # selecting the columns that will be added to the data_frame
    feature_cols = []

    for features in mapping.values():
        for f in features:
            col_name = final_col_name(f)
            feature_cols.append(col_name)

    feature_cols = sorted(set(feature_cols))

    new_feature_cols = []

    for col in feature_cols:
        if (
            col not in df.columns
        ):  # verifying if columns exist in dataframe so we don't add duplicates
            new_feature_cols.append(col)

    # adding the new columns
    if new_feature_cols:
        df = pd.concat(
            [df, pd.DataFrame(0, index=df.index, columns=new_feature_cols)], axis=1
        )

    for raw_tag, features in mapping.items():
        # if there is an empty list, don't add anything, this is for ignoring or "removing" irelevant tags
        if not features:
            continue

        mask = df[parsed_col].apply(
            lambda tags: raw_tag in tags
        )  # a series with true / false values along the rows to mark where the feature is present

        for feature in features:
            df.loc[mask, final_col_name(feature)] = 1  # applying the mask

    return df
