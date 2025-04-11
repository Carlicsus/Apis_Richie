from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# 🔹 Importar configuración de la BD
from config.db import Base, engine
import models  # 🔹 Importa todos los modelos desde __init__.py

# 🔹 INICIALIZAR FASTAPI
app = FastAPI(
    title="HOSPITAL S.A. de C.V.",
    description="""
API RESTful para la gestión operativa de un hospital, construida con FastAPI y SQLAlchemy.

Actualmente se gestionan las siguientes entidades clave:

🧑‍⚕️ **Usuarios y Personas**  
- Registro de usuarios del sistema con autenticación mediante JWT  
- Asociación uno a uno con datos personales (personas)

🔐 **Roles y Asignaciones**  
- Catálogo de roles disponibles  
- Relación entre usuarios y roles para control de acceso

🏥 **Servicios Médicos**  
- Administración de servicios médicos brindados por el hospital  
- Relación directa con espacios físicos y consumibles asignados

🏢 **Espacios Hospitalarios**  
- Registro de áreas físicas como consultorios, quirófanos, laboratorios, etc.  
- Asociación jerárquica y relación con servicios médicos

💊 **Consumibles Médicos**  
- Gestión de insumos médicos con detalles, cantidad y tipo  
- Relación directa con los servicios médicos que los utilizan

🩺 **Áreas Médicas**  
- Registro estructurado de especialidades y divisiones médicas internas

Todas las rutas críticas están protegidas mediante autenticación JWT.
"""
)


# 🔹 Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["http://localhost:8080"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔹 IMPORTAR RUTAS ACTIVAS
from routes.users import users_router
from routes.persons import persons_router
from routes.servicios_medicos import serviceM
from routes.servicios_medicos_espacios import router as servicios_espacios_router
from routes.servicios_medicos_consumibles import servicios_medicos_consumibles
from routes.espacios import espacio
from routes.consumibles import consumible
from routes.areas_medicas import area_medica
from routes.rol import rol
from routes.userrol import userrol

# 🔹 IMPORTAR RUTAS DOCUMENTADAS (NO USADAS POR AHORA)
from routes.receta import receta_router as receta # ✅
#from routes.citas import cita
# from routes.expediente import expediente
# from routes.cirugia import cirugia_router
# from routes.horarios import horarios
# from routes.bitacora import bitacora
from routes.departamentos import departamentos
from routes.dispensaciones import dispensacion_router as dispensacion
# from routes.estudios import estudios
# from routes.resultados_estudios import resultados_estudios
from routes.lotes import lotes_medicamentos_router as lote
from routes.medicamentos import medicamento_router as medicamento
from routes.solicitudes import solicitudes_router as solicitud
# from routes.personal_medico import personal_medico
# from routes.puestos import puesto
# from routes.puestos_departamentos import puesto_departamento
# from routes.solicitudes import request
# from routes.tbb_aprobaciones import tbb_aprobaciones
# from routes.tbc_organos import tbc_organos

# 🔹 INCLUIR RUTAS ACTIVAS
app.include_router(users_router)
app.include_router(persons_router)
app.include_router(serviceM)
app.include_router(servicios_espacios_router)
app.include_router(servicios_medicos_consumibles)
app.include_router(espacio)
app.include_router(consumible)
app.include_router(area_medica)
app.include_router(rol)
app.include_router(userrol)
app.include_router(departamentos)
app.include_router(receta)
app.include_router(dispensacion)
app.include_router(medicamento)
app.include_router(lote)
app.include_router(solicitud)



# 🔹 CREAR LAS TABLAS **DESPUÉS DE REGISTRAR LAS RUTAS**
print("🔄 Creando las tablas en MySQL si no existen...")
Base.metadata.create_all(bind=engine)
print("✅ Tablas creadas exitosamente en MySQL")
