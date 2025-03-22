import numpy as np
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import joblib

# Charger les données
data = np.load("preprocessed_data.npz")
X, y = data["X"], data["y"]

# PCA
pca = PCA(n_components=0.95)  # Garder 95% de variance
X_pca = pca.fit_transform(X)

# Séparation entraînement/test
X_train, X_test, y_train, y_test = train_test_split(X_pca, y, test_size=0.2)

# Entraînement SVM
model = SVC(kernel="linear", probability=True)
model.fit(X_train, y_train)

# Sauvegarder les modèles
joblib.dump(pca, "pca_model.pkl")
joblib.dump(model, "svm_model.pkl")
print(f"Accuracy: {model.score(X_test, y_test)*100:.2f}%")