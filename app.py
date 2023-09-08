from flask import Flask
from flask_cors import CORS

from gateway import \
    ExceptionHandling

app = Flask(__name__)

app_context = app.app_context()
app_context.push()

cors = CORS(app)

@app.route('/send-answer', methods=['POST'])
def post_evaluation_question():
    return ExceptionHandling.call_component_evaluation(ExceptionHandling, "/evaluar_pregunta")
    
@app.errorhandler(404)
def resource_not_found(error):
    return ExceptionHandling.get_message_not_found_url(ExceptionHandling)

if __name__ == '__main__':
    app.run(port=5005)

