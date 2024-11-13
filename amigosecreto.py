import random
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela para Windows e outros sistemas

def cadastrar_participantes():
    participantes = []
    while True:
        nome = input("Digite o nome do participante (ou 'sair' para finalizar): ")
        if nome.lower() == 'sair':
            break
        elif nome and nome not in participantes:
            participantes.append(nome)
        else:
            print("Nome inválido ou já cadastrado. Tente novamente.")
    return participantes

def sortear_amigo_secreto(participantes):
    sorteados = participantes.copy()
    random.shuffle(sorteados)
    
    amigos_secretos = {}
    for i, nome in enumerate(participantes):
        # Garante que ninguém tire a si mesmo
        if sorteados[i] == nome:
            # Se coincidir, embaralha novamente para evitar repetir
            return sortear_amigo_secreto(participantes)
        amigos_secretos[nome] = sorteados[i]
    
    return amigos_secretos

def main():
    print("Cadastro dos participantes do Amigo Secreto")
    participantes = cadastrar_participantes()
    
    if len(participantes) < 2:
        print("É necessário no mínimo dois participantes para o sorteio.")
        return
    
    amigos_secretos = sortear_amigo_secreto(participantes)
    
    print("\nSorteio concluído! Cada participante receberá o nome do seu amigo secreto.\n")
    
    for nome in participantes:
        print(f"{nome}, seu amigo secreto foi sorteado! Aguarde a mensagem privada.")
        input("Pressione Enter para revelar seu amigo secreto...")
        print(f"{nome}, seu amigo secreto é: {amigos_secretos[nome]}")
        input("Pressione Enter para limpar e passar para o próximo sorteio...")
        
        limpar_tela()  # Limpa a tela antes de passar para o próximo participante

if __name__ == "__main__":
    main()
