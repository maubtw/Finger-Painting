# Finger Painting con OpenCV y MediaPipe

Este proyecto permite dibujar en la pantalla usando tus dedos a través de la cámara. Se detecta la posición de la mano y el movimiento del dedo índice para trazar líneas en un lienzo digital. También puedes cambiar el color del pincel y limpiar el lienzo con gestos simples.

## Características

- **Dibujar**: Dibuja en la pantalla usando el dedo índice.
- **Cambio de color**: Selecciona entre varios colores de pincel moviendo tu dedo hacia las áreas de color en la pantalla.
- **Borrar lienzo**: Limpia el lienzo seleccionando la opción "Borrar".
- **Interfaz simple**: Cuatro colores de pincel y un botón de borrado disponibles en la parte superior de la pantalla.

## Requisitos

- Python 3.7 o superior
- OpenCV
- MediaPipe
- NumPy

## Instalación

 **Clona este repositorio**:
   ```bash
   git clone https://github.com/tu_usuario/finger-painting.git
   cd finger-painting
   ```

## Instalación de dependencias

Para instalar las dependencias necesarias, ejecuta el siguiente comando:

```bash
pip install opencv-python mediapipe numpy
```

## Uso

Ejecuta el script de Python:

```bash
python main.py
```

Una vez que el programa se esté ejecutando, verás las siguientes funciones en la pantalla:

- **Dibujo**: Mueve el dedo índice con el pulgar levantado (en forma de L) en la pantalla para dibujar.
- **Cambio de color**: Lleva tu dedo al área de color deseada en la parte superior para cambiar el color del pincel.
- **Borrar**: Lleva tu dedo al área "Borrar" para limpiar el lienzo.

## Controles

- **Dibujar**: Mantén el dedo índice separado del pulgar para dibujar.
- **Borrar**: Coloca el dedo sobre el área de "Borrar" en la pantalla.
- **Cambiar color**: Coloca el dedo sobre el área de color deseada.

## Estructura del Código

- **mp_hands** y **hands**: Configuran MediaPipe para el reconocimiento de manos.
- **select_color(x, y)**: Cambia el color del pincel según la posición del dedo.
- **are_thumb_and_index_separated()**: Determina si el pulgar y el índice están separados para activar el dibujo.
- **clear_canvas(x, y)**: Borra el lienzo si el dedo está en la posición del botón de borrado.
- **canvas**: Lienzo en blanco donde se dibuja con las coordenadas detectadas.

## Notas

- Asegúrate de estar en un lugar bien iluminado para una mejor detección de la mano.
- La tecla **Esc** cierra el programa.
- Si tienes una camara externa a la integrada, asegurate de cambiar la linea 38 "cap = cv2.VideoCapture(0)" por: "cap = cv2.VideoCapture(1)"
  
