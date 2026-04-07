#sistema de login melhorado

usuarios = []

def cadastrar_usuario():
    print("Digite o seu nome de usuário:")
    nome_usuario = input()
    print("Digite a sua senha:")
    senha = input()
    
    novo_usuario = {
        "nome_usuario": nome_usuario,
        "senha": senha 
    }
   
    for usuario in usuarios:
        if usuario['nome_usuario'] == nome_usuario:
            print('Usuário já existe')
            return
    usuarios.append(novo_usuario)
    print("Usuário cadastrado com sucesso!")
    
def login():
    print("Digite o seu nome de usuário:")
    nome_usuario = input()
    print("Digite a sua senha:")
    senha = input()
    
    if not usuarios:
        print("Nenhum usuário cadastrado")
        return
        
    for usuario in usuarios:
        if usuario["nome_usuario"] == nome_usuario and usuario["senha"] == senha:
            print("Login bem-sucedido!")
            return
    print("Nome de usuário ou senha incorretos.")
    for usuario in usuarios:
        if usuario["nome_usuario"] == nome_usuario:
            print("Usuário já existe")
        return

while True:
    print('\nDigite 1 para cadastrar um novo usuário:')
    print('\nDigite 2 para fazer login: ')  
    print('\nDigite 3 para listar os usuários:')
    print ('\nDigite 4 para sair:')
    opcao = input()
    if opcao == '1':
        cadastrar_usuario()
    elif opcao == '2':
        login()
    elif opcao == '3':
        if usuarios:
            print("Usuários cadastrados:")
            for usuario in usuarios:
                print(f"- {usuario['nome_usuario']}")
        else:
            print("Nenhum usuário cadastrado.")
    elif opcao == '4':
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")