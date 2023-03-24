---
marp: true
paginate: true
author: Pablo Moreira
theme: gaia
footer: ""
header: Laboratorio 3
---
# Unidad 02
# - Python
# - pip
# - virtualenv
# <!-- Presentación-->
---
# pip

## Acrónimo **P**ackage **I**nstaller for **P**ython

![bg right w:100%](img/pip0.png)

---

# pip list

```
$ pip list
```

![ h:75%](img/pip_list.png)

---

# Actualizar pip
```
$ python -m pip install --upgrade pip 
```

![ h:75%](img/pip_upgrade.png)

---
# Instalar virtualenv

```
pip install virtualenv
```
![h:60%](img/pip_virtualenv.png)

---
```
pip list

```
![h:60%](img/pip_lis1.png)

---

# Entornos virtuales

* ## Python biblioteca estándar (Módulos)
* ## Es muy común usar módulos de terceros

Un entorno  aislado de ejecución que permite a los usuarios de Python y a las aplicaciones instalar y actualizar paquetes de distribución de Python sin interferir con el comportamiento de otras aplicaciones de Python en el mismo sistema.

---

# Crear un entorno virtual
```
$ virtualenv [dirname]
```
![](img/virtualenv.png)

---
# Activar el entorno virtual
```
.\tp2\Scripts\activate.bat
```
![](img/activate.png)
```
$ pip list
```
---
# Freeze
Para guardar todos los requerimientos de una aplicación 
```
$ pip freeze > requirements.txt
```

Luego para restituirlos en un entorno virtual diferente en otro equipo o directorio.

```
$ pip install -r requirements.txt
```

---
Trabajo Practico 2

La facultad tiene una estación meteorológica funcionando en el techo del edificio.

[Link Galileo Galilei](https://www.frcon.utn.edu.ar/galileo/mb3.htm "Estación meteorológica")

La estación actualiza información aproximadamente cada 5 minutos. La siguiente [url](https://www.frcon.utn.edu.ar/galileo/downld02.txt) presenta datos de los últimos días en forma de registros, en un archivo de texto plano.
Utilizando la biblioteca o el paquete **requests**, escribir un programa en python que muestre por consola el dia, la hora y la temperatura del ultimo registro.

