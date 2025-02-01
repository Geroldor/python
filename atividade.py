# Importar bibliotecas necessárias
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Carregar o dataset Iris
iris = load_iris()

# Dividir o dataset em características (X) e rótulos (y)
X = iris.data
y = iris.target

# Dividir o dataset em conjuntos de treinamento e teste
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.2, random_state=42)

# Criar uma rede neural com 2 camadas ocultas, cada uma com 10 neurônios
mlp = MLPClassifier(hidden_layer_sizes=(10, 10), max_iter=1000)

# Treinar a rede neural com o conjunto de treinamento
mlp.fit(X_treino, y_treino)

# Realizar previsões com o conjunto de teste
previsoes = mlp.predict(X_teste)

# Avaliar o desempenho da rede neural
accuracy = accuracy_score(y_teste, previsoes)
print("Acurácia:", accuracy)
print("Relatório de classificação:\n", classification_report(y_teste, previsoes))
print("Matriz de confusão:\n", confusion_matrix(y_teste, previsoes))