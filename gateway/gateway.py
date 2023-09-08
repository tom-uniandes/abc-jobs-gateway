from flask import request, jsonify
import requests

urlBaseEvaluation = 'http://evaluacion:5000'
message_error = "El envío falló, intente nuevamente"

class ExceptionHandling():

    def get_response(status_code, message):
        data_response = {
            "message": message,
            "status_code": status_code
        }
        return data_response

    def call_component_evaluation(self, endpoint):
        try:
            body = request.get_json()
            id_pregunta = body.get('id_pregunta', None)
            id_respuesta = body.get('id_respuesta', None)
            endpoint = urlBaseEvaluation + endpoint + "/" + str(id_pregunta) + "/" + str(id_respuesta)

            response = requests.request(
                method = request.method,
                url = endpoint,
                headers = request.headers,
                data = request.get_data(),
                params = request.args,
                timeout=50
            )

            status_code = response.status_code

    
            if status_code >= 400:
                response.raise_for_status()
            
            return {}, response.status_code
        
        except requests.exceptions.Timeout as e:
            status_code = 504
            response = jsonify(self.get_response(status_code, message_error))
            return response, status_code
        
        except requests.exceptions.RequestException as e:
            status_code = getattr(e.response, 'status_code', 500)
            response = jsonify(self.get_response(status_code, message_error))
            return response, status_code
        
    def get_message_not_found_url(self):
        response = jsonify(self.get_response(404,"No se encontró el recurso solicitado, por favor verifique que el recurso solicitado es correcto o pongase en contacto con el servicio de soporte"))
        return response, 404