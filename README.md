# FastAPI Project

This project is built using FastAPI and provides endpoints as specified in the project documentation.

## Set up Database

### Create Database
1. Create the database:
    ```sql
    CREATE DATABASE assignment;
    ```

2. Import tables and data from the file:
    ```sh
    psql -U <your-username> -d assignment -f data/assignment.sql
    ```

## Steps to Run the Project

1. **Create a virtual environment**:
    ```sh
    python3 -m venv fastapi
    ```

2. **Activate the environment**:
    - On macOS/Linux:
        ```sh
        source fastapi/bin/activate
        ```
    - On Windows:
        ```sh
        fastapi\Scripts\activate
        ```

3. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Run the project**:
    ```sh
    uvicorn main:app --reload
    ```
5. **Sample User
    username: debasmita
    password: abcd1234

6. **Run test cases**:
    ```sh
    pytest
    ```

7. **Swagger UI** is available at:
    ```
    http://localhost:8000/docs
    ```

8. **Redoc** is available at:
    ```
    http://localhost:8000/redoc
    ```

## Deploy the Application

Considering there is a running Kubernetes setup, a `bitbucket-pipeline.yml` is included in the repository. The `deployment.yaml` and `service.yaml` files are included in the `k8s` folder. 

> Note: This project is currently configured to use Bitbucket as the Git repository and thus includes `bitbucket-pipeline.yml` for deployment.

### Kubernetes Deployment

1. Ensure your Kubernetes cluster is running and configured.
2. Deploy the application using the provided Kubernetes configuration files in the `k8s` folder:
    ```sh
    kubectl apply -f k8s/deployment.yaml
    kubectl apply -f k8s/service.yaml
    ```

For further details on the deployment process, refer to the `bitbucket-pipeline.yml` and the `k8s` folder within the repository.
