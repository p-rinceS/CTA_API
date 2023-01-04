#pkg imports:
from flask import *
import json, time
app = Flask(__name__)


@app.route('/', methods = ['GET'])
#creating ROUTE..
# Here we are creating home page (This is the default page that is loaded once api is opened.)
def home_page():
    data_set = {"Page": "Home", "Message": "Successfully Loaded", "Timestamp": time.time()}
    json_dump = json.dumps(data_set)
    
    
    return json_dump

@app.route('/user/', methods = ['GET'])
#creating ROUTE..
# Here we create another route or path.. this time to a request page. Just so we know it works...
# We created a user query to identify that it changes based on the url change.
# Hooray!
def request_page():
    user_query = str(request.args.get('user')) # .../user/?user=USER_NAME


    data_set = {"Page": "Request", "Message": f"Successfully Loaded Request Page for {user_query}", "Timestamp": time.time()}
    json_dump = json.dumps(data_set)
    
    
    return json_dump

#Let's simply run the whole program below..
if __name__ == "__main__":
    app.run(port=7777)



    # What we have to do now..

    # Find out a way to get Data for each bus.

    # Possible a text file or some csv file to list all stops.