from configuracion import SessionLocal
from crear_base_entidades import Institucion, Departamento, Investigador, Publicacion

def consulta_all():
    session = SessionLocal()
    
    print("=== TODAS LAS INSTITUCIONES ===")
    instituciones = session.query(Institucion).all()
    for inst in instituciones:
        print(f"{inst.id}: {inst.nombre} - {inst.ciudad}, {inst.pais}")
    
    print("\n=== TODOS LOS DEPARTAMENTOS ===")
    departamentos = session.query(Departamento).all()
    for depto in departamentos:
        print(f"{depto.id}: {depto.nombre} ({depto.codigo})")
    
    print("\n=== TODOS LOS INVESTIGADORES ===")
    investigadores = session.query(Investigador).all()
    for inv in investigadores:
        print(f"{inv.id}: {inv.nombre_completo()} - {inv.area_investigacion}")
    
    print("\n=== TODAS LAS PUBLICACIONES ===")
    publicaciones = session.query(Publicacion).all()
    for pub in publicaciones:
        print(f"{pub.id}: {pub.titulo} - {pub.tipo_publicacion}")
    
    session.close()

if __name__ == "__main__":
    consulta_all()
