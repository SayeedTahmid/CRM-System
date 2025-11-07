from fastapi import APIRouter, Depends

from ...core.security import require_roles
from ...dependencies import get_crm_service
from ...models.schemas import Deal, DealCreate, Role, UserContext
from ...services.crm_service import CRMService

router = APIRouter(prefix="/deals", tags=["deals"])


@router.get("", response_model=list[Deal])
async def list_deals(user: UserContext = Depends(require_roles(Role.admin, Role.manager, Role.sales)), crm: CRMService = Depends(get_crm_service)):
    return await crm.list_deals(user.company_id)


@router.post("", response_model=Deal)
async def create_deal(payload: DealCreate, user: UserContext = Depends(require_roles(Role.admin, Role.manager, Role.sales)), crm: CRMService = Depends(get_crm_service)):
    return await crm.create_deal(user.company_id, payload)


@router.put("/{deal_id}", response_model=Deal)
async def update_deal(deal_id: str, payload: DealCreate, user: UserContext = Depends(require_roles(Role.admin, Role.manager, Role.sales)), crm: CRMService = Depends(get_crm_service)):
    return await crm.update_deal(user.company_id, deal_id, payload)


@router.delete("/{deal_id}")
async def delete_deal(deal_id: str, user: UserContext = Depends(require_roles(Role.admin, Role.manager)), crm: CRMService = Depends(get_crm_service)):
    await crm.delete_deal(user.company_id, deal_id)
    return {"status": "deleted"}
