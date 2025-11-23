from configuracion import SessionLocal
from crear_base_entidades import Investigador, Publicacion

def consulta_filter():
    session = SessionLocal()
    
    print("=== FILTER: Investigadores de Inteligencia Artificial ===")
    investigadores_ia = session.query(Investigador).filter(
        Investigador.area_investigacion == "Inteligencia Artificial"
    ).all()
    
    for inv in investigadores_ia:
        print(f"{inv.nombre_completo()} - {inv.area_investigacion}")
    
    print("\n=== FILTER: Publicaciones tipo Artículo ===")
    publicaciones_articulo = session.query(Publicacion).filter(
        Publicacion.tipo_publicacion == "Artículo"
    ).all()
    
    for pub in publicaciones_articulo:
        print(f"{pub.titulo} - {pub.tipo_publicacion}")
    
    session.close()

if __name__ == "__main__":
    consulta_filter()
