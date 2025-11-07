from fastapi import APIRouter
from fastapi import Depends

from ...core.security import require_roles
from ...dependencies import get_crm_service
from ...models.schemas import Person, PersonCreate, Role, UserContext
from ...services.crm_service import CRMService

router = APIRouter(prefix="/persons", tags=["persons"])
__all__ = ["router"]


@router.get("", response_model=list[Person])
async def list_persons(user: UserContext = Depends(require_roles(Role.admin, Role.manager, Role.sales)), crm: CRMService = Depends(get_crm_service)):
    return await crm.list_persons(user.company_id)


@router.post("", response_model=Person)
async def create_person(payload: PersonCreate, user: UserContext = Depends(require_roles(Role.admin, Role.manager, Role.sales)), crm: CRMService = Depends(get_crm_service)):
    return await crm.create_person(user.company_id, payload)


@router.put("/{person_id}", response_model=Person)
async def update_person(person_id: str, payload: PersonCreate, user: UserContext = Depends(require_roles(Role.admin, Role.manager, Role.sales)), crm: CRMService = Depends(get_crm_service)):
    return await crm.update_person(user.company_id, person_id, payload)


@router.delete("/{person_id}")
async def delete_person(person_id: str, user: UserContext = Depends(require_roles(Role.admin, Role.manager)), crm: CRMService = Depends(get_crm_service)):
    await crm.delete_person(user.company_id, person_id)
    return {"status": "deleted"}
