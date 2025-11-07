from __future__ import annotations

from collections import Counter
from datetime import datetime
from typing import Dict, Iterable, List

from loguru import logger

from ..models.schemas import (
    Activity,
    ActivityCreate,
    ActivityNotification,
    ActivityType,
    Company,
    CompanyCreate,
    CRMFile,
    CRMFileCreate,
    CustomField,
    CustomFieldCreate,
    CustomFieldValue,
    CustomFieldValueCreate,
    DashboardSummary,
    Deal,
    DealCreate,
    Organization,
    OrganizationCreate,
    Person,
    PersonCreate,
    Pipeline,
    PipelineCreate,
    PipelineStage,
    PipelineStageCreate,
)
from .email import EmailService
from .integrations import CalendarIntegration, build_calendar_payload
from .repository import BaseRepository


class CRMService:
    """Business logic for CRM operations."""

    def __init__(self, repository: BaseRepository, email_service: EmailService, calendar_integration: CalendarIntegration | None = None) -> None:
        self.repository = repository
        self.email_service = email_service
        self.calendar_integration = calendar_integration or CalendarIntegration()

    async def _create_entity(self, table: str, company_id: str, payload: dict) -> dict:
        payload.update({"company_id": company_id})
        return await self.repository.create(table, payload)

    async def _update_entity(self, table: str, company_id: str, entity_id: str, payload: dict) -> dict:
        entity = await self.repository.get(table, entity_id)
        if not entity or entity.get("company_id") != company_id:
            raise ValueError("Entity not found")
        return await self.repository.update(table, entity_id, payload)

    async def _delete_entity(self, table: str, company_id: str, entity_id: str) -> None:
        entity = await self.repository.get(table, entity_id)
        if not entity or entity.get("company_id") != company_id:
            raise ValueError("Entity not found")
        await self.repository.delete(table, entity_id)

    # Companies & Users -------------------------------------------------
    async def create_company(self, payload: CompanyCreate) -> Company:
        record = await self.repository.create("companies", payload.model_dump())
        return Company.model_validate(record)

    async def list_company_users(self, company_id: str) -> List[dict]:
        return await self.repository.list("users", {"company_id": company_id})

    # Organizations ------------------------------------------------------
    async def list_organizations(self, company_id: str) -> List[Organization]:
        records = await self.repository.list("crm_organizations", {"company_id": company_id})
        return [Organization.model_validate(rec) for rec in records]

    async def create_organization(self, company_id: str, payload: OrganizationCreate) -> Organization:
        record = await self._create_entity("crm_organizations", company_id, payload.model_dump())
        return Organization.model_validate(record)

    async def update_organization(self, company_id: str, org_id: str, payload: OrganizationCreate) -> Organization:
        record = await self._update_entity("crm_organizations", company_id, org_id, payload.model_dump(exclude_unset=True))
        return Organization.model_validate(record)

    async def delete_organization(self, company_id: str, org_id: str) -> None:
        await self._delete_entity("crm_organizations", company_id, org_id)

    # Persons ------------------------------------------------------------
    async def list_persons(self, company_id: str) -> List[Person]:
        records = await self.repository.list("crm_persons", {"company_id": company_id})
        return [Person.model_validate(rec) for rec in records]

    async def create_person(self, company_id: str, payload: PersonCreate) -> Person:
        record = await self._create_entity("crm_persons", company_id, payload.model_dump())
        return Person.model_validate(record)

    async def update_person(self, company_id: str, person_id: str, payload: PersonCreate) -> Person:
        record = await self._update_entity("crm_persons", company_id, person_id, payload.model_dump(exclude_unset=True))
        return Person.model_validate(record)

    async def delete_person(self, company_id: str, person_id: str) -> None:
        await self._delete_entity("crm_persons", company_id, person_id)

    # Pipelines ----------------------------------------------------------
    async def list_pipelines(self, company_id: str) -> List[Pipeline]:
        records = await self.repository.list("crm_pipelines", {"company_id": company_id})
        return [Pipeline.model_validate(rec) for rec in records]

    async def create_pipeline(self, company_id: str, payload: PipelineCreate) -> Pipeline:
        record = await self._create_entity("crm_pipelines", company_id, payload.model_dump())
        return Pipeline.model_validate(record)

    async def update_pipeline(self, company_id: str, pipeline_id: str, payload: PipelineCreate) -> Pipeline:
        record = await self._update_entity("crm_pipelines", company_id, pipeline_id, payload.model_dump(exclude_unset=True))
        return Pipeline.model_validate(record)

    async def delete_pipeline(self, company_id: str, pipeline_id: str) -> None:
        await self._delete_entity("crm_pipelines", company_id, pipeline_id)

    async def list_pipeline_stages(self, company_id: str, pipeline_id: str | None = None) -> List[PipelineStage]:
        filters = {"company_id": company_id}
        if pipeline_id:
            filters["pipeline_id"] = pipeline_id
        records = await self.repository.list("crm_pipeline_stages", filters)
        return [PipelineStage.model_validate(rec) for rec in records]

    async def create_pipeline_stage(self, company_id: str, payload: PipelineStageCreate) -> PipelineStage:
        record = await self._create_entity("crm_pipeline_stages", company_id, payload.model_dump())
        return PipelineStage.model_validate(record)

    async def update_pipeline_stage(self, company_id: str, stage_id: str, payload: PipelineStageCreate) -> PipelineStage:
        record = await self._update_entity("crm_pipeline_stages", company_id, stage_id, payload.model_dump(exclude_unset=True))
        return PipelineStage.model_validate(record)

    async def delete_pipeline_stage(self, company_id: str, stage_id: str) -> None:
        await self._delete_entity("crm_pipeline_stages", company_id, stage_id)

    # Deals --------------------------------------------------------------
    async def list_deals(self, company_id: str) -> List[Deal]:
        records = await self.repository.list("crm_deals", {"company_id": company_id})
        return [Deal.model_validate(rec) for rec in records]

    async def create_deal(self, company_id: str, payload: DealCreate) -> Deal:
        record = await self._create_entity("crm_deals", company_id, payload.model_dump())
        return Deal.model_validate(record)

    async def update_deal(self, company_id: str, deal_id: str, payload: DealCreate) -> Deal:
        record = await self._update_entity("crm_deals", company_id, deal_id, payload.model_dump(exclude_unset=True))
        return Deal.model_validate(record)

    async def delete_deal(self, company_id: str, deal_id: str) -> None:
        await self._delete_entity("crm_deals", company_id, deal_id)

    # Activities ---------------------------------------------------------
    async def list_activities(self, company_id: str) -> List[Activity]:
        records = await self.repository.list("crm_activities", {"company_id": company_id})
        return [Activity.model_validate(rec) for rec in records]

    async def create_activity(self, company_id: str, payload: ActivityCreate, recipients: List[str] | None = None) -> Activity:
        record = await self._create_entity("crm_activities", company_id, payload.model_dump())
        activity = Activity.model_validate(record)
        if recipients:
            notification = ActivityNotification(activity=activity, recipients=recipients)
            await self.email_service.send_activity_notification(notification)
        if activity.type in {ActivityType.meeting, ActivityType.call} and activity.due_date:
            payload = await build_calendar_payload(record)
            await self.calendar_integration.push_event(payload)
        return activity

    async def update_activity(self, company_id: str, activity_id: str, payload: ActivityCreate) -> Activity:
        record = await self._update_entity("crm_activities", company_id, activity_id, payload.model_dump(exclude_unset=True))
        return Activity.model_validate(record)

    async def delete_activity(self, company_id: str, activity_id: str) -> None:
        await self._delete_entity("crm_activities", company_id, activity_id)

    # Files --------------------------------------------------------------
    async def list_files(self, company_id: str, related_id: str | None = None) -> List[CRMFile]:
        filters = {"company_id": company_id}
        if related_id:
            filters["deal_id"] = related_id
        records = await self.repository.list("crm_files", filters)
        return [CRMFile.model_validate(rec) for rec in records]

    async def create_file(self, company_id: str, payload: CRMFileCreate) -> CRMFile:
        record = await self._create_entity("crm_files", company_id, payload.model_dump())
        return CRMFile.model_validate(record)

    async def delete_file(self, company_id: str, file_id: str) -> None:
        await self._delete_entity("crm_files", company_id, file_id)

    # Custom fields ------------------------------------------------------
    async def list_custom_fields(self, company_id: str) -> List[CustomField]:
        records = await self.repository.list("custom_fields", {"company_id": company_id})
        return [CustomField.model_validate(rec) for rec in records]

    async def create_custom_field(self, company_id: str, payload: CustomFieldCreate) -> CustomField:
        record = await self._create_entity("custom_fields", company_id, payload.model_dump())
        return CustomField.model_validate(record)

    async def create_custom_field_value(self, company_id: str, payload: CustomFieldValueCreate) -> CustomFieldValue:
        record = await self._create_entity("custom_field_values", company_id, payload.model_dump())
        return CustomFieldValue.model_validate(record)

    # Dashboards ---------------------------------------------------------
    async def dashboard_summary(self, company_id: str) -> DashboardSummary:
        deals = await self.list_deals(company_id)
        activities = await self.list_activities(company_id)
        pipeline_counts = Counter(deal.pipeline_stage_id for deal in deals)
        activity_counts = Counter(activity.type.value for activity in activities)
        upcoming_tasks = [activity for activity in activities if activity.type == ActivityType.task and not activity.completed]
        upcoming_tasks.sort(key=lambda a: a.due_date or datetime.utcnow())
        return DashboardSummary(
            total_deals=len(deals),
            pipeline_by_stage=dict(pipeline_counts),
            activities_by_type=dict(activity_counts),
            upcoming_tasks=upcoming_tasks[:10],
        )

    async def activities_by_entity(self, company_id: str, entity: str, entity_id: str) -> List[Activity]:
        records = await self.repository.list("crm_activities", {"company_id": company_id, f"{entity}_id": entity_id})
        return [Activity.model_validate(rec) for rec in records]
