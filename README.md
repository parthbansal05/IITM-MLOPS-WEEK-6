# **Continuous Deployment of IRIS API using GitHub Actions & GCP**

**Author:** Parth Bansal
**Enrollment Number:** 21F3000805

---

## **Project Overview**

This project extends the **Continuous Integration (CI)** workflow developed in the previous week by adding **Continuous Deployment (CD)**.
The IRIS classification model is packaged as a **FastAPI-based microservice**, containerized using **Docker**, and deployed to **Google Kubernetes Engine (GKE)** using **GitHub Actions**.
The workflow ensures that every code change automatically trains, evaluates, builds, pushes, and deploys the updated API.

---

## **Assignment Objective**

* Integrate **Continuous Deployment (CD)** using **GitHub Actions**.
* Build and push the **Docker image** of the IRIS API to **Google Artifact Registry (GAR)**.
* Configure and authenticate **GCP Service Account** within GitHub Actions.
* Deploy the image on **GKE** through Kubernetes manifests (`deployment.yaml`, `service.yaml`).
* Demonstrate the difference between **Docker containers** and **Kubernetes Pods**.

---

## **Key Concepts**

### **1. GitHub Actions**

Automates the CI/CD pipeline through workflow YAML files:

* **CI Stage:** Runs training (`train.py`) and evaluation (`eval.py`) on pull requests using **CML** (Continuous Machine Learning).
* **CD Stage:** Builds the Docker image, pushes it to **GAR**, and deploys it to **GKE** on merge to `main`.

### **2. Docker**

* Packages the FastAPI application (`app.py`) and model artifacts into a container.
* The **Dockerfile** defines the environment, dependencies, and startup command (`uvicorn app:app`).
* The container image ensures consistent execution across environments.

### **3. Google Artifact Registry (GAR)**

* Acts as a **secure image repository** in GCP.
* GitHub Actions authenticates using a **GCP Service Account** and pushes the built image to GAR.

### **4. Google Kubernetes Engine (GKE)**

* Hosts and manages the containerized application using **Kubernetes**.
* The deployment and service YAML files define:

  * **Deployment:** Pod replicas, container image, and exposed ports.
  * **Service:** LoadBalancer to make the API publicly accessible.

### **5. Kubernetes vs Docker**

* **Docker Container:** A single isolated environment for running one application instance.
* **Kubernetes Pod:** The smallest deployable unit in Kubernetes that can contain one or more Docker containers sharing resources and networking.

---

## **Project Structure**

| **Path**                                | **Description**                                                                    |
| --------------------------------------- | ---------------------------------------------------------------------------------- |
| `.github/workflows/cml_pr_workflow.yml` | CI/CD workflow automating model training, evaluation, image build, and deployment. |
| `application/app.py`                    | FastAPI-based IRIS classification API.                                             |
| `application/Dockerfile`                | Docker image configuration for the API.                                            |
| `application/artifacts/`                | Stores the trained model and evaluation artifacts.                                 |
| `data/data.csv`                         | Dataset used for training and testing the model.                                   |
| `train.py`                              | Trains the SVM model and saves it as a `.joblib` file.                             |
| `eval.py`                               | Evaluates the model, generates metrics and confusion matrix.                       |
| `k8s/deployment.yaml`                   | Defines Kubernetes deployment configuration for GKE.                               |
| `k8s/service.yaml`                      | Exposes the deployed service using a LoadBalancer.                                 |
| `requirements.txt`                      | Python dependencies for training and API runtime.                                  |
| `gcp commands.txt`                      | Contains GCP CLI commands used for setup and debugging.                            |

---

## **Technologies Used**

* **GitHub Actions (CI/CD)**
* **FastAPI (Model Serving)**
* **Docker (Containerization)**
* **Google Artifact Registry (Image Hosting)**
* **Google Kubernetes Engine (Deployment)**
* **Python, Scikit-learn, Joblib, Pandas**

---

## **Redeployment Instructions**

To **re-deploy** the IRIS API:

1. **Recreate the GKE Autopilot Cluster:**

   * Open the **Google Cloud Console** → **Kubernetes Engine** → **Clusters**.
   * Click **Create Cluster** → Select **Autopilot Mode**.
   * Name your cluster (e.g., `iris-autopilot-cluster`) and choose a **zone** (default: `us-central1`).
   * Click **Create** and wait for provisioning.

2. **Update GitHub Secrets:**

   * Go to your **GitHub repository** → **Settings** → **Secrets and variables** → **Actions**.
   * Edit the secrets related to GKE:

     * `GKE_CLUSTER_NAME` → update with the new cluster name.
     * `GKE_ZONE` → update with the new zone.
   * Ensure your **GCP service account key** (`GCP_SA_KEY`) remains valid.

3. **Trigger Redeployment:**

   * Commit and push any change (e.g., update a README file).
   * GitHub Actions will automatically rebuild the Docker image, push it to **Artifact Registry**, and deploy it to your **new cluster**.

---

## **Acknowledgment**

This project is developed as part of the **IIT Madras MLOps Week 4** assignment —
*"Continuous Deployment of IRIS API using GitHub Actions and Google Cloud Platform (GCP)."*
