import pandas as pd
import matplotlib.pyplot as plt

while True:
    print("MAIN MENU")
    print("1.Dataframe Stats")
    print("2.Record Analysis")
    print("3.Insert Delete Record")
    print("4.Data Visualization as per records")
    print("5.Customized Data Visualization")
    print("6.Exit")
    ch = int(input("Enter Your Choice:"))
    if ch == 1:
        df = pd.read_csv("Untitled_spreadsheet.csv", encoding="latin-1")
        print("Dataframe Properties:")
        print("1.Diplay the transpose")
        print("2.Display column names")
        print("3.Display indexes")
        print("4.Display the shape")
        print("5.Display the dimension")
        print("6.Display the data types of all columns")
        print("7.Display the size")
        ch1 = int(input("Enter Your Choice:"))
        if ch1 == 1:
            print(df.T)
            input("Press Enter to continue...")
        elif ch1 == 2:
            print(df.columns)
            input("Press Enter to continue...")
        elif ch1 == 3:
            print(df.index)
            input("Press Enter to continue...")
        elif ch1 == 4:
            print(df.shape)
            input("Press Enter to continue...")
        elif ch1 == 5:
            print(df.ndim)
            input("Press Enter to continue...")
        elif ch1 == 6:
            print(df.dtypes)
            input("Press Enter to continue...")
        elif ch1 == 7:
            print(df.size)
            input("Press Enter to continue...")
        elif ch1 == 8:
            pass
    elif ch == 2:
        df = pd.read_csv("Untitled_spreadsheet.csv", encoding="latin-1")
        print("RECORD ANALYSIS MENU")
        print("1. Highest Sales")
        print("2. Lowest Sales")
        print("3. Specific Number of Records From Top")
        print("4. Specific Number of Records From Bottom")
        print("5. Details record for Sr.No.")
        print("6. Details record for a Top Demanded Product")
        print("7. Details record for a Product")
        print("8. Most Demanded Products")
        print("9. Least Demanded Products")
        print("10.Repeted Customers")
        print("0. Back")
        ch2 = int(input("Enter Your Choice:"))
        if ch2 == 1:
            df1 = df.nlargest(6, 'Sales')
            print(df1)
            input("Press Enter to continue...")
        elif ch2 == 2:
            df2 = df.nsmallest(6, 'Sales')
            print(df2)
            input("Press Enter to continue...")
        elif ch2 == 3:
            no = int(input("How Many Number of Records You Want To Be Printed From the Top:"))
            df3 = df.head(no)
            print(df3)
            input("Press Enter to continue...")
        elif ch2 == 4:
            n = int(input("How Many Number of Records You Want To Be Printed From the Bottom:"))
            df4 = df.tail(n)
            print(df4)
            input("Press Enter to continue...")
        elif ch2 == 5:
            sno = int(input("Enter the Sr.No. For Which You Want the data To Be Displayed:"))
            print(df.loc[sno - 1])
            input('Press Enter to continue...')
        elif ch2 == 6:
            top = input("Enter the Top Demanded Product Name For Which You Want the data To Be Displayed:")
            df6 = df[df['Top-Demanded-Products'] == top]
            print(df6)
            input('Press Enter to continue...')
        elif ch2 == 7:
            product = input("Enter the Product Name For Which You Want the data To Be Displayed:")
            df7 = df[df['Top-Demanded-Products'] == product]
            print(df7)
            input('Press Enter to continue...')
        elif ch2 == 8:
            df8 = df.nlargest(10, 'Top-Demanded-Product-Sales')
            print(df8)
            input("Press Enter to continue...")
        elif ch2 == 9:
            df9 = df.nsmallest(10, 'Top-Demanded-Product-Sales')
            print(df9)
            input("Press Enter to continue...")
        elif ch2 == 10:
            print("Repeated Customers Data:")
            repeated_customers = df[df['RepeatedCustomers'] > 0][['Company', 'Sales', 'RepeatedCustomers']]
            print(repeated_customers)
            input("Press Enter to continue...")
        elif ch2 == 0:
            pass
        else:
            print("Invalid Choice")
    elif ch == 3:
        df = pd.read_csv("Untitled_spreadsheet.csv", encoding="latin-1")
        print("Insert Delete record")
        print("1.Insert a record")
        print("2.Delete a records")
        print("3.Exit The Records Menu")
        ch3 = int(input("Enter Your Choice:"))
        if ch3 == 1:
            col = df.columns
            print(col)
            j = 0
            rec = {}
            for i in col:
                print("Enter", col[j], "value   :")
                nval = input()
                rec[col[j]] = nval
                j = j + 1
            df = pd.concat([df, pd.DataFrame([rec])], ignore_index=True)
            print("Data is Successfully Updated")
            df.to_csv("Untitled_spreadsheet.csv", index=False)
            input("Press enter to continue...")
        elif ch3 == 2:
            a = int(input("Enter S.No. whose data You Want to be deleted:"))
            df.drop([a - 1], inplace=True)
            df.to_csv("Untitled_spreadsheet.csv", index=False)
            print("Record deleted...")
            input("Press enter to continue...")
        elif ch3 == 3:
            pass
    elif ch == 4:
        df = pd.read_csv("Untitled_spreadsheet.csv", encoding="latin-1")
        print("Data Visualization Menu - According to no. of rows")
        print("1.Line Plot")
        print("2.Vertical Bar Plot")
        print("3.Horizontal Bar Plot")
        print("4.Histogram")
        print("5. Pai Chart")
        print("6.Exit The Data Visualization Menu")
        ch4 = int(input("Enter Choice:"))
        df1 = pd.DataFrame()
        if ch4 == 1:
            n = int(input("How many records from the top of table you want to plot:"))
            df1 = df.head(n)
            df1.plot(linestyle="-.", linewidth=2, label="Selected Records")
            plt.show()
        elif ch4 == 2:
            n = int(input("How many records from the top of table you want to plot:"))
            df1 = df.head(n)
            df1.plot(kind="bar", color="pink", width=0.8)
            plt.show()
        elif ch4 == 3:
            n = int(input("How many records from the top of table you want to plot:"))
            df1 = df.head(n)
            df1.plot(kind="barh", color="cyan", width=0.8)
            plt.show()
        elif ch4 == 4:
            df.hist(color="yellow", edgecolor="pink")
            plt.show()
        elif ch4 == 5:
            df1=df.head(n)
            df1.plot.pie(autopct='%1.1f%%', startangle=90)
            plt.show()
        elif ch4 == 6:
            pass
    elif ch == 5:
        df = pd.read_csv("Untitled_spreadsheet.csv", encoding="latin-1")
        print("Customized Data Visualization Menu")
        print("1. By Sales")
        print("2. By Top Demanded Products")
        print("3.Back")
        ch5 = int(input("Enter Choice:"))
        df1 = pd.DataFrame()
        if ch5 == 1:
            print("Ensure the Sales should match with CSV records:")
            sales = int(input("Enter Sales value you want to plot:"))
            df1 = df[df['Sales'] == sales]
            print("1. Line Chart")
            print("2. Bar Chart")
            print("3. Horizontal Bar Chart")
            print("4. Histogram")
            print("5. Back")
            ch5_1 = int(input("Enter your choice:"))
            if ch5_1 == 1:
                df1.plot(x='Company', y='Sales', kind='line', linestyle="-.", linewidth=2, color='r')
                plt.show()
            elif ch5_1 == 2:
                df1.plot(x='Company', y='Sales', kind='bar', color='r')
                plt.show()
            elif ch5_1 == 3:
                df1.plot(x='Company', y='Sales', kind='barh', color='r')
                plt.show()
            elif ch5_1 == 4:
                df1.plot(x='Company', y='Sales', kind='hist', bins=25, cumulative=True)
                plt.show()
            elif ch5_1 == 5:
                pass
            elif ch5_1 == 5:
                pass
        elif ch5 == 2:
            print("Ensure the name should match with CSV records:")
            product = input("Enter Product name you want to plot:")
            df1 = df[df['Top-Demanded-Products'] == product]
            print("1. Line Chart")
            print("2. Bar Chart")
            print("3. Horizontal Bar Chart")
            print("4. Histogram")
            print("5. Back")
            ch5_2 = int(input("Enter your choice:"))
            if ch5_2 == 1:
                df1.plot(x='Top-Demanded-Products', y='Sales', kind='line', linestyle="-.", linewidth=2, color='r')
                plt.show()
            elif ch5_2 == 2:
                df1.plot(x='Top-Demanded-Products', y='Sales', kind='bar', color='r')
                plt.show()
            elif ch5_2 == 3:
                df1.plot(x='Top-Demanded-Products', y='Sales', kind='barh', color='r')
                plt.show()
            elif ch5_2 == 4:
                df1.plot(x='Top-Demanded-Products', y='Sales', kind='hist', bins=25, cumulative=True)
                plt.show()
            elif ch5_2 == 5:
                pass
    elif ch == 6:
        print("Thanks For the visiting the project")
        break
    else:
        print("---------------------------INVALID CHOICE---------------------------")
