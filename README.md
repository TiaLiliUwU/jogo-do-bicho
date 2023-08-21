# Jogo do Bicho - Terminal Version 

Por favor, leia a seção __about__ deste repositório! 
![Meu projeto (1)](https://github.com/TiaLiliUwU/jogo-do-bicho/assets/72944953/46a62d04-cea2-4acb-a705-375d80a13d1f)


## Como usar:

Caso não tenha o python instalado, baixe a versão mais recente (no Windows habilite o python to PATH).

No seu terminal, instale as seguintes bibliotecas antes de executar o jogo (espero que não falte nenhuma):

(Para v3.1.1)
```shell
pip install questionary
pip install rich
pip install pyfiglet
pip install requests_html
pip install pytz
pip install ntplib
pip install tqdm
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

| - Criação de um sistema de pontuações |
| :--------------------------------------------------- |
| - Criação de um sistema apostas programadas |
| - Compilação e criptografia do algoritmo e arquivos relacionados |
| - Melhorias na interface do programa |
| - Criação do script de instalação dos componentes necessários |
| - Criação do script de download dos bancos de dados necessários |
| - Melhoria no sistema de armazenamento de dados |

### [v3.1.1] - 21-08-2023

#### Mudanças:

| - Bugs da verificação dos sorteios anteriores consertados |
| :--------------------- |
| - Bug get_local consertado |
| - Adição de interface de seleção dos dados de sorteios anteriores |
| - Melhoria no sistema de armazenamento de sorteios |
| - Melhorias na interface do programa |
| - Refatoração de código |


### Bugs conhecidos: 

- Ano bissexto:
    - Ainda preciso desenvolver o comportamento do algoritmo para anos bissextos, não que esse bug vá aparecer tão em breve, mas é importante relatar para corrigir depois.
- Função de sorteios:
    - Preciso desenvolver uma forma automatizada de obter os bancos de dados necessários para o funcionamento do programa a partir do dia 01/01/2024. Então, até a versão 3.1.1, esse bug permanece.


### Notas sobre a v3.1.1

Vocês não fazem IDEIA da quantidade de bugs que surgiram no meio do caminho e eu tive que resolver. Foi bug nos sorteios, bug nas apostas, bug na interface etc. Sério, que ódio, eu devo ter corrigido uns 10 bugs ao todo. Como a maioria desses bugs surgiu enquanto eu arrumava outros bugs, não vou deixar eles em nenhuma lista de bugs conhecidos, mas saibam que eles existiram E EU OS ODEIO!

Talvez alguns desses bugs sejam decorrente de problemas nas versões anteriores, então sugiro usar sempre a mais recente.

### [v3.1.0] - 10-08-2023

#### Mudanças:

| - Recriação do algoritmo de geração dos sorteios |
| :--------------------- |
| - Refatoração de código |
| - Bug de sorteios resolvido |

### Bugs conhecidos: 

- get_local:
    - Errei, fui mlk, o bug não foi resolvido, só está mostrando que não conseguiu os dados e em seguida crasha. Quando estiver com paciência eu conserto (se você não rodar o programa 1M de vezes por dia, dificilmente verá esse bug).
- Ano bissexto:
    - Ainda preciso desenvolver o comportamento do algoritmo para anos bissextos, não que esse bug vá aparecer tão em breve, mas é importante relatar para corrigir depois.
- Função de sorteios:
    - Preciso desenvolver uma forma automatizada de obter os bancos de dados necessários para o funcionamento do programa a partir do dia 01/01/2024. Então, até a versão 3.1.0, esse bug permanece.
- Verificação de sorteios:
    - Esqueci de consertar o código que puxa a verificação do banco de dados de sorteios passados.
    - Caso o usuário selecione um valor que não consta no banco de dados, o programa crash.

### [v3.0.0] - 05-08-2023

#### Mudanças:

| - Menus principais interativos |
| :--------------------- |
| - Refatoração do sistema de apostas e verificações |
| - Melhorias na estéticas do programa |
| - Vizualização das apostas para comparar com o sorteio |
| - Criação do banco de dados para Apostas e Sorteios (ainda em desenvolvimento) |
| - ~~Resolução do BUG em get_local, que causava crash por não se conectar ao servidor de data~~ |
| - Adição de Easter Egg |

### Bugs conhecidos: 

- Sorteio:
    - Eu pensei ter resolvido o bug dos múltiplos sorteios, mas algo ainda está fora. Estudarei por mais tempo o algoritmo para elaborar uma solução definitiva.

### [v2.1.0] - 30-07-2023

#### Mudanças:

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

### [v2.0.0] - 28-07-2023

#### Mudanças:

| - Criação de um algoritmo de geração procedural de apostas |
| :--------------------- |
| - Refatoração do código |

### Bugs conhecidos: 

- Sorteios:
    - Ainda estou terminando a lógica necessária para extrair os dados corretos de geração procedural. Por conta disso estão ocorrendo 3 sorteios quando na verdade deveriam ser 2. Acredito que a sincrônia se mantenha, contudo o resultado apresentado entre 00h e 12h deveria ser identico ao resultado apresentado entre 18h e 23:59h do dia anterior.

### [v1.2.0] - 23-07-2023

#### Mudanças:

| - Apostas em números funcionais |
| :--------------------- |
| - Refatoração do código |

### [v1.1.0] - 22-07-2023

#### Mudanças:

| - Refatoração do código |
| :--------------------- |
|  |

UwU