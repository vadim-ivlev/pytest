#%%%

print("hello")
print('hello1')
print('hello2')

#%%%

a=5
b=6
c=a+b
print(a+b)


# %%

# %%
# import an excel file into a dataframe and save it to sqlite3 database
def import_excel_to_sqlite():
    import pandas as pd
    import sqlite3
    # read the excel file into a dataframe
    df = pd.read_excel('data.xlsx')
    # save the dataframe to sqlite3 database
    conn=sqlite3.connect('data.db')
    df.to_sql('data', conn, if_exists='replace', index=False)
    # read the data from the database
    df = pd.read_sql('SELECT * FROM data', con=sqlite3.connect('data.db'))
    # print the dataframe
    print(df)
    
import_excel_to_sqlite()

# %%
