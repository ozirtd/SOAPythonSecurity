#UsuarioSecurity:
######################################################################################################

from fastapi import FastAPI

from Domain.Usuario.UsuarioModel import Usuario

app: FastAPI = FastAPI(title='SOA Python Security', description = 'USBSI 2023')

######################################################################################################

@app.post("/ingresarusuario",
          response_model=Usuario,
          summary="Create User",
          description="Ingresar Usuario",
          tags=["Usuario"])

async def ingresar_usuario(usuario: Usuario | None = None):
    return usuario

@app.post("/modificarusuario",
          response_model=Usuario,
          summary="Update User",
          description="Modificar Usuario",
          tags=["Usuario"]
          )
async def modificar_usuario(usuario: Usuario | None = None):
    return None

@app.post("/retirarusuario",
          response_model=Usuario,
          summary="Delete User",
          description="Retirar Usuario",
          tags=["Usuario"]
          )
async def retirar_usuario(usuario: Usuario | None = None):
    return None

@app.post("/consultarusuario",
          response_model=Usuario,
          summary="Read User",
          description="Consultar Usuario",
          tags=["Usuario"]
          )
async def consultar_usuario(usuario: Usuario | None = None):
    return None