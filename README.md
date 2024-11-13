# Sorteio de Amigo Secreto em Python 🎉

Este é um programa em Python para realizar o sorteio de amigo secreto, garantindo que cada participante receba um nome diferente do seu próprio. O código também é projetado para manter o nome sorteado em segredo, exibindo um nome de cada vez e limpando a tela após a revelação.

## Funcionalidades

- Cadastro dinâmico dos participantes sem limite de quantidade.
- Garantia de que nenhum participante tire a si mesmo.
- Revelação individual e privada do amigo secreto para cada participante.
- Limpeza automática da tela para que o nome sorteado de cada participante desapareça do console.

## Pré-requisitos

- Python 3.x
- Sistema operacional com suporte ao comando de limpeza de tela (`cls` para Windows ou `clear` para Unix/Linux/Mac).

## Como Usar

1. Clone o repositório ou baixe o arquivo Python:
   </br>
    `
   git clone https://github.com/sawaxta/amigosecreto.git
   `
   </br>
   `
   cd amigosecreto
    `
   
3. Execute o programa:
`
python amigosecreto.py
`

4. Siga as instruções no console:

- Digite o nome de cada participante e pressione Enter.
- Quando terminar de cadastrar todos, digite 'sair' para finalizar o cadastro.
- O programa fará o sorteio automaticamente e permitirá que cada participante veja seu amigo secreto individualmente, limpando a tela após cada revelação.

## Exemplo de Uso

```plaintext
Cadastro dos participantes do Amigo Secreto
Digite o nome do participante (ou 'sair' para finalizar): Alice
Digite o nome do participante (ou 'sair' para finalizar): Bob
Digite o nome do participante (ou 'sair' para finalizar): Carol
Digite o nome do participante (ou 'sair' para finalizar): sair

Sorteio concluído! Cada participante receberá o nome do seu amigo secreto.

Alice, seu amigo secreto foi sorteado! Aguarde a mensagem privada.
Pressione Enter para revelar seu amigo secreto...
Alice, seu amigo secreto é: Bob
Pressione Enter para limpar e passar para o próximo sorteio...
```

## Estrutura do Código

- `cadastrar_participantes()`: Função que permite o cadastro de participantes até que seja digitado `'sair'`.
- `sortear_amigo_secreto(participantes)`: Função que realiza o sorteio dos amigos secretos, garantindo que ninguém tire a si mesmo.
- `limpar_tela()`: Função que limpa a tela do console após a revelação do amigo secreto.
- `main()`: Função principal que organiza o fluxo do programa, exibindo mensagens e chamando as funções necessárias.

**Divirta-se com o sorteio! E boas festas! 🎄🎁**
