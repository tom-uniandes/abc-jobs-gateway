from flask import request
import requests

urlBaseEvaluation = 'http://localhost:5000'

class ExceptionHandling():
    def call_component_evaluation(endpoint):
        try:
            endpoint = urlBaseEvaluation + endpoint

            response = requests.request(
                method = request.method,
                url = endpoint,
                headers = request.headers,
                data = request.get_data(),
                params = request.args,
            )

            return (response.text, response.status_code, response.headers.items())
        except requests.exceptions.RequestException as e:
            error_message = "Ha ocurrido un error, por favor intentelo nuevamente"
            status_code = getattr(e.response, 'status_code', 500)
            return (error_message, status_code)
        
    def get_message_not_found_url():
        error_message = "No se encontró el recurso solicitado, por favor verifique que el recurso solicitado es correcto o pongase en contacto con el servicio de soporte"
        return (error_message, 404)