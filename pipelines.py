from typing import List

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer

from transformers import (AddTotalNights, AddRoomTypeChange, AddIsWeekendStay,
                          AddSpecialRequestsIndicator, AddColumns)


def create_pipeline(numeric_features: List[str],
                    categorical_features: List[str], model) -> Pipeline:

    pipeline = Pipeline(steps=[
        ('add_total_nights', AddTotalNights()),
        ('add_is_weekend_stay', AddIsWeekendStay()),
        ('add_room_type_change', AddRoomTypeChange()),
        ('special_requests_more_than_1', AddSpecialRequestsIndicator()),
    ])
    additional_features = ['is_weekend_stay', 'room_type_changed',
                           'special_requests_more_than_1']

    add_columns_transformer = AddColumns(additional_features)

    numeric_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ])

    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])

    # Preprocessing pipeline
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features + ['total_nights']),
            ('cat', categorical_transformer, categorical_features),
            ('add_cols', add_columns_transformer, additional_features)
        ])

    # Create the full pipeline with preprocessing and model
    full_pipeline = Pipeline(steps=[
        ('feature_engineering', pipeline),
        ('preprocessor', preprocessor),
        ('model', model)
    ])

    return full_pipeline
