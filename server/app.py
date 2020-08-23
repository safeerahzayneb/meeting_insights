import os
import uuid
import json
import datetime 

from flask import Flask, url_for, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
from transcription_analytics import Analytics
from db import add_data, get_data, deel
# from transcription import generate_transcript

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})
UPLOAD_DIRECTORY = '/server/file_uploads/'

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify(status='ok')

@app.route('/meeting/<meeting_id>', methods=['GET'])
def meetings(meeting_id):
    # deel()
    data = get_data()
    resp = jsonify(json.loads(data[0]))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route('/upload', methods=['POST'])
def upload_new_meeting():
    meeting_name = request.form.get("meeting_name")
    meeting_date = request.form.get("date")
    meeting_id = uuid.uuid4()

    # get file
    file = request.files['file']
    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_DIRECTORY, filename)
    file.save(filepath)
    summary, key_phrases, entity_recog, entity_linking, sentiment_analysis = Analytics(filepath).meeting_analytics()
    resp_dict = {
        "meeting_id": str(meeting_id),
        "date": str(datetime.datetime.now()),
        "attendees": "Alex, Jason, Safeerah, Jennifer",
        "summary": summary,
        "key_phrases": key_phrases,
        "entity_recog": entity_recog,
        "entity_linking": entity_linking,
        "sentiment_analysis": sentiment_analysis
    }
    add_data(str(meeting_id), json.dumps(resp_dict))
    resp = jsonify(resp_dict)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)