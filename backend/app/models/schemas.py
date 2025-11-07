from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, EmailStr, Field


class Role(str, Enum):
    admin = "admin"
    manager = "manager"
    sales = "sales"
    viewer = "viewer"


class UserContext(BaseModel):
    id: str
    email: EmailStr
    company_id: str
    role: str
    full_name: str | None = None


class TimestampedModel(BaseModel):
    id: str
    company_id: str
    created_at: datetime | None = None
    updated_at: datetime | None = None


class CompanyCreate(BaseModel):
    name: str


class Company(TimestampedModel):
    name: str


class UserBase(BaseModel):
    email: EmailStr
    full_name: str | None = None
    role: Role = Role.sales
    is_active: bool = True


class UserCreate(UserBase):
    password: str = Field(min_length=8)
    company_id: str | None = None


class User(UserBase):
    id: str
    company_id: str


class OrganizationBase(BaseModel):
    name: str
    domain: str | None = None
    description: str | None = None


class OrganizationCreate(OrganizationBase):
    pass


class Organization(TimestampedModel, OrganizationBase):
    pass


class PersonBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr | None = None
    phone: str | None = None
    organization_id: str | None = None
    title: str | None = None


class PersonCreate(PersonBase):
    pass


class Person(TimestampedModel, PersonBase):
    pass


class PipelineBase(BaseModel):
    name: str
    is_default: bool = False


class PipelineCreate(PipelineBase):
    pass


class Pipeline(TimestampedModel, PipelineBase):
    pass


class PipelineStageBase(BaseModel):
    pipeline_id: str
    name: str
    order: int
    probability: float | None = Field(default=None, ge=0, le=1)


class PipelineStageCreate(PipelineStageBase):
    pass


class PipelineStage(TimestampedModel, PipelineStageBase):
    pass


class DealBase(BaseModel):
    title: str
    value: float = Field(default=0, ge=0)
    pipeline_stage_id: str
    person_id: str | None = None
    organization_id: str | None = None
    owner_id: str
    status: str = "open"
    expected_close_date: datetime | None = None


class DealCreate(DealBase):
    pass


class Deal(TimestampedModel, DealBase):
    pass


class ActivityType(str, Enum):
    call = "call"
    email = "email"
    meeting = "meeting"
    task = "task"
    note = "note"


class ActivityBase(BaseModel):
    type: ActivityType
    subject: str
    description: str | None = None
    due_date: datetime | None = None
    completed: bool = False
    deal_id: str | None = None
    person_id: str | None = None
    organization_id: str | None = None
    owner_id: str


class ActivityCreate(ActivityBase):
    pass


class Activity(TimestampedModel, ActivityBase):
    pass


class CRMFileBase(BaseModel):
    name: str
    url: str
    deal_id: str | None = None
    person_id: str | None = None
    organization_id: str | None = None
    owner_id: str


class CRMFileCreate(CRMFileBase):
    pass


class CRMFile(TimestampedModel, CRMFileBase):
    pass


class CustomField(BaseModel):
    id: str
    company_id: str
    entity: str
    name: str
    field_type: str


class CustomFieldCreate(BaseModel):
    entity: str
    name: str
    field_type: str


class CustomFieldValue(BaseModel):
    id: str
    company_id: str
    custom_field_id: str
    entity_id: str
    value: str


class CustomFieldValueCreate(BaseModel):
    custom_field_id: str
    entity_id: str
    value: str


class AuthTokens(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    user: User


class RegisterRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)
    full_name: str
    company_name: str


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class RefreshRequest(BaseModel):
    refresh_token: str


class DashboardSummary(BaseModel):
    total_deals: int
    pipeline_by_stage: dict[str, int]
    activities_by_type: dict[str, int]
    upcoming_tasks: List[Activity]


class ActivityNotification(BaseModel):
    activity: Activity
    recipients: List[EmailStr]
