import pandas as pd
import pickle
import os
#file path to Santander Statments 
directory = "Statements"
output_filename = "Santander_df.pkl"
Santander_df = pd.DataFrame(columns = ['Date', 'Description','Amount', 'Balance'])

#Open files within Statements
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        print("Opening... " + filename)
        #Open file and loop through lines
        df_entry_number = 0
        df_date_entry = 0
        df_description_entry = 0
        df_amount_entry = 0
        df_balance_entry = 0
        
        file = open(os.path.join("Statements/", filename), "r")
        for line in file:
            #Parse for "Date" , "Amount", "Balance"
            if ("Date" in line):
                df_date_entry = line.split(':')                   #Remove "Date:"
                df_date_entry = df_date_entry[1].replace(" ", "") #Remove white space
                df_date_entry = df_date_entry.replace("\n", "")   #Remove \n
                # print(df_date_entry)

            elif ("Description" in line):
                df_description_entry = line.split("\xa0") #Weird Text character 
                df_description_entry = df_description_entry[1].replace("\n","")
                # print(df_description_entry)

            elif ("Amount" in line):
                df_amount_entry = line.split("\xa0")
                df_amount_entry = float(df_amount_entry[1])
                # print(df_amount_entry)

            elif ("Balance" in line):
                df_balance_entry = line.split(":")
                df_balance_entry = df_balance_entry[1].replace(" ", "")
                df_balance_entry = float(df_balance_entry)
                # print(df_balance_entry)

                #end of entry add to dataframe
                row = [df_date_entry,df_description_entry,df_amount_entry,df_balance_entry]
                Santander_df.loc[df_entry_number] = row 
                df_entry_number = df_entry_number + 1

print("Saving... Santander_df.pkl")       
Santander_df.to_pickle(output_filename)
