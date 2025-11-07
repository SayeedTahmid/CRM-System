from typing import List

from fastapi import APIRouter, Depends, Query

from ...core.security import require_roles
from ...dependencies import get_crm_service
from ...models.schemas import Activity, ActivityCreate, Role, UserContext
from ...services.crm_service import CRMService

router = APIRouter(prefix="/activities", tags=["activities"])


@router.get("", response_model=list[Activity])
async def list_activities(user: UserContext = Depends(require_roles(Role.admin, Role.manager, Role.sales)), crm: CRMService = Depends(get_crm_service)):
    return await crm.list_activities(user.company_id)


@router.get("/entity/{entity}/{entity_id}", response_model=list[Activity])
async def list_entity_activities(entity: str, entity_id: str, user: UserContext = Depends(require_roles(Role.admin, Role.manager, Role.sales)), crm: CRMService = Depends(get_crm_service)):
    return await crm.activities_by_entity(user.company_id, entity, entity_id)


@router.post("", response_model=Activity)
async def create_activity(
    payload: ActivityCreate,
    recipients: List[str] = Query(default_factory=list, alias="recipients"),
    user: UserContext = Depends(require_roles(Role.admin, Role.manager, Role.sales)),
    crm: CRMService = Depends(get_crm_service),
):
    return await crm.create_activity(user.company_id, payload, recipients)


@router.put("/{activity_id}", response_model=Activity)
async def update_activity(activity_id: str, payload: ActivityCreate, user: UserContext = Depends(require_roles(Role.admin, Role.manager, Role.sales)), crm: CRMService = Depends(get_crm_service)):
    return await crm.update_activity(user.company_id, activity_id, payload)


@router.delete("/{activity_id}")
async def delete_activity(activity_id: str, user: UserContext = Depends(require_roles(Role.admin, Role.manager)), crm: CRMService = Depends(get_crm_service)):
    await crm.delete_activity(user.company_id, activity_id)
    return {"status": "deleted"}
