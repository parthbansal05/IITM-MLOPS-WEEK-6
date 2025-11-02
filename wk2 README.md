# Assignment: Incorporating DVC in IRIS Pipeline

**Name:** Parth Bansal  
**Student ID:** 21f3000805

---

## Objective

The objective of this assignment is to integrate **Data Version Control (DVC)** into the IRIS Machine Learning pipeline to manage data and model versions effectively. The task involves setting up DVC with Google Cloud Storage as remote storage, augmenting the dataset, and demonstrating version control operations using DVC commands.

---

## Files Included

| File Name               | Description                                                         |
| ----------------------- | ------------------------------------------------------------------- |
| **main.sh**             | Shell script to automate setup and execution on GCP Cloud Shell.    |
| **train.py**            | Trains a new SVC model on the provided dataset.                     |
| **cont_train.py**       | Continues training of a pre-existing SVC model using updated data.  |
| **eval.py**             | Evaluates the trained SVC model’s performance.                      |
| **iris.csv**            | Original IRIS dataset used for training.                            |
| **shuffler.py**         | Script to shuffle rows of the dataset for data augmentation.        |
| **shuffled_output.csv** | Shuffled version of the IRIS dataset generated using `shuffler.py`. |
| **iris1.csv**           | First 50% split of the original dataset.                            |
| **iris2.csv**           | Second 50% split of the original dataset.                           |
| **requirements.txt**    | Lists all Python dependencies required to run the scripts.          |

---

## Execution Steps

1. Run `main.sh` in GCP Cloud Shell to set up the environment and execute all tasks.
2. The script performs the following:

   * Initializes a Git and DVC repository.
   * Configures Google Cloud Storage as remote storage.
   * Loads and augments the IRIS dataset.
   * Trains, continues training, and evaluates the model.
   * Tracks data and model versions using DVC commands.

---

## Notes

* Ensure Google Cloud SDK and DVC are pre-installed.
* Use `dvc checkout` to traverse between different data or model versions.
* All operations are demonstrated in the accompanying screencast.
