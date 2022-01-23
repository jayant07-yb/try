import datetime 
import time 
import calendar


""" The list of the videos """
active_list = [] 
"""ast uploaded time"""
last_uploaded = 0

def collect_data() : 
    pass 

if __name__ == '__main__' : 
    last_uploaded =  datetime.datetime.utcnow() 
    last_uploaded = calendar.timegm(last_uploaded.utctimetuple())
    print(int(last_uploaded))
    """I will run the data in the loop"""
    while(1) :
        print("Lets See that even it is working or not")
        collect_data()
        print(last_uploaded + 30 - int(calendar.timegm(datetime.datetime.utcnow().utctimetuple())))
        time.sleep(last_uploaded + 30 - int(calendar.timegm(datetime.datetime.utcnow().utctimetuple())))
