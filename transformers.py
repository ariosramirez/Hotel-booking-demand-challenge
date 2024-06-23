from sklearn.base import BaseEstimator, TransformerMixin


class AddTotalNights(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X = X.copy()
        X['total_nights'] = X['stays_in_week_nights'] + X['stays_in_weekend_nights']
        return X


class AddRoomTypeChange(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X = X.copy()
        X['room_type_changed'] = X['reserved_room_type'] != X['assigned_room_type']
        return X


class AddIsWeekendStay(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X = X.copy()
        X['is_weekend_stay'] = X['stays_in_weekend_nights'] > 0
        return X


class AddSpecialRequestsIndicator(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X = X.copy()
        X['special_requests_more_than_1'] = X['total_of_special_requests'] > 1
        return X


class AddColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        return X[self.columns].copy()
