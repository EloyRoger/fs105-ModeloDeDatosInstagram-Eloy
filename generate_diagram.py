from sqlalchemy import MetaData
from sqlalchemy_schemadisplay import create_schema_graph
from src.database.db import db
from src.models.User import User
from src.models.Post import Post
from src.models.Comment import Comment
from src.models.Media import Media
from src.models.Follower import Follower
from sqlalchemy import create_engine


engine = create_engine ("postgresql://gitpod:postgres@localhost:5432/example")

metadata = db.metadata

# Crear el grafo del esquema
graph = create_schema_graph(
    metadata=metadata,
    engine=engine,
    show_datatypes=True,  # muestra tipos de columnas
    show_indexes=True,    # muestra índices
    rankdir='LR',         # de izquierda a derecha
    concentrate=False     # mejor legibilidad
)

# Guardar en PNG
graph.write_png("diagram.png")

print("Diagrama creado: diagram.png")
