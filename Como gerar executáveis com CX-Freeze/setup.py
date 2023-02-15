import sys
import os
from cx_Freeze import setup, Executable

# Definir o que deve ser incluido na pasta final
arquivos = ['hackeranonimous.ico']
# Saida de aquivos
configuracao = Executable(script='app.py',icon='hackeranonimous'.ico)

# Configurar o cx-freeze (detalhes do programa)

setup(
    name = 'Automatizacao de Login',
    version = '1.0',
    description = 'Este programa automatiza o login',
    author = 'S4m4r1t4N'
    options = {'build_exe': {'include_files': arquivos }}, 
    executables = [configuracao]
)
