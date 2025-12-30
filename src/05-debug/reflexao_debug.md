# Reflexão sobre Depuração
1. O que você conseguiu enxergar no debugger que não ficava tão claro apenas
executando o programa normalmente (sem depuração)?

No debugger foi possível observar o valor que cada variável estava assumindo em cada
passo da execução, além disso, ficou mais claro na pilha de chamadas (call stack) a
ordem de chamada e encerramento das funções.

2. Em quais situações você acha mais prático usar o pdb pela linha de comando e
em quais prefere o debugger visual do VS Code?

O pdb é mais prático quando se quer fazer um debugging pontual para quando você já
sabe a região do código que está com problema e não há acesso a interfaces gráficas,
somente linha de comando.
O VS Code é melhor para quando você não sabe exatamente onde está o bug ou precisa
observar muita coisa ao mesmo tempo.

3. Houve algum erro ou comportamento inesperado nos seus exercícios que você só
percebeu por causa da depuração? Descreva brevemente.

Sim. Ao depurar, percebi que algumas funções estavam sendo redefinidas, o que poderia
causar confusão sobre qual comportamento estava sendo executado.