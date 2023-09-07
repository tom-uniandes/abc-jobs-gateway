from flask import Flask
from flask_cors import CORS

from gateway import \
    ExceptionHandling

app = Flask(__name__)

app_context = app.app_context()
app_context.push()

cors = CORS(app)

@app.route('/get-answer', methods=['GET'])
def get_answer():
    return ExceptionHandling.call_component_evaluation("/evalular_pregunta")
    
@app.errorhandler(404)
def resource_not_found(e):
    return ExceptionHandling.get_message_not_found_url()

if __name__ == '__main__':
    app.run(port=5005)

