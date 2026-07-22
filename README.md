# Software de Tabulación y Graficación de Ecuaciones Lineales

Una aplicación en Python diseñada para calcular, tabular valores y graficar ecuaciones matemáticas de manera interactiva a través de la terminal. Actualmente, la aplicación permite ingresar **dos ecuaciones lineales**, solicitar al usuario el rango de valores para la variable $x$, presentar las tablas de tabulación formateadas en consola y generar una gráfica visual utilizando **Matplotlib**.

En futuras versiones se incluirá soporte para ecuaciones cuadráticas, polinómicas y funciones trigonométricas.

---

## 📋 Características Principales

* **Entrada interactiva:** El usuario define las ecuaciones y los valores para $x$.
* **Tabulación clara en terminal:** Salida organizada mostrando el número de evaluación ($n^\circ$), el valor de $x$ y el resultado de $y$.
* **Visualización gráfica:** Renderizado de gráficos de alta calidad con líneas de referencia, leyenda y etiquetas claras mediante **Matplotlib**.
* **Entorno aislado:** Diseñado para ejecutarse dentro de un entorno virtual (`.venv`) manteniendo el sistema limpio.

---

## 🛠️ Requisitos Previos

Antes de comenzar, asegúrate de tener instalado en tu sistema:

* **Python 3.10+** (probado en Debian 12 / Linux / Windows / macOS)
* **Git**
* Módulo `venv` de Python instalado en el sistema (`sudo apt install python3-venv python3-pip` en Debian/Ubuntu).

---

## 🚀 Guía Paso a Paso para Iniciar / Clonar el Proyecto

Sigue esta secuencia exacta de comandos en tu terminal cuando me clones o descargues este proyecto en otra máquina (por ejemplo, en tu otra laptop).

### 1. Clonar el repositorio
```bash
git clone git@github.com:MMendoza-deb/Graficas.git
git clone https://github.com/MMendoza-deb/Graficas.git
cd Graficas
```

### 2. Crear el entorno virtual (`.venv`)
Crea una copia aislada de Python dentro de la carpeta del proyecto:
```bash
python3 -m venv .venv
```

### 3. Activar el entorno virtual
* **En Linux / macOS:**
  ```bash
  source .venv/bin/activate
  ```
* **En Windows (PowerShell):**
  ```powershell
  .\.venv\Scripts\Activate.ps1
  ```
* **En Windows (CMD):**
  ```cmd
  .\.venv\Scripts\activate.bat
  ```

> **Verificación:** Deberías ver `(.venv)` al inicio de la línea de comandos de tu terminal.

### 4. Instalar las dependencias
Instala todas las librerías necesarias (como `matplotlib`) a partir del archivo `requirements.txt`:
```bash
pip install -r requirements.txt
```
### 5. Instalar tKinter
ejecuta el siguiente comando:
```bash
sudo apt update && sudo apt install -y python3-tk
```

### 6. Ejecutar la aplicación
Ejecuta el script principal:
```bash
python main.py
```

---

## Formato de Salida en Terminal (Tabulación)

La aplicación mostrará los datos tabulados según el rango elegido por el usuario con la siguiente estructura:

```text
Ecuación 1: y = 2x + 1
+----+-----+--------------------+
| n° |  x  |  y = 2x + 1        |
+----+-----+--------------------+
|  1 | -2  | -3                 |
|  2 | -1  | -1                 |
|  3 |  0  |  1                 |
|  4 |  1  |  3                 |
|  5 |  2  |  5                 |
+----+-----+--------------------+

Ecuación 2: y = -x + 4
+----+-----+--------------------+
| n° |  x  |  y = -x + 4        |
+----+-----+--------------------+
|  1 | -2  |  6                 |
|  2 | -1  |  5                 |
|  3 |  0  |  4                 |
|  4 |  1  |  3                 |
|  5 |  2  |  2                 |
+----+-----+--------------------+
```

---

## 📦 Dependencias Principales

* [Matplotlib](https://matplotlib.org/) — Biblioteca para la generación de gráficos en 2D.

Si agregas nuevas librerías en el futuro, recuerda actualizar el archivo de dependencias ejecutando:
```bash
pip freeze > requirements.txt
```

---

## Funcionalidades Futuras (Roadmap)

- [x] Graficación de ecuaciones lineales ($y = mx + b$).
- [ ] Soporte para ecuaciones cuadráticas ($y = ax^2 + bx + c$).
- [ ] Graficación de múltiples funciones simultáneas en el mismo plano cartesiano.
- [ ] Exportación de gráficos en formato PNG o PDF.
- [ ] Interfaz gráfica de usuario (GUI).

---

## Licencia

Este proyecto está bajo la Licencia MIT — siéntete libre de usarlo y modificarlo.
