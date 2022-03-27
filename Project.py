import pandas as pd
import matplotlib.pyplot as plt
import time
import os

CSV_PATH = os.getcwd()+'\cars.csv'

def options():
    print("---------------------------------------------------------------")
    print("|| All Available Features :                                  ||")
    print("|| \t\t\tv --> to visualize data from csv     ||")
    print("|| \t\t\ts --> show data from csv             ||")
    print("|| \t\t\tr --> show a row from csv            ||")
    print("|| \t\t\tc --> show a col from csv            ||")
    print("|| \t\t\tdr --> delete a row from csv         ||")
    print("|| \t\t\tdc --> delete col/cols from csv      ||")
    print("|| \t\t\tac --> add new col in csv            ||")
    print("|| \t\t\tq --> quit the program               ||")
    print("---------------------------------------------------------------")
    print()

def quitting():
    print("\n\nQuitting Program.\r", end='')
    time.sleep(0.5)
    print("Quitting Program..\r", end='')
    time.sleep(0.5)
    print("Quitting Program...")
    time.sleep(0.5)
    print("\n\nProgram Successfuly Quit")
    print("\nThank You for Using our Program!\n\n")

try:
    while True:

        options()

        user_input = input("Which feature do you want do use : ")

        print()

        if user_input.lower() == 's':
            df = pd.read_csv(CSV_PATH,index_col="S.no")
            print(df)
        
        elif user_input.lower() == 'dr':
            df = pd.read_csv(CSV_PATH,index_col="Name")
            row_to_delete = input("Enter name to delete : ")
            df.drop([row_to_delete],inplace=True)
            print(df)
        
        elif user_input.lower() == 'r':
            df = pd.read_csv(CSV_PATH)
            row_no = int(input("Enter the row no : "))
            print(df.loc[row_no])
        
        elif user_input.lower() == 'c':
            df = pd.read_csv(CSV_PATH)
            col = input("Enter the col name : ")
            print(df[col])
        
        elif user_input.lower() == 'dc':
            df = pd.read_csv(CSV_PATH)
            col_to_delete = list(map(str, input("Enter the col name (if multiple col use space to seperate) : ").split(' ')))
            df.drop(col_to_delete,axis=1,inplace=True)
            print(df)
        
        elif user_input.lower() == 'ac':
            df = pd.read_csv(CSV_PATH)
            col_name = input("Enter the col name : ")
            row_ele = list(map(str, input("Enter the row elements with space between them : ").split(' ')))
            df[col_name] = pd.Series(row_ele)
            print(df)

        elif user_input.lower() == 'v':
            df = pd.read_csv(CSV_PATH)
            print("1.Barchart \n2.Line Chart \n3.Horizontal Bar Chart \n4.Histogram \n5.Go back to main menu\n")
            chart_type = int(input('Select the Chart Type : '))

            if chart_type==1:
                df.plot(kind="bar",x='Name',width=1.0)
                df.xlabel='Name'
                df.ylabel='Total'
                plt.title("Cost of Cars")
                plt.show()
                print()
                
            elif chart_type==2: 
                df.plot()
                df.xlabel='Name'
                df.ylabel='Total'
                plt.title("Cost of Cars")
                plt.show()
                print()
                
            elif chart_type==3: 
                df.plot(kind="barh",x='Name',width=1.0)
                df.xlabel='Name'
                df.ylabel='Total'
                plt.title("Cost of Cars")
                plt.show()
                print()
                
            elif chart_type==4: 
                df.plot(kind="hist",x='Name',bins=15,histtype="step")
                df.xlabel='Name'
                df.ylabel='Total'
                plt.title("Cost of Cars")
                plt.show()
                print()

            elif chart_type==5:
                print()      
                continue

        elif user_input.lower() == 'q':
            quitting()
            break

        print()

except KeyboardInterrupt :
    quitting()