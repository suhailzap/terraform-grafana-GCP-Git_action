# 🌐 Terraform Grafana Project on GCP

Welcome to the **Terraform Grafana Project on GCP** repository! This project uses Terraform to manage infrastructure on Google Cloud Platform (GCP) and GitHub Actions to automate deployment and destruction workflows.

---

## 📂 Repository Structure

- **`terraform-grafana/`**: Contains the Terraform configuration files.
- **`install_docker.py`**: Script to install Docker on the GCP instance.
- **`intro-to-mltp-main/`**: Contains Docker Compose files for deploying Grafana.

---

## 🚀 Workflows

### ⚙️ Terraform and Deploy

This workflow initializes and applies the Terraform configuration to set up the infrastructure and then deploys Grafana on a GCP instance.

#### 🔔 Trigger
- Manually via GitHub Actions.

#### 📝 Steps
1. **Checkout Terraform code**: Checks out the repository.
2. **Setup Terraform**: Sets up Terraform.
3. **Authenticate to Google Cloud**: Authenticates to GCP using a service account.
4. **Setup gcloud CLI**: Sets up the gcloud CLI.
5. **Terraform Init**: Initializes Terraform.
6. **Terraform Plan**: Creates an execution plan.
7. **Terraform Apply**: Applies the Terraform configuration.
8. **Checkout Compose file**: Checks out the repository again for Docker Compose files.
9. **Install Docker and Docker Compose on GCP Instance**: Installs Docker on the GCP instance.
10. **Deploy Grafana on GCP Instance**: Deploys Grafana using Docker Compose.
11. **Get GCP Instance Public IP Address**: Retrieves the public IP address of the GCP instance.

### 🛠️ Terraform Destroy on GCP

This workflow destroys the infrastructure created by the `Terraform and Deploy` workflow.

#### 🔔 Trigger
- Manually via GitHub Actions.

#### 📝 Steps
1. **Checkout Terraform code**: Checks out the repository.
2. **Setup Terraform**: Sets up Terraform.
3. **Authenticate to Google Cloud**: Authenticates to GCP using a service account.
4. **Setup gcloud CLI**: Sets up the gcloud CLI.
5. **Terraform Init**: Initializes Terraform.
6. **Terraform Plan (Destroy)**: Creates a plan to destroy the infrastructure.
7. **Terraform Destroy**: Destroys the infrastructure.

---

## 🏁 Getting Started

### 📋 Prerequisites

- GitHub account
- Google Cloud account
- Terraform installed locally (optional)

### ⚙️ Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/suhailzap/terraform-grafana.git
    cd terraform-grafana
    ```

2. **Configure GitHub Secrets**:
    - `GCP_SA_KEY`: JSON key of your Google Cloud service account.
    - Ensure your service account has the necessary permissions to manage the infrastructure.

### ▶️ Running Workflows

#### Deploying Infrastructure

1. Go to the **Actions** tab in your GitHub repository.
2. Select the `Terraform and Deploy` workflow.
3. Click on `Run workflow` to manually trigger the deployment.

#### Destroying Infrastructure

1. Go to the **Actions** tab in your GitHub repository.
2. Select the `Terraform Destroy on GCP` workflow.
3. Click on `Run workflow` to manually trigger the destruction.


---

## 📧 Contact

For any questions or issues, please contact **[suhailsap06@gmail.com](mailto:suhailsap06@gmail.com)**.

---

**Happy building!** ✨
