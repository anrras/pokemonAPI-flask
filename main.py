from flask import Flask, jsonify, request
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
    elif key == 'Name' and value == 'pikachu':
        return sortJson('pokemon.json', key, sort)

# Sort a json file by a key
def sortJson(jsonFilename, key, sort):
    # reading the json file  
    json_df = pd.read_json(jsonFilename)
    # sorting the dataframe by the key
    json_df.sort_values(by=key, ascending=sort)
    # converting the dataframe to json
    json_df.to_json('resultJson.json', orient='records')

    return jsonify({'pokemons': json.load(open('resultJson.json'))})


# Defining the function to convert CSV file to JSON file  
def csvToJson(csvFilename, jsonFilename):
    # reading the csv file  
    csv_df = pd.read_csv(csvFilename)
    # converting the dataframe to json
    csv_df.to_json(jsonFilename, orient='records')
    

if __name__ == '__main__' :
     app.run(port=8080, debug=True)
