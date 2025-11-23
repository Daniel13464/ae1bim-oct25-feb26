from configuracion import Base, engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Institucion(Base):
    __tablename__ = 'instituciones'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    ciudad = Column(String(50), nullable=False)
    pais = Column(String(50), nullable=False)
    
    departamentos = relationship("Departamento", back_populates="institucion")
    
    def __repr__(self):
        return f"<Institucion(id={self.id}, nombre='{self.nombre}')>"

class Departamento(Base):
    __tablename__ = 'departamentos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    codigo = Column(String(10), nullable=False)
    institucion_id = Column(Integer, ForeignKey('instituciones.id'), nullable=False)
    
    institucion = relationship("Institucion", back_populates="departamentos")
    investigadores = relationship("Investigador", back_populates="departamento")
    
    def __repr__(self):
        return f"<Departamento(id={self.id}, nombre='{self.nombre}')>"

class Investigador(Base):
    __tablename__ = 'investigadores'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), nullable=False)
    apellido = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    area_investigacion = Column(String(100), nullable=False)
    departamento_id = Column(Integer, ForeignKey('departamentos.id'), nullable=False)
    
    departamento = relationship("Departamento", back_populates="investigadores")
    publicaciones = relationship("Publicacion", back_populates="investigador")
    
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"
    
    def __repr__(self):
        return f"<Investigador(id={self.id}, nombre='{self.nombre_completo()}')>"

class Publicacion(Base):
    __tablename__ = 'publicaciones'
    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(200), nullable=False)
    fecha_publicacion = Column(String(10), nullable=False)
    doi = Column(String(100), unique=True)
    tipo_publicacion = Column(String(50), nullable=False)
    investigador_id = Column(Integer, ForeignKey('investigadores.id'), nullable=False)
    
    investigador = relationship("Investigador", back_populates="publicaciones")
    
    def __repr__(self):
        return f"<Publicacion(id={self.id}, titulo='{self.titulo}')>"

def crear_tablas():
    Base.metadata.create_all(bind=engine)
    print("✅ Tablas creadas exitosamente!")

if __name__ == "__main__":
    crear_tablas()
