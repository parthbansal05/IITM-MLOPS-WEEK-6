mkdir wk2
cd wk2
git clone https://github.com/parthbansal05/IITM-MLOPS-TEST-REPO.git
ls -larth
git init
python3 -m venv .env
source .env/bin/activate
cd IITM-MLOPS-TEST-REPO/
pip install -r requirements.txt
cd ..
pip install dvc
pip install dvc-gs
dvc init
git status
git add .
git commit -m "Initialize DVC"


gcloud storage cp "gs://iitm-mlops-course-ultimate-walker-473518-e6/IRIS dataset/Iris1.csv" ./data.csv
dvc add data.csv
python IITM-MLOPS-TEST-REPO/train.py
dvc add svm_iris_model.joblib
git add .
git commit -m "V1: Initial data and processed output"
git tag V1


gcloud storage cp "gs://iitm-mlops-course-ultimate-walker-473518-e6/IRIS dataset/Iris2.csv" ./data.csv
dvc add data.csv
python IITM-MLOPS-TEST-REPO/cont_train.py
dvc add svm_iris_model.joblib
git add .
git commit -m "V2: Updated data and processed output"
git tag V2



git checkout V1
dvc checkout
echo -e "\n-- Reverted V1 content --"
python IITM-MLOPS-TEST-REPO/eval.py


git checkout V2
dvc checkout
echo -e "\n-- Reverted V2 content --"
python IITM-MLOPS-TEST-REPO/eval.py