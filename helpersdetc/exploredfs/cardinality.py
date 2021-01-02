import pandas as pd
# ---------------------------------------------------------------------------------------

from os import path

test_df = pd.read_csv('helpersdetc/titanic.csv')

def rank_cardinality(df):
    """
    Takes a dataframe and returns it's column names 
    listed in order of increasing cardinality
    Params:
        df (pandas DataFrame)
    
    Returns:
        List of df column names from lowest cardinality to highest cardinality.
    """

    cat_columns = df.describe(exclude='number').columns
    perc_unique = {}
    for col in cat_columns:
        pu = df[col].nunique() / df.shape[0]
        perc_unique.update({col: pu})

    sorted_pu = sorted(perc_unique.values())
    sorted_names = []
    for pu in sorted_pu:
        sorted_names.append([col for col, perc_unq in perc_unique.items() if perc_unq == pu][0])
    
    return sorted_names

    



def cardinality_report(df):
    """
    Takes a dataframe and returns a report on the cardinality
    of categorical columns within the dataframe
    Params:
        df (pandas DataFrame)
    
    Returns:
        A series of 4 Print Statements for each Categorical Column
        identified in the dataframe separated by a newline
        The ouptut is ordered from lowest cardinality to 
        highest cardinality variables
    """
    # Get only categorical features from DF
    # Apply Ranking Function
    ranked_categoricals = rank_cardinality(df)
    
    # Evaluate cardinality qualities for each feature
    for i, col in enumerate(ranked_categoricals):
        print('-------------')
        print(f"COLUMN: {col}")
        print(f"nUnique: {df[col].nunique()}")
        print("--- TOP 5 ---")
        print(df[col].value_counts().nlargest(5))
        print('\n')

cardinality_report(test_df)