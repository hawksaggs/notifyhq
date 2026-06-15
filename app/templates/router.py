import uuid
from datetime import UTC, datetime

from fastapi import APIRouter, Query

from app.templates.schemas import (
    Channel,
    CreateTemplateRequest,
    PaginatedTemplatesResponse,
    TemplateResponse,
)

router = APIRouter(prefix="/templates", tags=["Templates"])

templates: list[TemplateResponse] = []


@router.get("")
async def get_templates(
    page: int = Query(default=1, ge=1),
    page_size: int = Query(default=20, ge=1, le=100, description="Results per page"),
    channel: Channel | None = None,
) -> PaginatedTemplatesResponse:
    # Filter by channel if provided
    data = [x for x in templates if x.channel == channel] if channel else templates

    # Calculate skip and limit
    skip = (page - 1) * page_size
    limit = skip + page_size

    return PaginatedTemplatesResponse(
        page=page, page_size=page_size, data=data[skip:limit]
    )


@router.post("")
async def create_template(payload: CreateTemplateRequest) -> TemplateResponse:
    template = TemplateResponse(
        id=str(uuid.uuid4()),
        created_at=datetime.now(UTC).isoformat(),
        name=payload.name,
        channel=payload.channel,
        subject=payload.subject,
        body=payload.body,
    )
    templates.append(template)
    return template
