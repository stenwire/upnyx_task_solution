# upnyx_task_solution

---

## How to Use

### Requirements:
- **Make**
- **Docker**
- **Docker Compose**

---

### Running the Application with Docker (Recommended)

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   ```

2. **Navigate to the project directory:**
   ```bash
   cd <repo-directory>
   ```

3. **Set up the environment:**
   - Duplicate the `.env.example` file:
     ```bash
     cp .env.example .env
     ```
   - Edit the `.env` file to suit your configuration.
   - Modify the `postgres` service in `docker-compose.yml` to reflect your choice of database, and ensure this matches the `.env` file.

4. **Build the docker image:**
   ```bash
   make build
   ```

5. **Run migrations:**
   ```bash
   make migrate
   ```

6. **Create a superuser:**
   ```bash
   make createsuperuser
   ```
   - Fill in the required details (your password won't be visible).

7. **Start the server:**
   ```bash
   make up
   ```

8. **Access the application:**
   - Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser to start using the application.

8. **Edit templates and customize as needed.**

---

### Running the Application Outside of Docker (Not Recommended)

1. **Create a Postgres database:**
   - You can do this manually through `psql` commands (not recommended).

2. **Set up the environment:**
   - Duplicate the `.env.example` file and rename it to `.env`.
   - Edit the `.env` file, especially the database settings
3. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

4. **Start the server:**
   ```bash
   gunicorn --bind 0.0.0.0:8000 config.wsgi:application
   ```

5. **Access the application:**
   - Visit [http://127.0.0.1:8000](http://127.0.0.1:8000).

6. **Switch to Docker for a smoother experience!**

---

### Common Commands (Makefile)

Most of the commands you'll need are defined in the `Makefile`. Use them as:

```bash
make <command>
```

**Available Commands:**
- `up`: Start up the containers
- `bash`: Start a bash shell for the application
- `build`: Build the containers only
- `build-up`: Build and start the containers
- `createsuperuser`: Create a superuser for the Django app
- `down`: Stop the containers
- `format`: Run `isort` and `black` to format the codebase
- `flush-db`: Empty the database and reset it from scratch
- `install`: Install all dependencies in a local virtual environment
- `lint`: Run `ruff` to lint and format the code
- `migrations`: Create migrations based on DB schema changes
- `migrate`: Run migrations
- `resetdb`: Reset the database and delete everything, including the database itself
- `run-command`: Run any custom command in the Django app context (e.g., `make run-command command="python manage.py test"`)
- `shell`: Start a Django shell session
- `test`: Run the test suite using `pytest`
- `testcase`: Run a single test case (e.g., `make testcase testcase="tests/test_models.py::TestUserModel::test_user_can_be_created"`)
- `up-d`: Start the container in detached mode (without logs)

---

### Running Commands in Docker

First, check if the command you need is in the list above. If it is, use:

```bash
make <command>
```

For example, to run tests:
```bash
make test
```

If the command isn't there, use:
```bash
make run-command command="<command>"
```

For example, to run tests:
```bash
make run-command command="python manage.py test"
```

Alternatively, without `make`:
```bash
docker compose run <container-name> <command>
```

For example, to run tests:
```bash
docker compose run web python manage.py test
```

---

### VSCode Setup for Auto-Imports

1. **Install dependencies outside of Docker:**
   ```bash
   make install
   ```

2. **Activate the virtual environment:**
   ```bash
   pipenv shell
   ```

3. **Configure VSCode:**
   - In the bottom-right corner, click the Python version.
   - Select the Python interpreter created from your virtual environment.

Now you can continue working inside Docker with the benefits of local environment features.

---

### Project Tree

```
upnyx_task_solution
├─ .dockerignore
├─ .git
├─ .gitignore
├─ authentication
│  ├─ admin.py
│  ├─ apps.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ serializers.py
│  ├─ tests.py
│  ├─ urls.py
│  ├─ views.py
│  └─ __init__.py
├─ chat
│  ├─ admin.py
│  ├─ apps.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ serializers.py
│  ├─ tests.py
│  ├─ urls.py
│  ├─ views.py
│  └─ __init__.py
├─ config
│  ├─ admin.py
│  ├─ asgi.py
│  ├─ settings.py
│  ├─ urls.py
│  ├─ wsgi.py
│  └─ __init__.py
├─ docker-compose.yml
├─ Dockerfile
├─ Makefile
├─ manage.py
├─ Pipfile
├─ Pipfile.lock
└─ README.md

```