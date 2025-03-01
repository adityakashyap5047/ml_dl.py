## PUT and Delete --> HTTP Verbs
## Working with APIs --> json

from flask import Flask, jsonify, request

app = Flask(__name__)

## Initialize data in my todo list
items = [
    {"id": 1, "name: ": "item1", "desc": "This is item1"},
    {"id": 2, "name: ": "item2", "desc": "This is item2"}
]

# Home route
@app.route('/')
def home():
    return "Welcome to the sample To Do List App"

# retrieve all the items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# retrieve a specific item
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item =next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({"error":"item not found"})
    return jsonify(item)

# add a new item
@app.route('/items', methods = ['POST'])
def add_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"error":"item not found"})
    new_item = {
        "id": items[-1]["id"] + 1 if items else 1,
        "name": request.json['name'],
        "desc": request.json['desc']
    }
    items.append(new_item)
    return items

# Update an existing item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item =next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({"error":"item not found"})
    item['name'] = request.json.get('name', item['name'])
    item['desc'] = request.json.get('desc', item['desc'])
    return jsonify(item)

# Delete an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({"result": "item Deleted"})

if __name__=="__main__":
    app.run(debug=True)