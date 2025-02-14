# Matrix Rain Effect

Um efeito visual estilo Matrix criado com Python e Pygame, gerenciado com Poetry.

## 🚀 Características

- Animação suave de caracteres estilo Matrix
- Caracteres em Katakana japonês e números
- Efeito de degradê nas "gotas" de caracteres
- Velocidade e tamanho aleatórios para cada gota
- Controles para sair (ESC ou fechar janela)

## 📋 Pré-requisitos

- Python 3.8 ou superior
- Poetry (gerenciador de dependências)

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone <seu-repositorio>
cd matrix-rain
```

2. Instale as dependências com Poetry:
```bash
poetry install
```

## 💻 Como Executar

Existem duas maneiras de executar o programa:

1. Usando o módulo Python diretamente (recomendado):
```bash
poetry run python -m matrix_rain.main
```

2. Ou usando o script configurado no Poetry:
```bash
poetry run matrix
```

## 🎮 Controles

- `ESC` - Sair do programa
- Fechar a janela - Encerrar o programa

## 📁 Estrutura do Projeto
```
matrix-rain/
├── pyproject.toml         # Configuração do Poetry
├── poetry.lock           # Versões fixas das dependências
├── README.md            # Esta documentação
└── matrix_rain/         # Pacote principal
    ├── __init__.py     # Arquivo de inicialização do pacote
    └── main.py         # Código principal da aplicação
```

## 🛠️ Construído Com

- [Python](https://www.python.org/) - Linguagem de programação
- [Pygame](https://www.pygame.org/) - Biblioteca para jogos e gráficos
- [Poetry](https://python-poetry.org/) - Gerenciamento de dependências

## ✏️ Personalização

Você pode modificar algumas constantes no início do arquivo `main.py`:

- `WIDTH` e `HEIGHT` - Dimensões da janela
- `FONT_SIZE` - Tamanho dos caracteres
- `GREEN` e `BLACK` - Cores utilizadas
- Modificar a string `characters` na classe `Drop` para usar diferentes caracteres

## 📝 Licença

Este projeto está sob a licença MIT - veja o arquivo [LICENSE.md](LICENSE.md) para detalhes.

## 🤝 Contribuindo

1. Faça o Fork do projeto
2. Crie sua Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request
