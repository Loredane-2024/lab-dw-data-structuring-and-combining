import pandas as pd

def initial_format (df: pd.DataFrame):
    df.columns = pd.Series(df.columns).apply(lambda col: col.lower())
    df.columns = [col.replace(" ", "_") for col in df.columns]
    #df.st.columns =["state"]
    df = df.rename(columns={"st": "state"})
    return df


def inconsistent_values (df: pd.DataFrame):
    # Gender column contains various inconsistent values such as "F", "M", "Femal", "Male", "female", which need to be standardized, for example, to "M" and "F".
    df["gender"] = df["gender"].replace({"male": "M","Male": "M", "Femal": "F", "female": "F"})

    #- State abbreviations be can replaced with its full name, for example "AZ": "Arizona", "Cali": "California", "WA": "Washington"
    df["state"] = df["state"].replace({"AZ": "Arizona","WA": "Washington", "Cali": "California"})

    #In education, "Bachelors" could be replaced by "Bachelor"
    df["education"] = df["education"].replace({"Bachelors": "Bachelor"})

    #In Customer Lifetime Value, delete the `%` character
    df["customer_lifetime_value"] = df["customer_lifetime_value"].str.replace("%", "")

    #In vehicle class, "Sports Car", "Luxury SUV" and "Luxury Car" could be replaced by "Luxury"
    df["vehicle_class"] = df["vehicle_class"].replace({"Luxury SUV": "Luxury","Luxury Car": "Luxury"})
    
    return df


def change_dtype (df: pd.DataFrame):
    df["customer_lifetime_value"] = df["customer_lifetime_value"].astype(float)

    df["number_of_open_complaints"] = df["number_of_open_complaints"].apply (lambda x: x.split("/")[1]if isinstance(x, str) else x)

    df["number_of_open_complaints"] = df["number_of_open_complaints"].astype(float)

    return df


def drop_all (df: pd.DataFrame):
    df= df.dropna (how = "all")
    return df


def  fill_nullvalues (df: pd.DataFrame):
    # Find the most frequent value in the Gender column
    most_frequent_value = df['gender'].mode()[0]

    # Fill missing values with the most frequent value
    df['gender'] = df['gender'].fillna(most_frequent_value)

    #Backward-fill null values in the customer_lifetime_value column with the mean
    df.customer_lifetime_value =df.customer_lifetime_value.fillna(df.customer_lifetime_value.mean())

    return df


def convert_float_columns(df: pd.DataFrame):
   float_columns = df.select_dtypes(include=['float64']).columns
   for column in float_columns:
      df[column] = df[column].astype(int)
    
   return df

#convert_float_columns (df)


def reset_index_new_df (df: pd.DataFrame):
    df_without_duplicates = df.copy()
    df_without_duplicates = df.drop_duplicates()
    df_without_duplicates.reset_index()
    return df_without_duplicates


