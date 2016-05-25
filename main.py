# -*- coding: utf-8 -*-
from flask import Flask, request, make_response
import json, os, psycopg2, urlparse

app = Flask(__name__)

##################################################################

def db_init():
    """Cette fonction crée la connexion à la base de données et renvoie,
       l'objet de connexion et un curseur."""

    urlparse.uses_netloc.append("postgres")
    url = urlparse.urlparse(os.environ["DATABASE_URL"])

    conn = psycopg2.connect(
        database=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port
    )
    cur = conn.cursor()    
    return conn, cur

def db_createTables(conn, cur):
  """Cette fonction initialise la base de données. Elle est invoquée par
     un chemin spécial - voir /debug/db/reset"""

  cur.execute('''\
    DROP TABLE IF EXISTS Product;
    CREATE TABLE Product (
      pid SERIAL,
      name varchar,
      price float
    );
    INSERT INTO Product (name, price) VALUES ('Pomme', 1.20);
    INSERT INTO Product (name, price) VALUES ('Poire', 1.60);
    INSERT INTO Product (name, price) VALUES ('Fraise', 3.80);
    ''')
  conn.commit()

def db_select(cur, sql, params = None):
  """Cette fonction exécute une requête SQL de type SELECT
     et renvoie le résultat avec pour chaque ligne un dictionnaire
     liant les noms de colonnes aux données."""

