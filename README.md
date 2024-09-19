# Crie e ative um ambiente virtual

(Opcional, mas recomendado)

Para criar:
`python -m venv venv`

Para ativar No Windows:
`venv\Scripts\activate`

Execute o comando pip para instalar as dependências listadas no requirements.txt:
`pip install -r requirements.txt`

Se você quiser criar um arquivo requirements.txt para seu próprio projeto, pode usar o comando:
`pip freeze > requirements.txt`

Isso listará todas as dependências atualmente instaladas no seu ambiente.

## Modelos Claude

<https://docs.anthropic.com/en/docs/about-claude/models#model-comparison>

## Prompts

O arquivo prompts.txt suporta prompts complexos e multilinha. Cada prompt é separado por uma linha contendo apenas "---".

### Para usar este sistema

Coloque seus prompts no arquivo app_road_map/prompts.txt, separando cada prompt com uma linha contendo apenas "---".

Configure sua chave API no arquivo .env

Execute o script principal com python PLAY.py.
