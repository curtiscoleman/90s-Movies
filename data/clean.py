import os

#Get current working directory
cwd = os.getcwd()

#Construct a path to the zip file in the subdirectory 'data'
file_path = os.path.join(cwd, 'data', 'movies.csv.zip')
import zipfile
import pandas as pd

# Open the zip file and extract the CSV file
with zipfile.ZipFile(file_path, 'r') as zip_file:
    zip_file.extractall()

# Read the CSV file into a pandas DataFrame
movies_df = pd.read_csv('./data/movies.csv')

# Display the first few rows of the DataFrame
#This list provides a reference for what will be referenced within the code to extract 
#the necessary data to answer the question.
movies_df = pd.read_csv(file_path)
movies_df.columns
movies_df.shape
movies_df.info()
movies_df.isnull().sum().sort_values(ascending=False)
movies_df.head()
#Dropping all of the unnecessary columns in the original dataset
movies_df.drop(['rating', 'released', 'writer', 'star', 'country', 'budget', 'gross', 'company', 'runtime'], axis=1, inplace=True )

#Here I am removing any items with null values from the columns so that the data isnt't skewed
movies_df.dropna(subset=['name', 'genre', 'year', 'score', 'votes', 'director'], inplace=True)
