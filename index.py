import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_athletes = pd.read_csv("./athletes.csv") 
df_medals = pd.read_csv("./medals.csv")

########## gráfico 1:  distribuição de atletas por gênero
df_athletes['gender'] = df_athletes['gender'].replace({"Male": "Masculino", "Female": "Feminino"})
athletes_gender_count = df_athletes['gender'].value_counts()

plt.figure(figsize=(8, 6))
athletes_gender_count.plot(kind='bar', color=['darkblue', 'darkred'])

# ajusta a graduação do eixo y
max_value = athletes_gender_count.max()
plt.yticks(np.arange(0, max_value + 500, 500))

# adiciona linhas tracejadas no eixo y
yticks = np.arange(0, max_value + 500, 500)
for tick in yticks:
    plt.axhline(y=tick, color='gray', linestyle='--', alpha=0.2)

plt.title('Distribuição de Atletas por Gênero (M/F)')
plt.xlabel('Gênero')
plt.ylabel('N° de Atletas')
plt.xticks(rotation=0)
plt.show()

########### gráfico 2: distribuição de medalhas por gênero
df_medals['gender'] = df_medals['gender'].replace({"M": "Masculino", "W": "Feminino"})
df_medals_filtered = df_medals[df_medals['gender'].isin(['Masculino', 'Feminino'])]
medals_gender_count = df_medals_filtered['gender'].value_counts()

plt.figure(figsize=(8, 6))
medals_gender_count.plot(kind='bar', color=['darkblue', 'darkred'])

# ajusta a graduação do eixo y
max_value = 600
plt.yticks(np.arange(0, max_value + 100, 100))

# adiciona linhas tracejadas no eixo y
yticks = np.arange(0, max_value + 100, 100)
for tick in yticks:
    plt.axhline(y=tick, color='gray', linestyle='--', alpha=0.2)

plt.title('Distribuição de Medalhas por Gênero (M/F)')
plt.xlabel('Gênero')
plt.ylabel('Número de Medalhas')
plt.xticks(rotation=0)
plt.show()

########## gráfico 3: desempenho das mulheres por país

# pega só as colunas masculino e feminino
df_medals_filtered = df_medals[df_medals['gender'].isin(['Masculino', 'Feminino'])]

# pega todas as medalhas femininas / pega nos 20 principais paises
df_women_medals = df_medals_filtered[df_medals_filtered['gender'] == 'Feminino']
women_medals_country = df_women_medals['country_code'].value_counts().head(20)

plt.figure(figsize=(10, 8))
women_medals_country.plot(kind='bar', color='darkred')
plt.title('Desempenho das Mulheres nos 20 Principais Países')
plt.xlabel('País')
plt.ylabel('N° de Medalhas')
plt.xticks(rotation=45, ha='right')
plt.show()

########## gráfico 4: desempenho esportes individuais x coletivos - feminino

# filtra somente por medalhas femininas
df_women_medals = df_medals[df_medals['gender'] == 'Feminino']

# seta os tipos por event_types
individual_event_types = ['ATH', 'HATH', 'HCOUP']
collective_event_types = ['TEAM', 'HTEAM', 'COUP']

# filtra os dados para eventos individuais e coletivos
individual_events = df_women_medals[df_women_medals['event_type'].isin(individual_event_types)]
collective_events = df_women_medals[df_women_medals['event_type'].isin(collective_event_types)]


# conta o número de medalhas em cada categoria
individual_medals_count = individual_events.shape[0]
collective_medals_count = collective_events.shape[0]

# criaçao do dataframe
performance_comparison_df = pd.DataFrame({
    'Modalidade': ['Individuais (ATH/HATH/HCOUP)', 'Coletivas (TEAM/HTEAM/COUP)'],
    'Número de Medalhas': [individual_medals_count, collective_medals_count]
})

plt.figure(figsize=(8, 6))
performance_comparison_df.set_index('Modalidade').plot(kind='bar', color=['darkred', 'orange'], legend=False)

plt.title('Desempenho Esportes Individuais x Coletivos - Feminino')
plt.xlabel('Modalidade')
plt.ylabel('N° de Medalhas')
plt.xticks(rotation=0)
plt.show()
