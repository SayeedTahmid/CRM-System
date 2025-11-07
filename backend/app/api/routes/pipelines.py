from fastapi import APIRouter, Depends

from ...core.security import require_roles
from ...dependencies import get_crm_service
from ...models.schemas import Pipeline, PipelineCreate, PipelineStage, PipelineStageCreate, Role, UserContext
from ...services.crm_service import CRMService

router = APIRouter(prefix="/pipelines", tags=["pipelines"])


@router.get("", response_model=list[Pipeline])
async def list_pipelines(user: UserContext = Depends(require_roles(Role.admin, Role.manager, Role.sales)), crm: CRMService = Depends(get_crm_service)):
    return await crm.list_pipelines(user.company_id)


@router.post("", response_model=Pipeline)
async def create_pipeline(payload: PipelineCreate, user: UserContext = Depends(require_roles(Role.admin, Role.manager)), crm: CRMService = Depends(get_crm_service)):
    return await crm.create_pipeline(user.company_id, payload)


@router.put("/{pipeline_id}", response_model=Pipeline)
async def update_pipeline(pipeline_id: str, payload: PipelineCreate, user: UserContext = Depends(require_roles(Role.admin, Role.manager)), crm: CRMService = Depends(get_crm_service)):
    return await crm.update_pipeline(user.company_id, pipeline_id, payload)


@router.delete("/{pipeline_id}")
async def delete_pipeline(pipeline_id: str, user: UserContext = Depends(require_roles(Role.admin)), crm: CRMService = Depends(get_crm_service)):
    await crm.delete_pipeline(user.company_id, pipeline_id)
    return {"status": "deleted"}


@router.get("/{pipeline_id}/stages", response_model=list[PipelineStage])
async def list_pipeline_stages(pipeline_id: str, user: UserContext = Depends(require_roles(Role.admin, Role.manager, Role.sales)), crm: CRMService = Depends(get_crm_service)):
    return await crm.list_pipeline_stages(user.company_id, pipeline_id)


@router.post("/stages", response_model=PipelineStage)
async def create_stage(payload: PipelineStageCreate, user: UserContext = Depends(require_roles(Role.admin, Role.manager)), crm: CRMService = Depends(get_crm_service)):
    return await crm.create_pipeline_stage(user.company_id, payload)


@router.put("/stages/{stage_id}", response_model=PipelineStage)
async def update_stage(stage_id: str, payload: PipelineStageCreate, user: UserContext = Depends(require_roles(Role.admin, Role.manager)), crm: CRMService = Depends(get_crm_service)):
    return await crm.update_pipeline_stage(user.company_id, stage_id, payload)


@router.delete("/stages/{stage_id}")
async def delete_stage(stage_id: str, user: UserContext = Depends(require_roles(Role.admin, Role.manager)), crm: CRMService = Depends(get_crm_service)):
    await crm.delete_pipeline_stage(user.company_id, stage_id)
    return {"status": "deleted"}
