from fastapi import APIRouter
from fastapi import Depends

from ...core.security import require_roles
from ...dependencies import get_crm_service
from ...models.schemas import CRMFile, CRMFileCreate, Role, UserContext
from ...services.crm_service import CRMService

router = APIRouter(prefix="/files", tags=["files"])
__all__ = ["router"]


@router.get("", response_model=list[CRMFile])
async def list_files(user: UserContext = Depends(require_roles(Role.admin, Role.manager, Role.sales)), crm: CRMService = Depends(get_crm_service)):
    return await crm.list_files(user.company_id)


@router.post("", response_model=CRMFile)
async def create_file(payload: CRMFileCreate, user: UserContext = Depends(require_roles(Role.admin, Role.manager, Role.sales)), crm: CRMService = Depends(get_crm_service)):
    return await crm.create_file(user.company_id, payload)


@router.delete("/{file_id}")
async def delete_file(file_id: str, user: UserContext = Depends(require_roles(Role.admin, Role.manager)), crm: CRMService = Depends(get_crm_service)):
    await crm.delete_file(user.company_id, file_id)
    return {"status": "deleted"}
