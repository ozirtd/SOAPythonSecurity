#SOAPythonSecurity

######################################################################################################

from fastapi import FastAPI

from Core.Security.Decode.base64Decode import Base64Decode
from Core.Security.Encode.Base64Encode import Base64Encode

app: FastAPI = FastAPI(title='SOA Python Security', description = 'USBSI 2023')

######################################################################################################

@app.get("/base64encode", summary="Base64 Encode", description="cifrado Base64", tags=["base64"])
async def base64_encode(plainText: str | None = None):
    base64encode = Base64Encode()
    return base64encode.encode(plainText)

@app.get("/base64decode", summary="Base64 Decode", description="Decifrado Base64", tags=["base64"])
async def base64_decode(encodedText: str | None = None):
    base64decode = Base64Decode()
    return base64decode.decode(encodedText)


######################################################################################################