# Primer Parcial Infografia: Proyecto Paint en Python

Este proyecto es una aplicación de dibujo simple implementada en Python utilizando la biblioteca `arcade`. Permite a los usuarios dibujar utilizando varias herramientas, guardar los dibujos en formato JSON y crear animaciones GIF del proceso de dibujo.

Realizado por Alexia Marin

## Características

- **Herramientas de Dibujo**: Incluye lápiz, marcador, spray y goma de borrar.
- **Selección de Color**: Cambia entre diferentes colores para personalizar tus trazos.
- **Tamaños de Herramienta**: Selecciona entre diferentes tamaños de herramienta para ajustar el grosor de los trazos.
- **Guardado de Dibujo**: Guarda tu dibujo en un archivo JSON para cargarlo más tarde.
- **Creación de GIF**: Captura el proceso de dibujo y guárdalo como un archivo GIF animado.

## Requisitos Previos

Antes de ejecutar el proyecto, asegúrate de tener instalados los siguientes requisitos:

- Python 3.9 o superior
- Paquetes de Python:
  - `arcade`
  - `imageio`
  - `numpy`

Puedes instalar las dependencias ejecutando:

```bash
pip install arcade imageio numpy
```

## Cómo Ejecutar el Proyecto

### Ejecución Básica

Para iniciar la aplicación de dibujo, simplemente ejecuta el archivo `main.py`:

```bash
python main.py
```

### Guardar un Dibujo

1. Dibuja utilizando las herramientas proporcionadas.
2. Presiona la tecla `O` para guardar tu dibujo como un archivo JSON (`drawing.json`).
3. El archivo se guardará en el directorio actual.

### Guardar un GIF

1. Dibuja utilizando las herramientas proporcionadas.
2. Presiona la tecla `V` para guardar un GIF animado del proceso de dibujo (`drawing.gif`).
3. El GIF se guardará en el directorio actual.

### Cargar un Dibujo Guardado
```bash
python main.py drawing.json
```

## Uso de Herramientas
- **Herramientas**:
  - `F`: Lápiz
  - `P`: Marcador
  - `S`: Spray
  - `E`: Goma de borrar

- **Colores**:
  - `R`: Rojo
  - `G`: Verde
  - `B`: Azul
  - `Y`: Amarillo
  - `K`: Negro

- **Tamaños**:
  - `1`: Tamaño pequeño
  - `2`: Tamaño mediano
  - `3`: Tamaño grande

## Estructura del Proyecto

```
|-- main.py          # Archivo principal que ejecuta la aplicación
|-- tool.py          # Definición de las herramientas de dibujo
|-- drawing.json     # Ejemplo de archivo JSON guardado (opcional)
|-- drawing.gif      # Ejemplo de GIF guardado (opcional)
|-- README.md        # Este archivo
```
