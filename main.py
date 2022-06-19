from flask import Flask, jsonify, request, Response
import pandas as pd
import json 

app = Flask(__name__)

@app.route('/')
def index():
    # filenames       
    csvFilename = r'pokemon.csv'  
    jsonFilename = r'pokemon.json'  
  
    # Calling the csvToJson function  
    csvToJson(csvFilename, jsonFilename) 

    return 'archivo csv convertido a json!!!'


@app.route('/pokemon')
# Convert a .csv file to a json output with flask
def getPokemons():
    key = request.args.get('key')
    value = request.args.get('value')
    sort = request.args.get('sort', default = True)	

    if key == None or value == None:
        return jsonify({'pokemons': json.load(open('pokemon.json'))})
   
    else:
        output_json =  filterJson(key, value, sort)
        return Response(json.dumps(output_json),  mimetype='application/json')

 # Filter the json file with the key and value
def filterJson(key, value, sort):
    input_dict = json.load(open('pokemon.json'))
    # Filter python objects with list comprehensions
    output_dict = [x for x in input_dict if x[key] == value]
    # Transform python object back into json
    return output_dict

# Defining the function to convert CSV file to JSON file  
def csvToJson(csvFilename, jsonFilename):
    # reading the csv file  
    csv_df = pd.read_csv(csvFilename)
    # converting the dataframe to json
    csv_df.to_json(jsonFilename, orient='records')
    

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 8000, debug = True)
