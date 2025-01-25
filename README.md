# AI Vision Backend

Multimodal AI Assistant with RAG capabilities

## Features

-   Multimodal input (text + images)
-   User-specific conversation history
-   Common knowledge base
-   Web search integration
-   PostgreSQL backend

## Local Setup (Miniconda)

1. Create environment:

```bash
conda create -n VisionRAG python=3.10
conda activate VisionRAG
```

2. Install dependencies:

```bash
conda install pytorch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1 pytorch-cuda=12.4 -c pytorch -c nvidia
pip install -r requirements.txt
```

3. Start PostgreSQL

```bash
# Start PostgreSQL in detached mode
docker-compose -f docker-compose.db.yml up -d

# Verify container is running
docker ps

# Check logs if needed
docker-compose -f docker-compose.db.yml logs -f db
```

```bash
# Build the application
docker-compose -f docker-compose.full.yml build

# Start all services
docker-compose -f docker-compose.full.yml up -d

# Verify running containers
docker ps

# Check application logs
docker-compose -f docker-compose.full.yml logs -f app
```

3. Start PostgreSQL:

```bash
# Production
docker-compose -f docker-compose.yml up --build

# Development
docker-compose -f docker-compose.yml -f docker-compose.override.yml up --build
```

4. Run API:

```bash
uvicorn api.main:app --reload
```

5. Docker Setup

```bash
docker-compose up --build
```

6. API Documentation
   API Docs: http://localhost:8000/docs
   PostgreSQL: localhost:5432
   pgAdmin: http://localhost:5050 (user: admin@aivision.com, password: admin123)

7. Management Commands:

```bash
# View logs
docker-compose logs -f app

# Run migrations
docker-compose exec app python -m api.src.core.database

# Enter container shell
docker-compose exec app sh

# Tear down
docker-compose down -v
```
