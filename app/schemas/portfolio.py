from datetime import datetime
from pydantic import BaseModel, HttpUrl, Field


class SystemHealth(BaseModel):
    """Schema for the Live Infrastructure Widget."""

    status: str = Field(..., description="Current operational status")
    environment: str = Field(
        ..., description="Running environment (e.g., development, production)"
    )
    timestamp: datetime = Field(..., description="Server time of the health check")
    hosted_on: str = Field(..., description="Infrastructure provider")
    message: str = Field(..., description="System health message")


class Project(BaseModel):
    """Schema for Portfolio Projects showcasing your T-shaped skills."""

    id: int
    title: str = Field(..., min_length=3, max_length=100)
    category: str = Field(
        ...,
        description="Must be one of: 'Backend & Core', 'Native Mobile', 'DevOps & Infra', 'AI Integrations'",
    )
    description: str = Field(..., max_length=500)
    tech_stack: list[str] = Field(
        ..., min_length=1, description="List of technologies used"
    )
    github_url: HttpUrl = Field(..., description="Link to the source code repository")
    demo_url: HttpUrl | None = Field(
        default=None, description="Optional link to a live demo"
    )
    featured: bool = Field(
        default=False, description="Flag to highlight on the main hero section"
    )
