from datetime import datetime

from fastapi import APIRouter
from fastapi import Depends

from ...core.security import require_roles
from ...dependencies import get_crm_service
from ...models.schemas import Activity, ActivityCreate, ActivityType, Role, UserContext
from ...services.crm_service import CRMService

router = APIRouter(prefix="/tasks", tags=["tasks"])
__all__ = ["router"]


@router.get("", response_model=list[Activity])
async def list_tasks(user: UserContext = Depends(require_roles(Role.admin, Role.manager, Role.sales)), crm: CRMService = Depends(get_crm_service)):
    tasks = await crm.list_activities(user.company_id)
    filtered = [task for task in tasks if task.type == ActivityType.task]
    filtered.sort(key=lambda task: task.due_date or datetime.utcnow())
    return filtered


@router.post("", response_model=Activity)
async def create_task(payload: ActivityCreate, user: UserContext = Depends(require_roles(Role.admin, Role.manager, Role.sales)), crm: CRMService = Depends(get_crm_service)):
    if payload.type != ActivityType.task:
        payload = ActivityCreate(**{**payload.model_dump(), "type": ActivityType.task})
    return await crm.create_activity(user.company_id, payload)
