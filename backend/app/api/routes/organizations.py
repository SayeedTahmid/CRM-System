from fastapi import APIRouter, Depends

from ...core.security import require_roles
from ...dependencies import get_crm_service
from ...models.schemas import Organization, OrganizationCreate, Role, UserContext
from ...services.crm_service import CRMService

router = APIRouter(prefix="/organizations", tags=["organizations"])


@router.get("", response_model=list[Organization])
async def list_organizations(user: UserContext = Depends(require_roles(Role.admin, Role.manager, Role.sales)), crm: CRMService = Depends(get_crm_service)):
    return await crm.list_organizations(user.company_id)


@router.post("", response_model=Organization)
async def create_organization(payload: OrganizationCreate, user: UserContext = Depends(require_roles(Role.admin, Role.manager)), crm: CRMService = Depends(get_crm_service)):
    return await crm.create_organization(user.company_id, payload)


@router.put("/{organization_id}", response_model=Organization)
async def update_organization(organization_id: str, payload: OrganizationCreate, user: UserContext = Depends(require_roles(Role.admin, Role.manager)), crm: CRMService = Depends(get_crm_service)):
    return await crm.update_organization(user.company_id, organization_id, payload)


@router.delete("/{organization_id}")
async def delete_organization(organization_id: str, user: UserContext = Depends(require_roles(Role.admin)), crm: CRMService = Depends(get_crm_service)):
    await crm.delete_organization(user.company_id, organization_id)
    return {"status": "deleted"}
