from configuracion import SessionLocal
from crear_base_entidades import Institucion, Departamento, Investigador, Publicacion

def poblar_base_datos():
    session = SessionLocal()
    
    try:
        institucion1 = Institucion(nombre="Universidad UTPL", ciudad="Cuenca", pais="Ecuador")
        institucion2 = Institucion(nombre="Instituto Tecnológico", ciudad="Medellín", pais="Colombia")

        session.add_all([institucion1, institucion2])
        session.commit()
        
        depto1 = Departamento(nombre="Ingenieria de Requisitos", codigo="IR001", institucion_id=institucion1.id)
        depto2 = Departamento(nombre="Gestion de la Calidad ", codigo="GC001", institucion_id=institucion1.id)
        depto3 = Departamento(nombre="Redes de dispositivos", codigo="RD001", institucion_id=institucion2.id)
        
        session.add_all([depto1, depto2, depto3])
        session.commit()
        
        inv1 = Investigador(
            nombre="Ana", apellido="Gómez", email="ana.gomez@email.com", 
            area_investigacion="Inteligencia Artificial", departamento_id=depto1.id
        )
        inv2 = Investigador(
            nombre="Carlos", apellido="López", email="carlos.lopez@email.com", 
            area_investigacion="Bioinformática", departamento_id=depto2.id
        )
        inv3 = Investigador(
            nombre="María", apellido="Rodríguez", email="maria.rodriguez@email.com", 
            area_investigacion="Genética", departamento_id=depto3.id
        )
        
        session.add_all([inv1, inv2, inv3])
        session.commit()
        

        pub1 = Publicacion(
            titulo="Avances en Machine Learning", fecha_publicacion="2023-05-15",
            doi="10.1234/ml.2023", tipo_publicacion="Artículo", investigador_id=inv1.id
        )
        pub2 = Publicacion(
            titulo="Análisis Genómico con Python", fecha_publicacion="2023-08-20",
            doi="10.1234/bio.2023", tipo_publicacion="Artículo", investigador_id=inv2.id
        )
        pub3 = Publicacion(
            titulo="Sistemas Autónomos en Robótica", fecha_publicacion="2023-11-10",
            doi="10.1234/rob.2023", tipo_publicacion="Conferencia", investigador_id=inv1.id
        )
        
        session.add_all([pub1, pub2, pub3])
        session.commit()
        
        print("✅ Base de datos poblada exitosamente!")
        
    except Exception as e:
        session.rollback()
        print(f"❌ Error: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    poblar_base_datos()
