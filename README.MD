Para resolver o problema, calcula-se o valor que cada email deverá pagar utilizando deivisão euclidiana, que divide o
valor total dos itens pelo total de emails, e o resto da divisão é armazenado em uma variável n. Após as divisões serem
realizadas, o valor de n é dividido entre os n ultimos emails da lista. Por ser uma divisão euclidiana, o valor restante
nunca será maior que o valor total de emails. Sendo assim, cada email só poderá receber no máximo mais 1 centavo do
resultado da divisão euclidiana.


Para rodar o projeto: basta instalar a versão 3.9.0 do python e rodar o arquivo main.py. Para testar mais valores, basta
substituir os valores das variáveis item_list e email_list no arquivo main.py.