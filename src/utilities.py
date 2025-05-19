from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OrdinalEncoder, PowerTransformer
from category_encoders import TargetEncoder

def CustomColumnTransformer(ordinalEncodingColumns, targetEncodingColumns, transformingColumns):
    return ColumnTransformer(
    [
        (
            'ordinalEncoding',
            OrdinalEncoder(
                categories=list(ordinalEncodingColumns.values()),
                handle_unknown='use_encoded_value',
                unknown_value=-1
            ),
            list(ordinalEncodingColumns.keys())
        ),
        (
            'targetEncoding',
           TargetEncoder(),
            targetEncodingColumns
        ),
        ('transformation',PowerTransformer(method='box-cox', standardize=True), transformingColumns)
    ],
    remainder='passthrough'
)