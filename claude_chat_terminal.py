from api_integrations.claude_anthropic import get_completion_claude
import sys

def main():
    print("Bem-vindo ao Chat com Claude AI!")
    print("Digite 'sair' para encerrar a conversa.")
    print("--------------------------------------")

    message_list = []

    while True:
        new_message = input("\nVocê: ")

        if new_message.lower() in ['sair', 'exit', 'quit']:
            print("Encerrando o chat. Até logo!")
            sys.exit(0)

        try:
            response = get_completion_claude(new_message, message_list)
            content = response.text
            message_list.append({"role": "assistant", "content": content})
            print(f"\nClaude: {content}")

        except Exception as e:
            print(f"Erro ao obter resposta: {str(e)}")
            print("Por favor, tente novamente.")

if __name__ == "__main__":
    main()