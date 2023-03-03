from Database_Calls.GetItems import ItemsWithSecurity, ItemIsNowFree
from datetime import datetime

def CheckTime():
    current_time = datetime.today()
    for item in ItemsWithSecurity("Low"):
        time_diff = datetime.today() - datetime.strptime(item[4], "%Y-%m-%d")
        if (time_diff.days >= 20):
            print(f"Item ID: {item[0]}")
            ItemIsNowFree(item[0])
            print("Updated Item.")


        

