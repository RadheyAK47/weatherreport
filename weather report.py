from tkinter import *
import requests
import json
root=Tk()

root.geometry("500x400")
root.title("asman kay samachar")

cities=Label(root,text="Enter city name",font=("classic",24,"bold"))
cities.place(relx=0.5,rely=0.3,anchor=CENTER)

textinput=Entry(root)
textinput.place(relx=0.5,rely=0.5,anchor=CENTER)

weather_info=Label(root)
weather_info.place(relx=0.5,rely=0.7,anchor=CENTER)


def weather():
    api_request=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+textinput.get()+ "&appid="+ "21cab08deb7b27f4c2b55f3e2df28ea4")
    api_output_json=json.loads(api_request.content)
    info=api_output_json["weather"][0]["main"]
    print(info)
    weather_info["text"]= str(info)


btn_search=Button(root,text="search",command=weather)
btn_search.place(relx=0.5,rely=0.9,anchor=CENTER)







root.mainloop()