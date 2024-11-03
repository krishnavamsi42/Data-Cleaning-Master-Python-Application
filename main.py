# This is a data cleaning application

"""
Please create a python application that can take datasets and clean the data
- It should ask for datasets path and name
- it should check number of duplicats and remove all the duplicates 
- it should keep a copy of all the duplicates
- it should check for missing values 
- if any column that is numeric it should replace nulls with mean else it should drop that rows
- at end it should save the data as clean data and also return 
- duplicates records, clean_data 
"""

#importing dependencies
import pandas as pd
import numpy as np
import time
import openpyxl
import xlrd
import os
import random


def data_cleaning_master(data_path,data_name):
    
    print('Thank you for giving the details!')

    sec=random.randint(1,4)    #generating random number

    #print delay message
    print(f'please wait for{sec} seconds!  checking file path')
    time.sleep(sec)

        #checking the file type
    if data_path.endswith('.csv'):
        print("Dataset is a csv.")
        data=pd.read_csv(data_path,encoding_errors='ignore')


    elif data_path.endswith('.xlsx'):
        print('Dataset is excel file')
        data=pd.read_excel(data_path)

    else:
        print('Unknown file')
        return  

    #print delay message
    sec=random.randint(1,4)
    print(f'please wait for{sec} seconds!  checking total columns and rows')
    time.sleep(sec)

    #showing no. of records
    print(f"Dataset contain total rows:{data.shape[0]}\n Total columns:{data.shape[1]}")                          
            
    #start cleaning

    #print delay message
    sec=random.randint(1,4)
    print(f'please wait for{sec} seconds!  checking total duplicates')
    time.sleep(sec)

    duplicates=data.duplicated()
    total_duplicates=data.duplicated().sum()

    print(f"dataset has total duplicate records:{total_duplicates}")

    #print delay message
    print(f'please wait for{sec} seconds!  saving duplicates rows.')
    time.sleep(sec)



    #saving the duplicates in a csv file
    if total_duplicates>0:
        duplicate_records=data[duplicates]
        duplicate_records.to_csv(f'{data_name}duplicates.csv',index=None)


    #deleting duplicates
    df=data.drop_duplicates()

    #print delay message
    sec=random.randint(1,4)
    print(f'please wait for{sec} seconds!  checking for missing values')
    time.sleep(sec)


    #finding missing values
    total_missing_values=df.isnull().sum().sum()
    missing_value_column=df.isnull().sum()

    print(f'Dataset has total missing value:{total_missing_values}')
    print(f'Dataset contain missing value by column \n {missing_value_column}')


    #dealing with missing values
    # fillna -- int and float
    # dropna -- any object
    

    #print delay message
    sec=random.randint(1,4)
    print(f'please wait for{sec} seconds!  cleaning the datasets')
    time.sleep(sec)  


    columns=df.columns

    for col in columns:
        #filling mean for numeric columns all rows
        if pd.api.types.is_numeric_dtype(df[col]):
            df[col]=df[col].fillna(df[col].mean())

        else:
            #droping all rows with missing values for non num col
            df.dropna(subset=col,inplace=True)    

    #print delay message
    sec=random.randint(1,4)
    print(f'please wait for{sec} seconds!  Exporting datasets.')
    time.sleep(sec)

    # data is cleaned
    print(f'congrates! Dataset is cleaned! \nNumber of rows: {df.shape[0]} Number of columns:{df.shape[1]}')

    #saving the clean dataset
    df.to_csv(f'{data_name}_Clean_data.csv',index=None)
    print("Dataset is saved!")



if __name__ == "__main__":
    
    print("Welcome to data cleaning master!")
    #ask path and fie namecl

    #calling function
    while(True):
        data_path = input("please enter dataset path:")
        data_name = input("please enter dataset name:")
        if not os.path.exists(data_path):
            print("Incorrect path. Try again with correct")
        else:
            data_cleaning_master(data_path,data_name)
            break 
    
