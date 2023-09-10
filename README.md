# abc-jobs-gateway
1) clonar el repositorio de evaluación
        https://github.com/leinaro/abc-jobs-evaluacion

    abrir una consola de comandos en la carpeta y ubicarse en la que se descargó el repositorio de evaluacion

    ejecutar el comando 
        docker network create abc-network

    ejecutar el comando
        docker build -t evaluacion .

    ejecutar el comando
        docker run --network=abc-network --name evaluacion -p 5000:5000 evaluacion

    En otra consola de comandos ejecutar el siguiente comando
        docker start evaluacion

2) clonar el repositorio de gateway
        https://github.com/tom-uniandes/abc-jobs-gateway

    abrir una consola de comandos en la carpeta y ubicarse en la que se descargó el repositorio de gateway
        docker build -t gateway .

    ejecutar el comando
        docker run --network=abc-network --name gateway -p 5005:5005 gateway

    En otra consola de comandos ejecutar el siguiente comando
        docker start gateway

3) instalar k6 
    tutorial + instaladores para otros sistemas operativos
        https://k6.io/docs/es/empezando/instalacion/

    instalador para windows
        https://dl.k6.io/msi/k6-latest-amd64.msi


4) ejecutar el comando
    k6 run script.js --out json=Experimento1.json --out csv=Experimento1.csv --log-output=file=Experimento1.log


5) validar los archivos  
    Experimento1.json 
    Experimento1.csv 
    Experimento1.log

6) validar el archivo 
    Experimento1.html

    ir a la seccion Checks & Groups


integracion con grafana
6) clonar o descargar el repositorio de grafana + influxdb + k6
    https://github.com/grafana/k6


7) ejecutar el comando
    docker-compose up -d influxdb grafana

8) configurar el datasource en grafana

9) configurar el dasboard en grafana

10) ejecutar el comando 
    k6 run script.js --out json=Experimento1.json --out csv=Experimento1.csv --log-output=file=Experimento1.log --out influxdb=http://localhost:8086/k6    
