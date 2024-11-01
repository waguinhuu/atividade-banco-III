from services.usuario_service import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from config.database import Session
import os

def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)


    #Solicitando dados do usuario
    print("\nAdicionando usuario: ")
    nome = input("Digite o nome do usuario: ")
    email = input("Digite o email do usuario: ")
    senha = input("Digite a senha do usuario: ")

    service.criar_usuario(nome=nome, email=email, senha=senha)

    # Exibindo todos os usuarios na tabela usuarios do banco de dados.
    print("\nListando usuarios cadastrados: ")
    lista_usuarios = service.listar_todos_usuarios()
    for usuario in lista_usuarios:
        print(f"\nNome: {usuario.nome} - \nE-mail: {usuario.email} - \nSenha: {usuario.senha}\n")

if __name__ == "__main__":
    os.system("cls || clear")
    main()