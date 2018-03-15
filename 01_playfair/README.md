# Relatório: Playfair

Como proposto pela atividade, a implementação desse algoritimo foi realizada em dupla, com o colega Gleydson Rodrigues (https://github.com/gleydson)

No início, estranhei a escolha do meu colega pela linguagem python para implementar o algoritimo, pois nunca tinha tido contato antes. Mas logo percebi que a sintaxe simples, os tipos e as estruturas não seriam um problema, logo, essa atividade serviu como um ótimo "hello world" de python para mim.

Começamos discutindo como "traduzir" os passos necessários para normalizar a mensagem, a chave, e o processo de criptografar e descriptografar. Decidimos trazer "do mundo real" para o código todos os elementos importantes, como: o **alfabeto** a **matriz (linhas e colunas)** a **chave** e a **mensagem**. A partir disso, foi possível pensar em quais funções seriam necessárias.

O meu colega possui um conhecimento maior sobre implementação de algoritmos, o que foi essencial para encontrar soluções que eu não conseguiria sozinho. Por exemplo: utilizar mod % para dividir as colunas e montar a matriz da matriz; dividir as letras pares em variáveis individuais através do seu índice na matriz.

Sendo assim, dividimos a implementação das funções necessárias, onde mais especificamente fiquei responsável pelo método de desencriptografar a mensagem encriptada, e chegamos a soluções parecidas discutindo e implementando o código juntos no mesmo ambiente.

