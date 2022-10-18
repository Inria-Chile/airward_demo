# Intrucciones para la ejecución DEMO – Proyecto AirWard

## Requerimientos:
- Dispositivo externo de visualización (teléfono móvil o tablet) con la app DJI Go 4.0 instalada.
- Dron DJI PHANTOM 4 Pro con sus accesorios (Radio control, baterías, cargador de energía).
- Red Local Inalámbrica (WLAN)
- Unidad de procesamiento (notebook, RapsberryPi): con sistema operativo Ubuntu 20.04 y Python 3.8 o superior.
- Acceso al repositorio https://github.com/Inria-Chile/airward_demo.git

## Preparación de la unidad de procesamiento:
```
- git clone https://github.com/Inria-Chile/airward_demo.git

- cd server/LuaJIT/
    - make
    - sudo make install

- cd server/MonaServer2/
    - make

- python3.8 -m venv venv
    - source env/bin/activate
    - pip -r ./modelv0.1/requirements.txt
```

## Ejecución de la demo:
1. Ejecutar en la unidad de procesamiento "sudo ./server/MonaServer2/MonaServer/MonaServer
2. En la unidad de procesamiento se debe chequear la IP (por ejemplo: 192.168.0.101).
3. El dispositivo externo debe estar conectado a la misma red que la unidad de procesamiento, y se debe chequear que la IP tenga el mismo segmento (por ejemplo: 192.168.0.102).
4. Se debe ejecutar la aplicación DJI GO.
5. En la aplicación DJI GO, se deben realizar los siguientes pasos: ir al Menú principal (parte superior derecha); seleccionar la opción "Select Live Broadcast Plataform" y elegir la opción RTMP; posteriormente en la ventana "create custom Live Broadcast", se debe ingresar el texto “rtmp://<IP unidad de procesamiento>:1935/live”; finalmente se debe presionar el botón de inicio de la transmisión.
6. La cámara del drone debe estar enfocando al monitor en donde se esté reproduciendo el archivo "test_video.mp4".  
7. Ejecutar en el entorno virtual de python el comando: "python3 ./modelv0.1/detect.py --source "rtmp://0.0.0.0:1935/live" --weights best.pt"
9. Visualizar en la ventana de resultados la detección realizada por el modelo mediante el conjunto de bounding boxes con su etiqueta (fire o smoke) e índice de confianza respectivo.
