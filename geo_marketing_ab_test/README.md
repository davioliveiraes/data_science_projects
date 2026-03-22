# Teste A/B em Campanha de Geoespacial Marketing Analytics

## Finalidade

Este projeto realiza um **Teste A/B** para avaliar se a localização geográfica dos usuários influencia a taxa de conversão em uma campanha de marketing. A análise investiga se existe diferença estatisticamente significativa entre dois grupos (A e B) distribuídos em diferentes regiões geográficas.

O dataset contém 1.000 registros com informações de `usuario_id`, `grupo` (A ou B), `latitude`, `longitude` e `conversao` (0 ou 1).

### Resultados Obtidos

| Métrica | Grupo A | Grupo B |
|---|---|---|
| Taxa de Conversão | 30,00% | 31,57% |

- **Teste de Shapiro-Wilk**: Os dados de ambos os grupos **não** seguem distribuição normal (p-value ≈ 0).
- **Teste de Levene**: As variâncias dos grupos são homogêneas (p-value = 0.59).
- **Teste de Mann-Whitney U**: Não há diferença estatisticamente significativa entre os grupos (p-value = 0.59).

**Conclusão**: Não há evidências estatísticas de que a região geográfica influencia a taxa média de conversão entre os grupos A e B.

## Tecnologias Utilizadas

- **Python 3**
- **Jupyter Notebook** - ambiente interativo para análise
- **Pandas** - manipulação e análise de dados
- **NumPy** - operações numéricas e reprodutibilidade (seed)
- **Matplotlib** - visualização da distribuição geográfica
- **Seaborn** - visualizações estatísticas
- **SciPy** - testes estatísticos (Shapiro-Wilk, Levene, t de Student, Mann-Whitney U)

## Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/davioliveiraes/data_science_projects.git
   cd data_science_projects/geo_marketing_ab_test
   ```

2. Crie e ative um ambiente virtual:
   ```bash
      conda create -n geo_marketing_ab_test python=3.13
      conda activate geo_marketing_ab_test
   ```

3. Instale as dependências:
   ```bash
   pip3 install -r requirements.txt
   ```

4. Execute o notebook:
   ```bash
   jupyter notebook geo_marketing_ab_test.ipynb
   ```

## Conceitos Aprendidos

- **Teste A/B**: Metodologia para comparar duas variantes e determinar qual apresenta melhor desempenho com base em evidências estatísticas.
- **Teste de Hipóteses**: Formulação de hipótese nula (H0) e hipótese alternativa (H1), definição de nível de significância (α = 0.05) e tomada de decisão com base no valor-p.
- **Validação de Suposições Estatísticas**: Verificação de normalidade (Shapiro-Wilk) e homogeneidade de variâncias (Levene) antes de escolher o teste adequado.
- **Testes Paramétricos vs. Não Paramétricos**: Quando os dados não atendem às suposições de normalidade, deve-se optar por testes não paramétricos como o Mann-Whitney U em vez do teste t de Student.
- **Análise Geoespacial**: Uso de coordenadas geográficas (latitude/longitude) para avaliar o impacto da localização em campanhas de marketing.
- **Visualização de Dados Geográficos**: Representação da distribuição espacial dos grupos através de gráficos de dispersão.

## Referências

- [SciPy - Testes Estatísticos](https://docs.scipy.org/doc/scipy/reference/stats.html)
- [Pandas - Documentação Oficial](https://pandas.pydata.org/docs/)
- [Matplotlib - Documentação Oficial](https://matplotlib.org/stable/contents.html)
- [Teste de Mann-Whitney U - Wikipedia](https://en.wikipedia.org/wiki/Mann%E2%80%93Whitney_U_test)
- [Teste de Shapiro-Wilk - Wikipedia](https://en.wikipedia.org/wiki/Shapiro%E2%80%93Wilk_test)
- [Data Science Academy - Business Analytics e Machine Learning](https://www.datascienceacademy.com.br/)

## Autor

**Davi Oliveira**
