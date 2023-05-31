import json
import requests
import dtale as dt
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA
from sklearn.neural_network import MLPRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.compose import TransformedTargetRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler, KBinsDiscretizer
from sklearn.model_selection import train_test_split, GridSearchCV

# Récupération des données
url = 'https://disease.sh/v3/covid-19/countries'
response = requests.get(url)
data = json.loads(response.text)

df = pd.DataFrame(data=data)

# Affiche des colonnes du dataset
print(df.columns)

print('---------------------------------------------------------')

# Affichage des informations sur le dataset
print(df.info())

print('---------------------------------------------------------')

print(df.head())

print('---------------------------------------------------------')

# Affichage des statistiques descriptives du dataset
print(df.describe())

print('---------------------------------------------------------')

dt.show(df)

# Exclusion des colonnes non-numériques
num_df = df.select_dtypes(include=['float64', 'int64'])

# Affichage de la matrice de corrélation entre les variables numériques
corr = num_df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Matrice de corrélation entre les variables numériques')
plt.show()

# Tri des données les plus corrélées
sorted_corr = corr.unstack().sort_values(kind='quicksort').drop_duplicates()
highest_corr = sorted_corr[sorted_corr != 1.0][-10:]

# Affichage des données les plus corrélées
print("Les données les plus corrélées :\n" + str(highest_corr))

print('---------------------------------------------------------')

# Tri des données les moins corrélées
lowest_corr = sorted_corr[:10]

# Affichage des données les moins corrélées
print("\nLes données les moins corrélées :\n" + str(lowest_corr))

print('---------------------------------------------------------')

# Affichage de la distribution du nombre de cas dans les différents pays
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='cases', bins=50)
plt.title('Distribution du nombre de cas dans les différents pays')
plt.xlabel('Nombre de cas')
plt.ylabel('Nombre de pays')
plt.show()

# Affichage de la distribution du nombre de morts dans les différents pays
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='deaths', bins=50)
plt.title('Distribution du nombre de morts dans les différents pays')
plt.xlabel('Nombre de morts')
plt.ylabel('Nombre de pays')
plt.show()

# Affichage de la distribution du nombre de guérisons dans les différents pays
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='recovered', bins=50)
plt.title('Distribution du nombre de guérisons dans les différents pays')
plt.xlabel('Nombre de guérisons')
plt.ylabel('Nombre de pays')
plt.show()

# Affichage de la distribution de la population dans les différents pays
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='population', bins=50)
plt.title('Distribution de la population dans les différents pays')
plt.xlabel('Population')
plt.ylabel('Nombre de pays')
plt.show()

# Affichage des 20 pays avec le plus grand nombre de cas
top_20_cases = df[['country', 'cases']].sort_values('cases', ascending=False).head(20)
plt.figure(figsize=(10, 6))
sns.barplot(data=top_20_cases, x='cases', y='country', palette='coolwarm')
plt.title('20 pays avec le plus grand nombre de cas')
plt.xlabel('Nombre de cas')
plt.ylabel('Pays')
plt.show()

# Affichage des 20 pays avec le plus grand nombre de morts
top_20_deaths = df[['country', 'deaths']].sort_values('deaths', ascending=False).head(20)
plt.figure(figsize=(10, 6))
sns.barplot(data=top_20_deaths, x='deaths', y='country', palette='coolwarm')
plt.title('20 pays avec le plus grand nombre de morts')
plt.xlabel('Nombre de morts')
plt.ylabel('Pays')
plt.show()

# Affichage des 20 pays avec le plus grand nombre de guérisons
top_20_recovered = df[['country', 'recovered']].sort_values('recovered', ascending=False).head(20)
plt.figure(figsize=(10, 6))
sns.barplot(data=top_20_recovered, x='recovered', y='country', palette='coolwarm')
plt.title('20 pays avec le plus grand nombre de guérisons')
plt.xlabel('Nombre de guérisons')
plt.ylabel('Pays')
plt.tight_layout()
plt.show()

# Création d'une colonne pour le taux de mortalité
df['mortality_rate'] = df['deaths'] / df['cases']

# Affichage des 20 pays avec le plus grand taux de mortalité
top_20_mortality_rate = df[['country', 'mortality_rate']].sort_values('mortality_rate', ascending=False).head(20)
plt.figure(figsize=(10, 6))
sns.barplot(data=top_20_mortality_rate, x='mortality_rate', y='country', palette='coolwarm')
plt.title('20 pays avec le plus grand taux de mortalité')
plt.xlabel('Taux de mortalité')
plt.ylabel('Pays')
plt.tight_layout()
plt.show()


# Pour comparer le nombre de cas et le nombre de morts dans les différents pays,
# nous pouvons utiliser un graphique à dispersion :

fig1 = px.scatter(data_frame=df, x='cases', y='deaths', hover_name='country', log_x=True, log_y=True,
                 color_discrete_sequence=['#e74c3c'], title='Comparaison entre nombre de cas et de morts')
fig1.show()

# Il en va de même pour comparer le nombre de cas et le nombre de guérisons dans les différents pays :

fig2 = px.scatter(data_frame=df, x='cases', y='recovered', hover_name='country', log_x=True, log_y=True,
                 color_discrete_sequence=['#2ecc71'], title='Comparaison entre nombre de cas et de guérisons')
fig2.show()

# Ainsi que pour comparer le nombre de morts et le nombre de guérisons dans les différents pays :

fig3 = px.scatter(data_frame=df, x='deaths', y='recovered', hover_name='country', log_x=True, log_y=True,
                 color_discrete_sequence=['#3498db'], title='Comparaison entre nombre de morts et de guérisons')
fig3.show()

# Affichage de la répartition du nombre de cas, de morts et de guérisons dans le monde
world_cases = df['cases'].sum()
world_deaths = df['deaths'].sum()
world_recovered = df['recovered'].sum()
world_stats = pd.DataFrame({
    'Cas': [world_cases],
    'Décès': [world_deaths],
    'Guérisons': [world_recovered]
})
world_stats.plot(kind='bar', figsize=(8, 6), color=['#ff7f0e', '#1f77b4', '#2ca02c'])
plt.title('Répartition du nombre de cas, de morts et de guérisons dans le monde')
plt.xticks(rotation=0)
plt.ylabel('Nombre de personnes')
plt.tight_layout()
plt.show()

# Affichage de la répartition du nombre de cas dans les différents pays
fig = px.choropleth(data_frame=df, locations='country', locationmode='country names', color='cases',
                    color_continuous_scale='Reds', title='Répartition du nombre de cas dans les différents pays')
fig.update_layout(geo=dict(showframe=False, showcoastlines=False))
fig.show()


# Exemple d'algorithme de Régression linéaire simple

# Sélection des features
X = df[['cases']]
y = df['deaths']

# Split des données en jeu d'entraînement et jeu de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entraînement du modèle
lr = LinearRegression()
lr.fit(X_train, y_train)

# Prédiction sur le jeu de test
y_pred = lr.predict(X_test)

# Evaluation du modèle
print('MSE: %.2f' % mean_squared_error(y_test, y_pred))
print('R2: %.2f' % r2_score(y_test, y_pred))

print('---------------------------------------------------------')

# Exemple d'algorithme de Regression linéaire multiple

# Sélection des features
X = df[['cases', 'recovered']]
y = df['deaths']

# Normalisation des données
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split des données en jeu d'entraînement et jeu de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entraînement du modèle
lr = LinearRegression()
lr.fit(X_train, y_train)

# Prédiction sur le jeu de test
y_pred = lr.predict(X_test)

# Evaluation du modèle
print('MSE: %.2f' % mean_squared_error(y_test, y_pred))
print('R2: %.2f' % r2_score(y_test, y_pred))

print('---------------------------------------------------------')

# Exemple d'algorithme Random Forest

# Sélection des features et de la target
X = df[['cases', 'recovered', 'active', 'population']]
y = df['deaths']

# Split des données en jeu d'entraînement et jeu de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Mise en place d'un pipeline pour la normalisation, la PCA et le modèle de Random Forest
pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('pca', PCA()),
    # ('discretize', KBinsDiscretizer()),
    ('rf', RandomForestRegressor(random_state=42))
])

# Paramètres pour la recherche par grille d'hyperparamètres
param_grid = {
    'pca__n_components': [2, 3, 4],
    # 'discretize__n_bins': [2, 3, 4],
    'rf__n_estimators': [100, 200, 300],
    'rf__max_depth': [5, 10, 20, None],
    'rf__max_features': ['sqrt', 'log2', None]
}

# Recherche par grille d'hyperparamètres
grid = GridSearchCV(pipe, param_grid=param_grid, cv=5, scoring='neg_mean_squared_error', n_jobs=-1)
grid.fit(X_train, y_train)

# Prédiction sur le jeu de test
y_pred = grid.predict(X_test)

# Evaluation du modèle
print('MSE: %.2f' % mean_squared_error(y_test, y_pred))
print('R2: %.2f' % r2_score(y_test, y_pred))

# Affichage des meilleurs paramètres
print("Meilleurs paramètres :")
print(grid.best_params_)

print('---------------------------------------------------------')

# Exemple d'algorithme de Réseau de neurones

# Sélection des features
X = df[['cases', 'recovered', 'active', 'population']]
y = df['deaths']

# Scale des features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split des données en jeu d'entraînement et jeu de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Définition des transformations à appliquer sur les features et la target
preprocessor = StandardScaler()
target_transformer = StandardScaler()

# Création du pipeline
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('target_transformer', target_transformer),
    ('nn', MLPRegressor(max_iter=10000, solver='adam'))
])

# Création de l'objet TransformedTargetRegressor
regressor = TransformedTargetRegressor(regressor=pipeline, transformer=target_transformer)

# Définition de la grille de paramètres à tester
param_grid = {
    'regressor__nn__hidden_layer_sizes': [(100,50), (200,100), (300,200)],
    'regressor__nn__activation': ['relu', 'logistic', 'tanh'],
    # 'regressor__nn__solver': ['adam', 'lbfgs', 'sgd'],
    'regressor__nn__alpha': [0.0001, 0.001, 0.01],
    'regressor__nn__max_iter': [500, 1000, 2000, 3000]
}

# Définition du GridSearch avec cross-validation
grid_search = GridSearchCV(
    estimator=regressor,
    param_grid=param_grid,
    scoring='neg_mean_squared_error',
    cv=5
)

# Entraînement du modèle
grid_search.fit(X_train, y_train)

# Prédiction sur le jeu de test
y_pred = grid_search.predict(X_test)

# Évaluation du modèle
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"MSE: {mse}")
print(f"R2: {r2}")

# Meilleurs paramètres
print("Meilleurs paramètres :")
print(grid_search.best_params_)
