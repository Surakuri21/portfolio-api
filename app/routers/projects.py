from fastapi import APIRouter
from app.schemas.portfolio import Project

router = APIRouter(prefix="/projects", tags=["Projects"])

# In-memory database representing my T-shaped portfolio
PORTFOLIO_PROJECTS = [
    Project(
        id=1,
        title="Automated Multi-Cloud CI/CD Pipeline",
        category="DevOps & Infra",
        description="Containerized microservice architecture running on Cloud Run with GitHub Actions automated testing.",
        tech_stack=[
            "Docker",
            "FastAPI",
            "GitHub Actions",
            "Cloud Run",
            "Git Bash",
            "Vim",
        ],
        github_url="https://github.com/Surakuri21/portfolio-api",
        featured=True,
    ),
    Project(
        id=2,
        title="Hardware E-Commerce Platform",
        category="Full-Stack Web Development",
        description="A complete e-commerce solution for hardware components, driven by a robust, highly-concurrent Java backend.",
        tech_stack=[
            "Java",
            "Spring Boot",
            "Hibernate / JPA",
            "Postman",
            "Maven",
            "REST API",
            "SQL",
            "Authentication",
        ],
        github_url="https://github.com/Surakuri21/ai-reviewer",
        featured=True,
    ),
    Project(
        id=3,
        title="Edge AI Engineering Co-Pilot",
        category="Native Mobile & Edge AI",
        description="An offline-first Android utility utilizing a Hybrid Isolation Architecture to safely execute natural language engineering calculations.",
        tech_stack=[
            "Kotlin",
            "Jetpack Compose",
            "LiteRT-LM",
            "exp4j",
            "Android Studio",
        ],
        github_url="https://github.com/Surakuri21/engiCal",
        featured=False,
    ),
]


@router.get("/", response_model=list[Project])
async def list_projects(category: str | None = None) -> list[Project]:
    """Retrieve all portfolio projects with optional category filtering."""
    if category:
        return [p for p in PORTFOLIO_PROJECTS if p.category.lower() == category.lower()]
    return PORTFOLIO_PROJECTS
