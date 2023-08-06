# Jogo do Bicho - Terminal Version 

Por favor, leia a seção __about__ deste repositório! 
![Meu projeto (1)](https://github.com/TiaLiliUwU/jogo-do-bicho/assets/72944953/da9570ef-7ee4-4e1e-8e41-5e8080ed7af2)


## Como usar:

Caso não tenha o python instalado, baixe a versão mais recente (no Windows habilite o python to PATH).
No seu terminal, instale as seguintes bibliotecas antes de executar o jogo (espero que não falte nenhum):

```shell
pip install questionary
pip install rich
pip install pyfiglet
pip install requests_html
pip install pytz
pip install requests
pip install ntplib
```

Após baixar a release mais recente, abra o arquivo core.py no terminal e se divirta!


Windows:
```shell
py core.py
```

Unix:
```sh
python3 core.py
```

O programa tem suporte para Windows (PowerShell) e sistemas Unix (macOS, Linux etc.).

## Changelog:

### Recursos a serem adicionados nas próximas atualizações:

| - Resolução do bug de sorteio |
| :--------------------------------------------------- |
| - Criação de um sistema de pontuações |
| - Melhoria no sistema de armazenamento de dados |
| - Compilação e criptografia do algoritmo |
| - Melhorias na interface do programa |
| - Criação do script de instalação dos componentes necessários |

#### [v3.0.0] - 05-08-2023

### Mudanças:

| - Menus principais interativos |
| :--------------------- |
| - Refatoração do sistema de apostas e verificações |
| - Melhorias na estéticas do programa |
| - Vizualização das apostas para comparar com o sorteio |
| - Criação do banco de dados para Apostas e Sorteios (ainda em desenvolvimento) |
| - Resolução do BUG em get_local, que causava crash por não se conectar ao servidor de data |
| - Adição de Easter Egg |

### Bugs conhecidos: 

- Sorteio:
    - Eu pensei ter resolvido o bug dos múltiplos sorteios, mas algo ainda está fora. Estudarei por mais tempo o algoritmo para elaborar uma solução definitiva.

#### [v2.1.0] - 30-07-2023

### Mudanças:

| - Migração do scraper para uma API no algoritmo |
| :--------------------- |
| - Resolução de bug de sorteios |
| - Melhorias na interface do programa |
| - Refatoração do código |

### Bugs conhecidos: 

- Sincronização da data:
    - Precisa ser desenvolvido um mecanismo que impeça o programa de crashar quando não obter resposta do servidor.
- Sorteio:
    - O modo como a data é passada para obter os dados de previsão do tempo está incorreto, ocasionando um bug no dia 31.

#### [v2.0.0] - 28-07-2023

### Mudanças:

| - Criação de um algoritmo de geração procedural de apostas |
| :--------------------- |
| - Refatoração do código |

### Bugs conhecidos: 

- Sorteios:
    - Ainda estou terminando a lógica necessária para extrair os dados corretos de geração procedural. Por conta disso estão ocorrendo 3 sorteios quando na verdade deveriam ser 2. Acredito que a sincrônia se mantenha, contudo o resultado apresentado entre 00h e 12h deveria ser identico ao resultado apresentado entre 18h e 23:59h do dia anterior.

#### [v1.2.0] - 23-07-2023

### Mudanças:

| - Apostas em números funcionais |
| :--------------------- |
| - Refatoração do código |

#### [v1.1.0] - 22-07-2023

### Mudanças:

| - Refatoração do código |
| :--------------------- |
|  |

UwU