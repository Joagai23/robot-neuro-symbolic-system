import pandas as pd

class ReasoningSystem:
    '''
    Class to perform queries and infer affordance probabilities
    '''

    def __init__(self):
        self.df = pd.read_csv("./src/reasoning_system/AffordanceReasoningBase.csv")

    def __get_probability(self, df:pd.DataFrame):
        '''
        Calculate the probability of a column value in a given dataframe.
        '''
        affordance_prob = {}
        for column in df.columns[12:]:
            affordance = df[column].value_counts(normalize=True)
            for i in affordance.index:
                if i:
                    affordance_prob[column] = affordance[i]

        return affordance_prob
    
    def __filter_dataframe(self, columns:list[str], column_values:list[str]) -> pd.DataFrame:
        '''
        Given two lists of the same lenght containing the column names and its values,
        return a dataframe containing such values for the given columns.
        '''
        #print(columns, column_values)
        filtered_df = pd.DataFrame(self.df)
        for column, value in zip(columns, column_values):
            filtered_df = filtered_df[filtered_df[column] == value]
        return filtered_df
    
    def __process_caption(self, caption:str) -> tuple[list[str], list[str]]:
        '''
        Match caption with static values to determine its perception properties
        '''
        columns, column_values = [], []
        caption = str.lower(caption)
        for column in self.df.columns[1:12]:
            for value in self.df[column].unique():
                value = str(value)
                if str.lower(value) in caption:
                    columns.append(column)
                    column_values.append(value)

        return columns, column_values

    def infer_affordances(self, caption:str):
        '''
            1. Process caption to get properties
            2. Filter dataframe to obtain entries with matching properties
            3. Calculate probabilities of affordances
        '''
        columns, column_values = self.__process_caption(caption)
        filtered_df = self.__filter_dataframe(columns, column_values)
        print(self.__get_probability(filtered_df))
        return list(self.__get_probability(filtered_df))