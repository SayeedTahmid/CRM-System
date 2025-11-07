from fastapi import APIRouter, Depends

from ...core.security import require_roles
from ...dependencies import get_crm_service
from ...models.schemas import DashboardSummary, Role, UserContext
from ...services.crm_service import CRMService

router = APIRouter(prefix="/dashboard", tags=["dashboard"])


@router.get("/summary", response_model=DashboardSummary)
async def get_dashboard_summary(user: UserContext = Depends(require_roles(Role.admin, Role.manager, Role.sales)), crm: CRMService = Depends(get_crm_service)):
    return await crm.dashboard_summary(user.company_id)
