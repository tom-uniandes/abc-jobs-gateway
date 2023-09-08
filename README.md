# abc-jobs-gateway

Gateway del experimento para el proyecto ABC

## Configuracion de Docker
1. Crear la network para los dos microservicios del experimento (correr solo una vez)

    ```bash
    docker network create abc-network
    ```
2. Construir la imagen de docker 
    ```bash
     docker build -t gateway .
    ```
3. Crear y iniciar el container (correr solo una vez)
    ```bash
    docker run --network=abc-network --name gateway -p 5005:5005 gateway
    ```
4. Iniciar el container de nuevo:
    ```bash
    docker start gateway
    ```