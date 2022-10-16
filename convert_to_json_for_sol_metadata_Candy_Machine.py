import os
import shutil
import json

json_format = {
  "name": "hash gang #1",
  "symbol": "HG",
  "description": "The unstructured cap is a one-size fits all six panel cap boasting an embroidered Buddiezz Block Logo. Rep your Buddiezz with the freshest headwear on the Solana blockchain. 100% Cotton. Adjustable fastener with metal clasp, tonal under-peak lining.",
  "seller_fee_basis_points": 1000,
  "image": "1.png",
  # "edition": 1,
 "attributes": [
        {
            "trait_type": "item",
            "value": "CAPS"
        }
    ],
  "properties": {
    "files": [
      {
        "uri": "1.png",
        "type": "image/png"
      }
    ],
    "category": "image",
    "creators": [
      {
        "address": "7fXNuer5sbZtaTEPhtJ5g5gNtuyRoKkvxdjEjEnPN4mC",
        "share": 100
      }
    ]
  },
    "collection": {
        "name": "Buddiez",
        "family": "Caps"
    }
}

c= {
    "name": "Number #0001",
    "symbol": "NB",
    "description": "Collection of 10 numbers on the blockchain. This is the number 1/10.",
    "seller_fee_basis_points": 500,
    "image": "0.png",
    "attributes": [
        {"trait_type": "Layer-1", "value": "0"},
        {"trait_type": "Layer-2", "value": "0"}, 
        {"trait_type": "Layer-3", "value": "0"},
        {"trait_type": "Layer-4", "value": "1"}
    ],
    "properties": {
        "creators": [{"address": "N4f6zftYsuu4yT7icsjLwh4i6pB1zvvKbseHj2NmSQw", "share": 100}],
        "files": [{"uri": "0.png", "type": "image/png"}]
    },
    "collection": {"name": "numbers", "family": "numbers"}
}

def make_png_json(editions, json_tempelate, nft_name, symbol ,creator ,collection = None, description=None):
    for val in range(0,editions):
        json_location = os.getcwd() + '/assets/' + str(val) + '.json'
        with open(json_location,"w+") as file:
            temp = json_tempelate.copy()
            temp['name'] =  f"{nft_name} #{str(val)}"
            temp['symbol'] = f"{str(symbol)}"
            temp['description'] = f"{str(description)}"
            temp['image'] = f"{str(val)}.png"
            # temp['edition'] = val
            temp['properties']['files'][0]['uri'] = f"{str(val)}.png"
            temp['properties']['creators'][0]['address'] = str(creator)
            temp['collection']['name'] = str(collection)
            file.write(json.dumps(temp))
            file.close()
        src_dir = os.getcwd() + '\\0' + '.png'
        dest_dir = os.getcwd()+"/assets/" + str(val) + '.png'
        shutil.copy(src_dir,dest_dir)
        #copy the file to destination dir
        

make_png_json(10, json_format,'Test Cap','Test Cap', '56izEsShAiLTzdruzTe3zy9nuAhWXd2RjRXGE7UbQjdc', 'Test', 'Cap' )
