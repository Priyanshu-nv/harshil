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
 ch=int(input("Enter Your Choice:"))
 if(ch==1):
    df=pd.read_csv("your_updated_file.csv")
    print("Dataframe Properties:")
    print("1.Diplay the transpose")
    print("2.Display column names")
    print("3.Display indexes")
    print("4.Display the shape")
    print("5.Display the dimension")
    print("6.Display the data types of all columns")
    print("7.Display the size")
    print("8.Back")
 ch1=int(input("Enter Your Choice:"))
 if ch1==1:
    print(df.T)
    input("Press Enter to continue...")
 elif ch1==2:
    print(df.columns)
    input("Press Enter to continue...")
 elif ch1==3:
    print(df.index)
    input("Press Enter to continue...")
 elif ch1==4:
    print(df.shape)
    input("Press Enter to continue...")
 elif ch1==5:
    print(df.ndim)
    input("Press Enter to continue...")
 elif ch1==6:
    print(df.dtypes)
    input("Press Enter to continue...")
 elif ch1==7:
    print(df.size)
    input("Press Enter to continue...")
 elif ch1==8:
    pass
 elif ch==2:
    df=pd.read_csv("your_updated_file.csv")
    print("RECORD ANALYSIS MENU")
    print("1.Highest Sales")
    print("2.Lowest Sales")
    print("3.Specific Number of Records From Top")
    print("4.Specific Number of Records From Bottom")
    print("5.Details record for Sr.No.")
    print("6.Details record for a Team")
    print("7.Details record for a product")
    print("8.Most Demanded Products")
    print("9.Least Demanded Products")
    print("0.Back")
 ch2=int(input("Enter Your Choice:"))
 if ch2==1:
    df1=df.nlargest(10,'Sales')
    print(df1)
    input("Press Enter to continue...")
 elif ch2==2:
    df2=df.nsmallest(10,'Sales')
    print(df2)
    input("Press Enter to continue...")
 elif ch2==3:
    no=int(input("How Many Number of Records You Want To Be Printed From The Top:"))
    df3 = df.head(no)
    print(df3)
    input("Press enter to continue...")
 elif ch2==4:
    n=int(input("How Many Number of Records You Want To Be Printed From Bottom:"))
    df4 = df.tail(n)
    print(df4)
    input("Press enter to continue...")
 elif ch2==5:
    sno=int(input("Enter The Sr.No. For Which You Want The data To Be Displayed:"))
    print(df.loc[sno-1])
    input('Press enter to continue...')
 elif ch2==6:
    team=input("Enter The Team Name For Which You Want The data To Be Displayed:")
    df6=df[df['Top Demanded Products']==team]
    print(df6)
    input('Press enter to continue...')
 elif ch2==7:
    product =input("Enter The Product Name For Which You Want The data To Be Displayed:")
    df7=df[df['Top Demanded Products']==product]
    print(df7)
    input('Press enter to continue...')
 elif ch2==8:
    df8=df.nlargest(10,'Top Demanded Product Sales')
    print(df8)
    input("Press enter to continue...")
 elif ch2==9:
    df9=df.nsmallest(10,'Top Demanded Product Sales')
    print(df9)
    input("Press enter to continue...")
 if ch2==0:
    pass
 else : 
    print("Invalid Choice")
 if (ch==3):
    df=pd.read_csv("your_updated_file.csv")
    print("Insert Delete record")
    print("1.Insert a record")
    print("2.Delete a records")
    print("3.Exit The Records Menu")
    ch3=int(input("Enter Your Choice:"))
 if ch3==1:
    col=df.columns
    rec={}
   for i in col:
      nval = input(f"Enter {i} value: ")
      rec[i] = nval
      df = df.append(rec, ignore_index=True)
      print("Data is Successfully Updated")
      df.to_csv('your_updated_file.csv', index=False)  # Replace with your actual file name
      input("Press Enter to continue...")
 elif ch3 == 2:
      a = int(input("Enter S.No. whose data You Want to be deleted:"))
      df = df.drop([a - 1])
      df.to_csv('your_updated_file.csv', index=False)  # Replace with your actual file name
      print("Record deleted...")
      input("Press Enter to continue...")
   elif ch3 == 3:
      pass
 elif ch == 4:
        df = pd.read_csv("your_updated_file.csv")  # Replace "your_updated_file.csv" with the actual CSV file name
        print("Data Visualization Menu - According to no. of records")
        print("1. Line Plot")
        print("2. Vertical Bar Plot")
        print("3. Horizontal Bar Plot")
        print("4. Histogram")
        print("5. Exit The Data Visualization Menu")
        
        ch4 = int(input("Enter Choice:"))
        df1 = pd.DataFrame()
   if ch4 == 1:
      n = int(input("How many records from the top of table you want to plot:"))
      df1 = df.head(n)
      df1.plot(linestyle="-.", linewidth=2, label="Sales Data")
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
      pass
   elif ch == 5:
      df = pd.read_csv("your_updated_file.csv")  # Replace "your_updated_file.csv" with the actual CSV file name
      print("Customized Data Visualization Menu")
      print("1. By Sales")
      print("2. By Top Demanded Products")
      print("3. Back")
      
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
        elif ch5 == 2:
            print("Ensure the Top Demanded Products should match with CSV records:")
            product = input("Enter Product name you want to plot:")
            
            df1 = df[df['Top Demanded Products'] == product]
            
            print("1. Line Chart")
            print("2. Bar Chart")
            print("3. Horizontal Bar Chart")
            print("4. Histogram")
            print("5. Back")
            
            ch5_2 = int(input("Enter your choice:"))
            
            if ch5_2 == 1:
                df1.plot(x='Company', y='Top Demanded Product Sales', kind='line', linestyle="-.", linewidth=2, color='r')
                plt.show()
            elif ch5_2 == 2:
                df1.plot(x='Company', y='Top Demanded Product Sales', kind='bar', color='r')
                plt.show()
            elif ch5_2 == 3:
                df1.plot(x='Company', y='Top Demanded Product Sales', kind='barh', color='r')
                plt.show()
            elif ch5_2 == 4:
                df1.plot(x='Company', y='Top Demanded Product Sales', kind='hist', bins=25, cumulative=True)
                plt.show()
            elif ch5_2 == 5:
                pass
        elif ch5 == 3:
            pass
    elif ch == 6:
        print('Downloaded from www.tutorialaicsip.com')
        print("Thanks for visiting our blog, for more projects stay tuned with us!!!")
        break
    else:
        print("---------------------*INVALID CHOICE---------------------*")
        print('Downloaded from www.tutorialaicsip.com')
        print("Thanks for visiting our blog, for more projects stay tuned with us!!!")