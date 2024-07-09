import pandas as pd

def load_data():
    '''
    Read and convert csv jar data into dataframes.
    '''
    jars_df = pd.read_csv('./data/csv/jars.csv')
    closures_df = pd.read_csv('./data/csv/jar_closures.csv')

    return jars_df, closures_df

def get_probability(df:pd.DataFrame, column:str):
    '''
    Calculate the probability of all column values in a given dataframe.
    '''
    return df[column].value_counts(normalize=True)

def filter_dataframe(df:pd.DataFrame, columns:[str], column_value:[str]):
    '''
    Given two lists of the same lenght containing the column names and its values,
    return a dataframe containing such values for the given columns.
    '''
    for column, value in zip(columns, column_value):
        df = df[df[column] == value]
    return df

def test():
    jars_df, jar_closures_df = load_data()
    # Apply material and color filter: { Material: Glass, Color: White }
    filter_df = filter_dataframe(jars_df, ["Material", "Color", "Capacity"], ["Glass", "White", "<= 250 mL"])
    finish_prob = get_probability(filter_df, "Finish")
    print(filter_df)
    print(finish_prob)

if __name__ == "__main__":
    test()