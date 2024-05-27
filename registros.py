import sqlite3

conexion = sqlite3.connect("bdbiblioteca.db")

cursor = conexion.cursor()

# En una cadena guardaremos el script de creacion de la tabla pais
tabla_pais = """CREATE TABLE pais(
                    idpais INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT UNIQUE,
                    estado TEXT
                    )
            """
tabla_editorial = """ CREATE TABLE editorial(
                        ideditorial INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT,
                        estado TEXT
                    )
            """

tabla_autor = """ CREATE TABLE autor(
                    idautor INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT,
                    f_nacimiento TEXT
                    )
            """
tabla_libro = """ CREATE TABLE libro(
                    idlibro INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT,
                    cantidad INTEGER,
                    anio INTEGER,
                    precio REAL,
                    estado TEXT,
                    idpais INTEGER REFERENCES pais,
                    ideditorial INTEGER REFERENCES editorial,
                    idautor INTEGER REFERENCES autor
                    )
            """
cursor.execute(tabla_pais)
cursor.execute(tabla_editorial)
cursor.execute(tabla_autor)
cursor.execute(tabla_libro)


lista_autores = [('Flor Cerdán', '25/10/1978'),                  
                  ('Daniel Levano', '17/01/1980'),
                  ('Omar Peña', '15/10/1978'),
                  ('Cesar Zapata', '15/10/1960')
                  ]

lista_editoriales = [('EIU', 'A'),                  
                  ('Macro', 'A'),
                  ('Bosch', 'A'),
                  ('Lima Sur', 'A'),
                  ('Pirámide', 'A'),
                  ('Colombus', 'A'),
                  ('Centro', 'A')
                  ]


lista_paises = [('Argentina', 'A'),                  
                  ('Colombia', 'A'),
                  ('Venezuela', 'A'),
                  ('Uruguay', 'A'),
                  ('Paraguay', 'A'),
                  ('USA', 'A')
                  ]

lista_libros = [('Oracle 11g', 10, 2019, 50, 'A', 1, 1, 1),                  
                 ('Sistemas Operativos', 14, 2016, 59, 'A', 1, 4, 3),
                 ('Estructuras de Datos', 6, 2018, 20, 'A', 2, 2, 3),
                 ('Algoritmos con Python', 8, 2017, 70, 'A', 2, 2, 1),
                 ('BI', 6, 1998, 50, 'A', 1, 4, 2),
                 ('Ing. de Software', 9, 2000, 56, 'A', 3, 2, 4),
                 ('Organización de PC', 9, 2016, 60, 'A', 7, 2, 1),
                 ('Ensamblaje', 9, 2018, 50, 'A', 4, 4, 3)
                  ]

consulta_pais = """INSERT INTO 
                PAIS(NOMBRE, ESTADO) 
                VALUES (?,?)
            """

consulta_editorial = """INSERT INTO 
                EDITORIAL(NOMBRE, ESTADO) 
                VALUES (?,?)
            """

consulta_autor = """INSERT INTO 
                AUTOR(NOMBRE, F_NACIMIENTO) 
                VALUES (?,?)
            """
consulta_libro = """INSERT INTO 
                LIBRO(TITULO, CANTIDAD, ANIO, PRECIO, ESTADO, IDAUTOR, IDEDITORIAL, IDPAIS) 
                VALUES (?,?,?,?,?,?,?,?)
            """
        
cursor.executemany(consulta_pais,lista_paises)
cursor.executemany(consulta_editorial,lista_editoriales)
cursor.executemany(consulta_autor,lista_autores)
cursor.executemany(consulta_libro,lista_libros)
conexion.commit()

conexion.close()

