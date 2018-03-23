# Relatório: Vigenere

- A mensagem descriptografada se encontra no arquivo results.txt, que contem apenas algumas das permutações (o arquivo com todas elas tem um tamanho de quase 945 MB)

Foi feita a implementação do algoritimo de acordo com as instruções para o método de descriptografia, que seguiram basicamente essas etapas:

1. Copiei o texto do arquivo texto_cifrado_amor.txt
2. Implementei o método para normalizar a chave e a mensagem cifrada
3. Implementei o método de descriptografar uma mensagem com uma determinada chave
4. Adicionei ao método main() a leitura e escrita dos arquivos .txt
5. Utilizei a ferramenta crunch para gerar um wordlist de palavras com 4 letras e salvá-las no arquivos words.txt
6. Implementei uma instrução para procurar a palavra 'AMOR' nos resultados das chaves de 4 letras que encontrar as possibilidades das 4 letras inciais da chave e escrevê-las no arquivo attempts.txt
7. Implementei mais uma instrução para percorrer estas possibilidades e encontrar as 4 ultimas letras da chave, analisando o arquivo results.txt para descobrir qual delas retornou a mensagem descriptografada e com a chave correta.

Consegui implementar o algoritimo sozinho. No dia, vários colegas estavam estudando e discutindo juntos para implementar o algorítimo (cada um em linguagem diferente de sua preferência). Como disse no relatório da atividade_01, estas atividades são também os meu primeiro contato com python, por isso, algumas coisas básicas da linguagem me deram trabalho e me fizeram gastar um total de 5 horas para implementa-lo totalmente.

Mas, no meio do processo, me deparei com um erro no meu código que não conseguia ler mais do que uma linha no arquivo .txt   ):

Por isso gastei mais tempo ainda na resolução desse erro, e de ajuda dos meus colegas que estavam discutindo o algoritimo para resolver os problemas com a manipulação de arquivos em python e implementar corretamente a linha de código que determina como a mensagem será descriptografa segundo a fórmula.

Por fim, em comparação com a chave descoberta por meus colegas, testei e vi que o algoritimo estava implementado corretamente e que a mensagem foi descriptografada. De tudo que foi feito eu acho que consigo reproduzir. Eu não tinha conseguido encontrar a chave sozinho antes de resolver o bug no código, mas depois de resolvê-lo consegui encontrar a chave e validar o funcionamento do algoritimo. Infelizmente tive muita dificuldade na implementação. Mas extamente por isso, o aproveitamento da atividade foi bom para mim. Aprendi bastante.