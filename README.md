# Introdução

Este é um projeto destinado a explorar diferentes abordagens de tipagem em Python, usando a simples operação de soma (2 + 3) como exemplo. Embora o resultado matemático seja o mesmo para todos, as implicações em termos de tipagem podem variar significativamente. Esta discussão é relevante para desenvolvedores que desejam compreender as nuances da tipagem em Python e como ela pode impactar seus projetos.

# Quanto vale 2 + 3?

Para uma pessoa comum, a resposta é simples: 5. No entanto, para um desenvolvedor, a resposta é...

...depende!

# Abordagens de Tipagem

Neste projeto, examinaremos quatro estratégias distintas para realizar a operação 2 + 3 em Python, cada uma delas com suas próprias implicações:

## 1) Funções sem tipagem explícita

Nesta abordagem, adotamos a simplicidade do Python, onde os valores de entrada podem assumir diversas formas, como inteiros, strings ou listas. Isso proporciona uma flexibilidade considerável, sendo especialmente útil em cenários de prototipagem rápida ou para scripts mais simples. Aqui, não há necessidade de declarar tipos, classes ou objetos.

## 2) Uso de Anotações de Tipo (Type Hint)

Nesta estratégia, introduzimos anotações de tipo (Type Hint) para indicar qual tipo de valor é esperado como entrada. Contudo, é crucial compreender que essas anotações não alteram o comportamento da função em si. Elas servem como sugestões para outros desenvolvedores e ferramentas de análise estática, mas não impõem validações ou restrições aos valores de entrada.

## 3) Utilização de Validação com Pydantic

Neste cenário, fazemos uso da biblioteca Pydantic para VALIDAR e IMPOR restrições sobre as entradas, sempre que possível, antes de efetuar a operação. Isso garante a coerência do tipo de dado no resultado. Essa abordagem se destaca em aplicações como APIs e sistemas web, onde os dados de entrada podem ser inesperados e potencialmente perigosos. Assim, evitamos a inserção de informações inapropriadas em nosso banco de dados ou relatórios

## 4) Validação Rígida com Pydantic (Modo Strict)

Com a configuração de tipagem estrita do Pydantic, não há espaço para ambiguidades. Se o tipo de entrada for INT, ele DEVE SER de fato um inteiro. Essa abordagem é essencial em contextos críticos, como sistemas financeiros, nos quais a precisão e consistência dos dados são de suma importância.

# Conclusão

Resumindo, a escolha da abordagem de tipagem em Python deve ser orientada pelas necessidades específicas de cada projeto. A questão não se resume apenas à obtenção da resposta correta, mas também à garantia de que os requisitos do projeto sejam satisfeitos de maneira eficaz.
