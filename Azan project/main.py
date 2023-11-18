 
# here to put a link to extract information 
import requests
# here we import it to make GUI  
import tkinter as tk
from tkinter import ttk , messagebox

app =tk.Tk()
# to change the title of gui 
app.title("prayer times")

frame = ttk.Frame(app , padding = 20)
frame.grid(row=0 , column =0)

city_label = ttk.Label(frame , text="city" )
city_label.grid (row=0 , column =0 , pady =5)

city_entry = ttk.Entry(frame , width = 20)
city_entry.grid (row=0 , column =1 , pady = 5 )

country_label = ttk.Label(frame , text="country" )
country_label.grid (row=1 , column =0 , pady =5)

country_entry = ttk.Entry(frame , width = 20)
country_entry.grid (row=1 , column =1 , pady = 5 )





 def fetch_prayer_times (city , country ) :
    url = f" http://api.aladhan.com/v1/timingsByCity?city={city}&country={country}&method=2"
    try :
        response = requests.get(url)
        # now dat is exist in dictionary
        info = response.json()
        if "data" in info :
            timings = info["data"]["timings"]
            return timings
        else :
            return  None 
    except Exception as e :
        return f"unexpected error occurred {e}"
    
        
city = input (" enter city name  :  ")
country = input (" enter country name  :  ")
if city and country :
    prayer_timings =fetch_prayer_times(city , country)
    #print(prayer_timings)
    for name , time in prayer_timings.items():
        print(f"{name} : {time}")
else  :
    print ("unable to fetch prayer times") """