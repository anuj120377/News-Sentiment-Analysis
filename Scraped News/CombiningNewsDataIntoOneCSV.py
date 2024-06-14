import pandas as pd
import glob

# Specify the path where your CSV files are located
path = "Scraped News/"  # Update this path

# Use glob to get all the csv files in the folder
csv_files = glob.glob(path + "*.csv")

# List to hold the dataframes
df_list = []

# Loop through the list of csv files and read them into dataframes
for file in csv_files:
    df = pd.read_csv(file,header=None)
    df_list.append(df)

# Concatenate all the dataframes in the list
combined_df = pd.concat(df_list, ignore_index=True)

# Save the combined dataframe to a new CSV file
combined_df.to_csv("NewsData.csv", index=False)

print("CSV files have been combined successfully!")
