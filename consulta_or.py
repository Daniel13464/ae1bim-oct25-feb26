from configuracion import SessionLocal
from crear_base_entidades import Investigador, Publicacion
from sqlalchemy import or_

def consulta_or():
    session = SessionLocal()
    
    print("=== OR: Investigadores de IA O Bioinformática ===")
    investigadores_or = session.query(Investigador).filter(
        or_(
            Investigador.area_investigacion == "Inteligencia Artificial",
            Investigador.area_investigacion == "Bioinformática"
        )
    ).all()
    
    for inv in investigadores_or:
        print(f"{inv.nombre_completo()} - {inv.area_investigacion}")
    
    print("\n=== OR: Publicaciones tipo Artículo O Conferencia ===")
    publicaciones_or = session.query(Publicacion).filter(
        or_(
            Publicacion.tipo_publicacion == "Artículo",
            Publicacion.tipo_publicacion == "Conferencia"
        )
    ).all()
    
    for pub in publicaciones_or:
        print(f"{pub.titulo} - {pub.tipo_publicacion}")
    
    session.close()

if __name__ == "__main__":
    consulta_or()
