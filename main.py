from flask import request
from flask import Flask
import json 
import os 
from flask import send_file
import time
import threading 

app = Flask(__name__)

running = 0 



def get_views(link) : 
    return 1 
    pass  
"""The app for adding the value in the list"""
@app.route('/add_link', methods=["GET"])
def add_link():

    try : 
        link = request.args.get('link')
        link = link[1:][:-1]

        """Open the file """
        with open("to_collect.json" , 'r')  as my_collector : 
            to_collect = json.load(my_collector)
            to_collect[link] = 1  
        with open("to_collect.json" , 'w')  as my_collector : 
            json.dump(to_collect,my_collector) 

        return link
    except  : 
        return "Invalied Value of the Link"

@app.route('/collect_data', methods=["GET"])
def collect_data() : 
    if 1 : 
        link =  request.args.get('link')
        link = link[1:][:-1]
        """I got the link"""
        """The data is stored in the link.csv"""
        with open(link+".csv" ,"r")  as current_file : 
            data_base =  current_file.read()
            #return  data_base 
        return send_file(link+".csv" , as_attachment=True)
        #return send_from_directory(directory = app.root_path ,filename = link+".csv",)
    else   : 
        return "An error occured , Please check the link and retry"


@app.route('/routine') 
def routine() : 
    global running 
    if running  == 1  : 
        return "Already running"
    running = 1  

    try : 
        collector = open("to_collect.json" , 'r')
        to_collect = json.load(collector)
    except : 
        return "Unable to read the main file"

    
    try: 
        for link in to_collect.keys() : 
            if to_collect[link] == 1 : 
                current_view =  get_views(link) 
                file_object = open(link+'.csv' , 'a') 
                file_object.write( link +',' + str(current_view ) + "\n")
        
        return "Successfully processed"
    except : 
        return "An error occured"



if __name__ == '__main__':
    app.run(port=5000,debug=True) 
    