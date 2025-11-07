import os

os.environ.setdefault("CRM_TESTING", "true")

from fastapi.testclient import TestClient

from ..main import app

client = TestClient(app)


def register_admin():
    response = client.post(
        "/auth/register",
        json={
            "email": "admin@example.com",
            "password": "password123",
            "full_name": "Admin User",
            "company_name": "Example Corp",
        },
    )
    assert response.status_code == 200, response.text
    data = response.json()
    return data["access_token"], data["user"]["company_id"], data["user"]["id"]


def auth_headers(token: str):
    return {"Authorization": f"Bearer {token}"}


def test_crm_flow():
    token, company_id, user_id = register_admin()

    # Create organization
    org_response = client.post(
        "/api/organizations",
        json={"name": "Acme", "domain": "acme.com", "description": "Important customer"},
        headers=auth_headers(token),
    )
    assert org_response.status_code == 200
    organization = org_response.json()

    # Create contact
    person_response = client.post(
        "/api/persons",
        json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane@acme.com",
            "organization_id": organization["id"],
            "title": "CTO",
        },
        headers=auth_headers(token),
    )
    assert person_response.status_code == 200
    person = person_response.json()

    # Create pipeline and stage
    pipeline_response = client.post(
        "/api/pipelines",
        json={"name": "Sales", "is_default": True},
        headers=auth_headers(token),
    )
    assert pipeline_response.status_code == 200
    pipeline = pipeline_response.json()

    stage_response = client.post(
        "/api/pipelines/stages",
        json={"pipeline_id": pipeline["id"], "name": "Discovery", "order": 1, "probability": 0.2},
        headers=auth_headers(token),
    )
    assert stage_response.status_code == 200
    stage = stage_response.json()

    # Create deal
    deal_response = client.post(
        "/api/deals",
        json={
            "title": "New deal",
            "value": 1000,
            "pipeline_stage_id": stage["id"],
            "person_id": person["id"],
            "organization_id": organization["id"],
            "owner_id": user_id,
            "status": "open",
        },
        headers=auth_headers(token),
    )
    assert deal_response.status_code == 200
    deal = deal_response.json()

    # Create activity (task)
    activity_response = client.post(
        "/api/activities",
        json={
            "type": "task",
            "subject": "Follow up",
            "description": "Call the customer",
            "deal_id": deal["id"],
            "owner_id": user_id,
        },
        headers=auth_headers(token),
    )
    assert activity_response.status_code == 200

    # Dashboard summary reflects data
    dashboard_response = client.get("/api/dashboard/summary", headers=auth_headers(token))
    assert dashboard_response.status_code == 200
    summary = dashboard_response.json()
    assert summary["total_deals"] == 1
    assert summary["pipeline_by_stage"][stage["id"]] == 1
    assert summary["activities_by_type"]["task"] == 1

    # Tasks endpoint returns the created task
    tasks_response = client.get("/api/tasks", headers=auth_headers(token))
    assert tasks_response.status_code == 200
    tasks = tasks_response.json()
    assert len(tasks) == 1
    assert tasks[0]["subject"] == "Follow up"

    # Ensure we can list activities by entity
    activities_response = client.get(
        f"/api/activities/entity/deal/{deal['id']}",
        headers=auth_headers(token),
    )
    assert activities_response.status_code == 200
    assert len(activities_response.json()) == 1
