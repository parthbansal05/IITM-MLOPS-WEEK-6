# eval.py
import json
from matplotlib import pyplot as plt
import pandas as pd
import joblib 
from sklearn.model_selection import train_test_split 
from sklearn.metrics import accuracy_score, confusion_matrix
import sys
import numpy as np


# Define file paths
model_path = 'application/artifacts/svm_iris_model.joblib'
data_path = 'data/data.csv'
METRICS_FILEPATH = 'application/artifacts/metrics.json'
CM_PLOT_PATH = 'application/artifacts/confusion_matrix.png'

try:
    model = joblib.load(model_path)
    iris = pd.read_csv(data_path)
    iris = iris.sample(frac=1, random_state=None).reset_index(drop=True)

    train, test = train_test_split(iris, test_size=0.3, random_state=42) 
    X_test = test[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']] 
    y_test = test.Species 
except FileNotFoundError as e:
    print(f"Error: Missing file - {e}. Make sure DVC has pulled the data and model.")
    sys.exit(1)


y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

metrics = {
    'accuracy': round(accuracy, 4),
    'cm': cm.tolist() # Convert numpy array to list for JSON serialization
}


with open(METRICS_FILEPATH, 'w') as f:
    json.dump(metrics, f, indent=4)
print(f"Metrics saved to {METRICS_FILEPATH}")


# --- 5. Generate CML Plot (Confusion Matrix) ---
fig, ax = plt.subplots(figsize=(6, 6))
cax = ax.matshow(cm, cmap=plt.cm.Blues)
plt.title('Confusion Matrix')
fig.colorbar(cax)
ax.set_xlabel('Predicted')
ax.set_ylabel('True')
ax.set_xticklabels([''] + [0, 1])
ax.set_yticklabels([''] + [0, 1])

# Annotate the matrix
for (i, j), val in np.ndenumerate(cm):
    ax.text(j, i, f'{val}', ha='center', va='center', color='white' if val > cm.max() / 2 else 'black')

plt.savefig(CM_PLOT_PATH)
print(f"Confusion Matrix plot saved to {CM_PLOT_PATH}")

markdown_content = f"""
## Model Evaluation Report (Dev Branch)

| Metric | Value |
| :--- | :--- |
| Accuracy | {metrics['accuracy']} |

### Confusion Matrix
![]({CM_PLOT_PATH})

"""
# Write the markdown to a file for the CML workflow to use
with open('cml_report.md', 'w') as f:
    f.write(markdown_content)
    
print("Evaluation complete. Report generated.")
