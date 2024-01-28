# VideoLibManager

An interactive video library built with Flask and Docker, featuring a RESTful API for JSON data management. Streamlined deployment facilitated by a virtual machine (VM).

---

## Installation Guide

### Setting Up the Environment

1. **Install Docker**: Ensure Docker is installed on your system. If not, follow the official [Docker installation guide](https://docs.docker.com/get-docker/).

2. **Clone the Repository**: Clone the VideoLibManager repository to your local machine:
    ```bash
    git clone https://github.com/Rahim21/VideoLibManager.git
    ```

3. **Navigate to Project Directory**: Move into the project directory:
    ```bash
    cd VideoLibManager
    ```

4. **Configure Non-Local Addresses** (if necessary): If your application will be accessed from a non-local environment, modify the API URL in the following files to match your server's address:
    - `VideoLibManager/DigitalMovies/controllers/movie_controller.py`
    - `VideoLibManager/DigitalMovies/controllers/user_controller.py`

## Docker Usage

1. **Build Docker Containers**: To build the Docker containers, execute:
    ```bash
    sudo docker-compose up --build -d
    ```

2. **Start Containers**: Start the containers with:
    ```bash
    sudo docker-compose up -d
    ```

3. **Stop Containers**: To stop the running containers, use:
    ```bash
    sudo docker-compose down
    ```

## Additional Docker Commands

- **View Container Logs**: Check the logs of running containers:
    ```bash
    sudo docker-compose logs
    ```

- **Check Docker Service Status**: Verify the status of Docker service:
    ```bash
    sudo docker-compose status
    ```

- **List Running Containers**: See the list of currently running containers:
    ```bash
    sudo docker-compose ps
    ```
