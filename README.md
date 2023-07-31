# Jogo do Bicho - Terminal Version 

Esse programa será a base para futuras aplicações!
![Meu projeto (1)](https://github.com/TiaLiliUwU/jogo-do-bicho/assets/72944953/da9570ef-7ee4-4e1e-8e41-5e8080ed7af2)


## Como usar:

Após baixar a release mais recente, abra o arquivo core.py da forma como lhe for mais conveniente e se divirta!

O programa tem suporte para Windows (Power Shell) e sistemas Unix (macOS, Linux etc.).

## Changelog:

### Recursos a serem adicionados nas próximas atualizações:

| - Criação de um sistema de armazenamento de dados |
| :--------------------------------------------------- |
| - Criação de um sistema de pontuações |
| - Melhorias na interface do programa |
| - Refatoração do sistema de apostas e verificações |
| - Compilação e criptografia do algoritmo |

#### [v2.1.0] - 30-07-2023

### Mudanças:

| - Migração do scraper para uma API no algoritmo |
| :--------------------- |
| - Resolução de bug de sorteios |
| - Melhorias na interface do programa |
| - Refatoração do código |

### Bugs conhecidos: 

- Algoritmo:
    - Quando o algoritmo não consegue se conectar ao servidor ntp para pegar as informações de horário o programa crasha.
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