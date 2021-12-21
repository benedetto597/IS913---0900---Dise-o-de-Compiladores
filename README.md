<div align="center">
    <img src="https://cdn-icons-png.flaticon.com/512/186/186303.png" width="300px"> </img> 
    
<!-- Encabezado -->
## IS-913 | Diseño de Compiladores
## III PAC - 2021
### Proyecto - Grupo #4

### Catedratico **Ing. Alex Hernán Moncada Gómez**


</div>
### Integrantes 
| Nombre | Numero De Cuenta |
|:-------------:| :-----:|
| Edgar Josué Benedetto Godoy | `20171033802` |
| Gina Nicol Discua Quiroz | `20181005768` |
| Gerson David Chávez Figueroa | `20171000892` |
| Kevin Daniel Varela Vásquez | `20171004483` |
| Lisandro Alfredo Suárez Salinas | `20161002968` |
| Rafael Alberto Bautista Santos | `20151001991` |
| Cristian Alexander Martínez Ochoa | `20131015700` |


_______
_______

### **Paquetes de Python a instalar previamente**

1. **Pip 3** - Gestor de paquetes para python.
    ```
    sudo apt-get install python3-pip
    ```

2. **Lark** - Principalmente un contenedor delgado para los diferentes analizadores (Lexico, Sintactico y Semantico) y para la construcción de árboles sintacticos.

    ```
    sudo pip3 install lark
    ```
3. **Matplotlib** - Generación de gráficos a partir de datos contenidos en listas o arrays en el lenguaje de programación Python y su extensión matemática NumPy.
    ```
    sudo apt-get install python3-matplotlib
    ```

4. **Tabulate** - Impresión de tablas con estilo en consola

    ```
    sudo pip3 install tabulate
    ```

5. **Graphviz** - La visualización de gráficos es una forma de representar información estructural como diagramas de gráficos y redes abstractos. Tiene importantes aplicaciones en redes, bioinformática, ingeniería de software, diseño de bases de datos y web, aprendizaje automático y en interfaces visuales para otros dominios técnicos.

    ```
    sudo pip3 install pygraphviz
    ```

6. **NetworkX** - Estudio de grafos y analisis de redes
    ```
    sudo pip3 install networkx
    ```
7. **PIL** - PIL (Python Imaging Library) agrega muchas funciones de procesamiento de imágenes a Python. Pillow es un fork de PIL que agrega algunas características fáciles de usar.
    ```
    sudo pip3 install PIL
    ```

______
### **Comandos para ejecución en consola**

##### Estructura de comando
    
    python3 main.py <nombreArchivo> <comando>
    
##### Comandos disponibles
* Imprimir tabla de símbolos 
    ```
    python3 main.py index.lng --symbols-table
    ```

* Traduccion por gramatica libre de contexto 
    ```
    python3 main.py index.lng --grammar-translation
    ```
* Imprimir arbol sintactico
    ```
    python3 main.py index.lng --syntactic-tree
    ```
* Graficar arbol sintactico
    ```
    python3 main.py index.lng --graph-tree
    ```

______

### Bibliografía

##### Documentaciones

* [Documentación de Lark Ultima Version](hhttps://lark-parser.readthedocs.io/en/latest/index.html#)
* [Documentación de Lark Parser](https://lark-parser.readthedocs.io/en/stable/)
* [Documentación de Matplotlib](https://matplotlib.org/)
* [Documentación de Tabulate](https://pypi.org/project/tabulate/)
* [Documentación de Graphviz](https://pygraphviz.github.io/documentation/stable/index.html)
* [Documentación de NetworkX](https://networkx.org/documentation/latest/index.html)

##### Ejemplos

* [Ejemplos de NetworkX](https://www.geeksforgeeks.org/python-visualize-graphs-generated-in-networkx-using-matplotlib/)
* [Ejemplos de Parseo con JSON](https://github.com/lark-parser/lark/blob/master/docs/json_tutorial.md)