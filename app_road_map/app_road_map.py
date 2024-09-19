import os
import time
from api_integrations.claude_anthropic import get_completion_claude

def ler_prompts():
    prompts = []
    with open(os.path.join(os.path.dirname(__file__), 'prompts.txt'), 'r', encoding='utf-8') as file:
        current_prompt = []
        for linha in file:
            if linha.strip() == '---':
                if current_prompt:
                    prompts.append('\n'.join(current_prompt))
                    current_prompt = []
            else:
                current_prompt.append(linha.strip())
        if current_prompt:
            prompts.append('\n'.join(current_prompt))
    return prompts

def salvar_resposta(resposta, numero):
    pasta_respostas = os.path.join('ROTEIRO')
    if not os.path.exists(pasta_respostas):
        os.makedirs(pasta_respostas)

    nome_arquivo = os.path.join(pasta_respostas, f'Parte{numero:03d}.txt')
    with open(nome_arquivo, 'w', encoding='utf-8') as file:
        file.write(resposta)

def concatenar_respostas():
    pasta_respostas = os.path.join('ROTEIRO')
    respostas = sorted([f for f in os.listdir(pasta_respostas) if f.startswith('Parte')])
    nome_arquivo_final = os.path.join(pasta_respostas, 'ROTEIRO_COMPLETO.txt')
    with open(nome_arquivo_final, 'w', encoding='utf-8') as outfile:
        for arquivo in respostas:
            with open(os.path.join(pasta_respostas, arquivo), 'r', encoding='utf-8') as infile:
                outfile.write(infile.read() + '\n\n')

def app_road_map():
    prompts = ler_prompts()
    message_list = []

    for i, prompt in enumerate(prompts, 1):
        print(f"Processando prompt {i}/{len(prompts)}")
        response = get_completion_claude(prompt, message_list)
        content = response.text
        message_list.append({"role": "assistant", "content": content})
        salvar_resposta(content, i)
        time.sleep(1)

    concatenar_respostas()
    print("Processo concluído. Seu roteiro está pronto!")