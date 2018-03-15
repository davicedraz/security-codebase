## Perguntas da aula S03E02

As respostas foram pesquisadas em grupo pelos alunos:
- Davi Cedraz
- Samuel Alves
- Ernandes Azevedo

#### 1. O que são chaves simétricas e assimétricas?

Simétrica: É uma forma de criptossistema em que a criptografia e a decriptografia são realizadas usando a mesma chave.
Assimétrica: A criptografia de chave pública ou criptografia assimétrica é um método de criptografia que utiliza um par de chaves: uma chave pública e uma chave privada. A chave pública é distribuída livremente para todos os correspondentes via e-mail ou outras formas, enquanto a chave privada deve ser conhecida apenas pelo seu dono.
Quais as diferenças

Na chave simétrica, tanto a criptografia quando a descriptografia são feitas através da mesma chave. Já a chave assimétrica utiliza uma chave pública para criptografar dados onde somente a chave privada é capaz de descriptografar.

#### 2. Dê exemplo reais de algoritmos:

Simétrico: A cifra de playfair é um exemplo de uso da chave simétrica.
Assimétrico: O RSA envolve um par de chaves, uma chave pública que pode ser conhecida por todos e uma chave privada que deve ser mantida em sigilo. Toda mensagem cifrada usando uma chave pública só pode ser decifrada usando a respectiva chave privada. A criptografia RSA atua diretamente na internet, por exemplo, em mensagens de emails, em compras on-line e o que você imaginar; tudo isso é codificado e recodificado pela criptografia RSA. Fundamenta-se em teorias clássicas dos números.

#### 3. Dê um exemplo de onde elas são usadas em conjunto:

*Não conseguimos responder esta pergunta*

#### 4. O que é um KDC? Dê um exemplo real:

https://www.gta.ufrj.br/grad/07_1/kerberos/KeyDistributionCenter(KDC).html

O Kerberos é um protocolo de autenticação da rede concebido para fornecer uma autenticação sólida a aplicações de cliente/servidor através da utilização de criptografia de chaves secretas.
Com o Kerberos, um cliente (geralmente, um utilizador ou um serviço) envia um pedido de uma senha ao KDC. O KDC cria uma senha de concessão de senhas (TGT, ticket-granting ticket) para o cliente, codifica-a utilizando a palavra-passe do cliente como chave e envia a TGT codificada de novo ao cliente. Em seguida, o cliente tenta descodificar a TGT, utilizando a respectiva palavra-passe. Se o cliente descodificar com êxito a TGT (i.e., se o cliente tiver fornecido a palavra-passe correcta), esta mantém a TGT descodificada, que indica a prova da identidade do cliente.
As senhas têm um período de tempo de disponibilidade. O Kerberos requer que os relógios dos sistemas centrais envolvidos estejam sincronizados. Se o relógio da HMC não estiver sincronizado com o relógio do servidor de KDC, a autenticação falhará.
 O KDC, então, gera uma mensagem incluindo duas componentes:
Uma chave de sessão (session key), a qual é codificada com uma chave secreta do usuário.
O ticket-granting ticket, (TGT), que inclui uma cópia da chave de sessão.
	
#### 5. Como funciona o GPG?

https://www.ibm.com/developerworks/community/blogs/752a690f-8e93-4948-b7a3-c060117e8665/entry/be-a-ba_do_gpg_parte_1_crie_sua_chave_hoje_mesmo?lang=en

#### 6. O que é um ICP?

Infraestrutura de Chaves Públicas Brasileira (ICP Brasil) é um conjunto de tecnologias (técnicas, práticas e procedimentos) que garante às transações e aos documentos eletrônicos a segurança por meio do uso de um par de chaves. Uma delas é pública (de conhecimento geral), e a outra, privada (de conhecimento somente do proprietário), cujos dados estão consolidados em um “certificado digital”.
A tramitação de documento eletrônico oficial somente acontecerá quando devidamente certificado por entidade integrante da infraestrutura governamental e classificado quanto ao nível de segurança.	

#### 7. Porque dá erro de certificado em alguns sites? inclusive no site da Caixa?

O certificado é um protocolo que garante que os usuários que visitam seu site naveguem em um ambiente seguro. A comunicação entre o site e servidor fica protegida com um certificado criptografado, impedindo que os dados sejam interceptados através de phishing e sites fraudulentos. 

Muitas vezes, esse problema pode ocorrer por causa de um ataque de vírus. O vírus pode agir trocando letras por números, isto é, quando você digita um endereço o vírus troca todas as letras por números ou troca o IP do Google por outro. Assim, o site não pode mais abrir sua página, pois provoca erro de certificado. 

Esse problema ocorre no site da Caixa porque a mesma não se regularizou como um "site confiável" e seu certificado não é automaticamente reconhecido pelos navegadores.
