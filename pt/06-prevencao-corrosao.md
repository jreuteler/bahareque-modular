# Prevenção de Corrosão

## Filosofia de Projeto

O sistema de painéis utiliza múltiplos materiais em contato íntimo. Cada interface de materiais é um risco potencial de corrosão. Este capítulo documenta a análise galvânica de cada interface e a estratégia de prevenção.

**Meta de projeto: 80–100 anos sem falha estrutural por corrosão.**

## Série Galvânica (metais relevantes)

Do mais anódico (corrói primeiro) ao mais catódico (protegido):

1. Zinco (revestimento de galvanização)
2. Alumínio (tela contra insetos)
3. Aço carbono (estrutura, tiras de fixação)
4. Aço inoxidável (parafusos)

Quando dois metais estão em contato elétrico na presença de um eletrólito (umidade), o metal mais anódico corrói preferencialmente. Este é o princípio da corrosão galvânica.

## Análise de Interfaces

### 1. Estrutura de Aço <-> Argamassa

- **Contato:** Direto — a argamassa é vertida sobre e ao redor da estrutura de aço galvanizado
- **Nível de risco:** BAIXO
- **Análise:** O ambiente alcalino da argamassa de cimento (pH 12–13) passiva o revestimento de zinco, formando uma camada estável de óxido de zinco. Esta é na verdade uma combinação *benéfica* — a argamassa protege o zinco, e o zinco protege o aço. O mesmo princípio das barras de aço no concreto armado.
- **O aditivo pozolânico** gradualmente reduz o pH da argamassa para 10–11 ao longo de décadas. Isso permanece bem dentro da faixa de passivação do zinco.
- **Prevenção:** Galvanização a quente conforme ISO 1461 (mínimo 85 μm). Nenhuma medida adicional necessária.

### 2. Parafusos de Aço Inoxidável <-> Estrutura Galvanizada

- **Contato:** Direto — os parafusos passam pela alma galvanizada
- **Nível de risco:** BAIXO-MÉDIO
- **Análise:** O aço inoxidável é catódico em relação ao zinco. Em teoria, isso acelera a corrosão do zinco no ponto de contato. Na prática, o encapsulamento em argamassa elimina a umidade contínua (o eletrólito), e o revestimento de zinco no furo do parafuso é uma área sacrificial — o zinco ao redor o protege catodicamente.
- **Prevenção:** Usar parafusos de aço inoxidável A2 (304). A cabeça do parafuso é coberta pela tira de fixação e argamassa. Sem caminho para umidade.

### 3. Tela de Galinheiro <-> Estrutura de Aço

- **Contato:** Indireto — a tela de galinheiro é grampeada sobre a face de argamassa, separada da estrutura por 30+ mm de argamassa
- **Nível de risco:** NENHUM
- **Análise:** Ambas são de aço galvanizado. Sem diferença de potencial galvânico. Separadas pela camada de argamassa. Sem problema.

### 4. Tela de Alumínio <-> Estrutura de Aço

- **Contato:** Indireto — a tela de alumínio fica entre a tela de galinheiro e a argamassa, separada da estrutura por 30+ mm
- **Nível de risco:** NENHUM
- **Análise:** O alumínio é anódico em relação ao aço (ele correria primeiro em contato direto). Mas não há contato metal-metal direto — a camada de argamassa proporciona isolamento elétrico completo.
- **Prevenção:** Garantir que a tela de alumínio não faça contato direto com a estrutura de aço durante a instalação. A camada de argamassa cuida disso naturalmente.

### 5. Tela de Alumínio <-> Tela de Galinheiro (Aço Galvanizado)

- **Contato:** Direto — as camadas de tela se tocam durante a instalação
- **Nível de risco:** BAIXO
- **Análise:** Existe algum potencial galvânico. Mas ambas são embebidas em argamassa após a instalação, eliminando o caminho de umidade. A tela de alumínio é uma camada fina sacrificial — mesmo que ocorra alguma corrosão nos pontos de contato, a tela de galinheiro estrutural permanece intacta.
- **Prevenção:** Nenhuma ação necessária. O encapsulamento em argamassa é suficiente.

### 6. Tira de Fixação <-> Alma da Estrutura

- **Contato:** Direto — a tira de fixação é parafusada contra a alma através das tiras de bambu
- **Nível de risco:** NENHUM
- **Análise:** Ambas são de aço carbono galvanizado a quente. Mesmo material, mesmo revestimento. Sem potencial galvânico.

### 7. Estrutura de Aço <-> Tiras de Bambu

- **Contato:** Direto — as tiras de bambu encostam na alma galvanizada
- **Nível de risco:** BAIXO
- **Análise:** O bambu não é um metal — nenhuma corrosão galvânica é possível. A preocupação é a umidade sendo conduzida pelo bambu criando uma zona persistentemente úmida no aço. O encapsulamento em argamassa elimina isso selando a interface. O tratamento com borato também reduz a absorção de umidade.

## Fatores Ambientais

### Ambientes Costeiros (< 1 km do mar)

O ar carregado de sal acelera dramaticamente o consumo de zinco. Em ambientes costeiros:
- Aumentar a espessura de galvanização para 120+ μm
- Usar parafusos de aço inoxidável 316L (em vez de 304)
- Considerar revestimento epóxi adicional na estrutura antes da galvanização
- Vida útil esperada da estrutura em zona costeira: 40–60 anos (vs 80–100 no interior)

### Alta Pluviosidade (> 2.000 mm/ano)

- Garantir beiral adequado do telhado (mínimo 1,5 m) para manter a chuva longe das superfícies da parede
- O reboco de cal atua como camada sacrificial — renovar a cada 10–15 anos em zonas de alta pluviosidade
- O interior da parede (encapsulado em argamassa) não é afetado pela chuva

### Umidade Tropical

- A respirabilidade do reboco de cal é crítica — permite que a umidade passe através em vez de ficar presa
- NÃO sele a parede com tinta ou revestimento impermeabilizante — isso retém umidade e acelera a degradação
- A parede deve respirar: somente caiação

## Resumo

| Interface | Risco | Prevenção | Manutenção |
|-----------|-------|-----------|------------|
| Estrutura de aço na argamassa | Baixo | Galvanização a quente | Nenhuma (inspecionar aos 40 anos) |
| Parafusos inox na estrutura galvanizada | Baixo-Médio | Inox A2, encapsulamento em argamassa | Nenhuma |
| Tela de galinheiro → estrutura | Nenhum | Mesmo material, separação por argamassa | Nenhuma |
| Tela de alumínio → estrutura | Nenhum | Isolamento pela argamassa | Nenhuma |
| Tela de alumínio → tela de galinheiro | Baixo | Encapsulamento em argamassa | Nenhuma |
| Tira de fixação → estrutura | Nenhum | Mesmo material | Nenhuma |
| Aço → bambu | Baixo | Tratamento com borato, encapsulamento em argamassa | Nenhuma |

**A proteção contra corrosão do sistema se baseia em três camadas: galvanização (primária), encapsulamento em argamassa (secundária) e reboco de cal (terciária/sacrificial). A falha de qualquer camada isolada não compromete o sistema.**
