from configuracion import SessionLocal
from crear_base_entidades import Investigador, Publicacion
from sqlalchemy import and_

def consulta_and():
    session = SessionLocal()
    
    print("=== AND: Investigadores de IA con email específico ===")
    investigadores_and = session.query(Investigador).filter(
        and_(
            Investigador.area_investigacion == "Inteligencia Artificial",
            Investigador.email.like("%@email.com%")
        )
    ).all()
    
    for inv in investigadores_and:
        print(f"{inv.nombre_completo()} - {inv.area_investigacion} - {inv.email}")
    
    print("\n=== AND: Publicaciones de 2023 tipo Artículo ===")
    publicaciones_and = session.query(Publicacion).filter(
        and_(
            Publicacion.tipo_publicacion == "Artículo",
            Publicacion.fecha_publicacion.like("2023-%")
        )
    ).all()
    
    for pub in publicaciones_and:
        print(f"{pub.titulo} - {pub.tipo_publicacion} - {pub.fecha_publicacion}")
    
    session.close()

if __name__ == "__main__":
    consulta_and()
