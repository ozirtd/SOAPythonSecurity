#UsuarioModel:

from pydantic import BaseModel

class Usuario(BaseModel):

    Documento: str
    Usuario: str
    Clave: str
    Nombres: str
    Apellidos: str
    TarjetaCredito: float
    CVV: int