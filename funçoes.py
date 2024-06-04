def exibirmensagem(nome, mensagem="seja bem vindo"):
    print(f"(mensagem) {nome}")
    return f"usuario logado: {nome}"

nome_usuarion = input('digite o nome de usuario:')
msg = input('digite uma mensagem:')
usuario = exibirmensagem('nome_usuario, msg')
print(usuario)

print(50 * '-')

nome_usuarion = input('digite o nome de usuario:')
msg = input('digite uma mensagem:')
usuario = exibirmensagem('nome_usuario, msg')
print(usuario)
