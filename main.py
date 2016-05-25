�
�EWc           @   sz   d  d l  m Z m Z m Z d  d l Z d  d l Z d  d l Z d  d l Z e e � Z	 d �  Z
 d �  Z d d � Z d S(   i����(   t   Flaskt   requestt   make_responseNc          C   sy   t  j j d � t  j  t j d � }  t j d |  j d d |  j d |  j	 d |  j
 d |  j � } | j �  } | | f S(	   so   Cette fonction crée la connexion à la base de données et renvoie,
       l'objet de connexion et un curseur.t   postgrest   DATABASE_URLt   databasei   t   usert   passwordt   hostt   port(   t   urlparset   uses_netloct   appendt   ost   environt   psycopg2t   connectt   patht   usernameR   t   hostnameR	   t   cursor(   t   urlt   connt   cur(    (    s0   /home/vagrant/Vagrant/TP/tp3-RomainBURET/main.pyt   db_init	   s    				c         C   s   | j  d � |  j �  d S(   st   Cette fonction initialise la base de données. Elle est invoquée par
     un chemin spécial - voir /debug/db/resets;      DROP TABLE IF EXISTS Product;
    CREATE TABLE Product (
      pid SERIAL,
      name varchar,
      price float
    );
    INSERT INTO Product (name, price) VALUES ('Pomme', 1.20);
    INSERT INTO Product (name, price) VALUES ('Poire', 1.60);
    INSERT INTO Product (name, price) VALUES ('Fraise', 3.80);
    N(   t   executet   commit(   R   R   (    (    s0   /home/vagrant/Vagrant/TP/tp3-RomainBURET/main.pyt   db_createTables   s    
c         C   s   d S(   s�   Cette fonction exécute une requête SQL de type SELECT
     et renvoie le résultat avec pour chaque ligne un dictionnaire
     liant les noms de colonnes aux données.N(    (   R   t   sqlt   params(    (    s0   /home/vagrant/Vagrant/TP/tp3-RomainBURET/main.pyt	   db_select+   s    (   t   flaskR    R   R   t   jsonR   R   R
   t   __name__t   appR   R   t   NoneR   (    (    (    s0   /home/vagrant/Vagrant/TP/tp3-RomainBURET/main.pyt   <module>   s
   0		