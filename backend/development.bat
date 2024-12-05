@echo off

if not exist "venv\" (
    echo Criando ambiente virtual...
    python -m venv venv
)

call venv\Scripts\activate

if not exist ".dependencies_installed" (
    echo Instalando dependências...
    pip install -r requirements.txt
    echo 1 > .dependencies_installed
)

if not exist ".env" (
    echo Criando o arquivo .env...

    echo BANCO_DE_DADOS="">> .env
    echo SECRET_KEY="">> .env

    echo Preencha as variaveis no arquivo .env e inicie novamente
    exit /b 1
) else (
    echo Iniciando o projeto no modo desenvolvimento...
    flask run
)