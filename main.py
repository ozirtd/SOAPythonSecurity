#Main

import uvicorn

if __name__ == '__main__':
    #uvicorn.run("Application.SOAPythonSecurity:app", host="0.0.0.0", port=8000, reload=True)
    uvicorn.run("Application.UsuarioSecurity:app", host="0.0.0.0", port=8000, reload=True)

