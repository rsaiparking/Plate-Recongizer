import os
from flask import Flask, request
import Main
import plate
from flask import Response
from flask_cors import CORS

app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

@app.route('/number', methods=['POST'])
def handle_form():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    print("Posted file: {}".format(request.files['file']))
    file = request.files['file']
    filename = file.filename
    file.save(os.path.join(root_dir, filename))
    plate_number = Main.get_plate_number(filename)
    os.remove(os.path.join(root_dir, filename))
    plate_number_object = plate.Plate_Number(plate_number)
    return Response(plate_number_object.toJSON(), mimetype='application/json')

app.run()