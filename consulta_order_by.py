from configuracion import SessionLocal
from crear_base_entidades import Investigador, Publicacion

def consulta_order_by():
    session = SessionLocal()
    
    print("=== ORDER BY: Investigadores ordenados por apellido ===")
    investigadores_ordenados = session.query(Investigador).order_by(
        Investigador.apellido
    ).all()
    
    for inv in investigadores_ordenados:
        print(f"{inv.apellido}, {inv.nombre} - {inv.area_investigacion}")
    
    print("\n=== ORDER BY: Publicaciones ordenadas por fecha descendente ===")
    publicaciones_ordenadas = session.query(Publicacion).order_by(
        Publicacion.fecha_publicacion.desc()
    ).all()
    
    for pub in publicaciones_ordenadas:
        print(f"{pub.fecha_publicacion}: {pub.titulo}")
    
    session.close()

if __name__ == "__main__":
    consulta_order_by()
