# Relatório: Prática de Local File Inclusion

Este ataque é realizado explorando a vulnerabiilidade de um site incluindo um arquivo externo malicioso à aplicação principal.

![](screenshots/acess_passwd_file.jpg)

Na realização da atividade prática, foi possível fazer upload de um arquivo usando web shell em um exemplo de servidor vulnerável, o bWAPP.

Segundo o passo a passo proposto pelo tutorial, consegui realizar as seguintes etapas:

1. Baixei o script b374k
2. Gerei o shell backdoor com o comando:
>php -f index.php -- -o shell.php -p raj123

![](screenshots/shell-php.jpg)

3. Acessei a página principal do bWAPP, selecionei a opção 'Unrestricted File Upload'
4. Fiz o upload do arquivo malicioso gerado 'shell.php'

![](screenshots/hack.jpg)

Dessa forma, obtive acesso ao servidor, e através das opções do b374k foi possível obter informações do sistema, listar todos os processos e ter acesso a um terminal para executar comandos e explorar a vulnerabilidade:

Lista de todos os processos:

![](screenshots/process.jpg)

Informações do servidor:

![](screenshots/server_info.jpg)


A atividade prática proposta pelo tutorial sugerem que sejam executados comandos no WebShell. 

5. Consegui obter acesso ao sistema de arquivos do diretório do servidor:

![](screenshots/shell.jpg)

![](screenshots/shell2.jpg)

Realizei o passo a passo do tutorial logo após a apresentação do tutorial. Não tive dificuldades para fazer a instalação das ferramentas e explorar a vulnerabilidade do servidor bWAPP. Foi muito interessante e me mostrou na prática a necessidade de se preocupar com autenticação de páginas na construção de um website.