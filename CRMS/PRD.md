# Product Requirements Document: Modern CRM System

<div style="background: #1a1a2e; color: #F9FAFB; padding: 20px; border-left: 4px solid #6C63FF;">

**Document Version:** 1.0  
**Last Updated:** 2025-10-24  
**Status:** Active  
**Owner:** Product Team  
**Stakeholders:** Engineering, Design, QA, Business

</div>

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Product Vision & Objectives](#2-product-vision--objectives)
3. [Target Users & Personas](#3-target-users--personas)
4. [Success Metrics](#4-success-metrics)
5. [Technical Architecture](#5-technical-architecture)
6. [Feature Requirements](#6-feature-requirements)
7. [Data Models](#7-data-models)
8. [User Interface Specifications](#8-user-interface-specifications)
9. [Integration Requirements](#9-integration-requirements)
10. [Non-Functional Requirements](#10-non-functional-requirements)
11. [Development Roadmap](#11-development-roadmap)
12. [Risks & Mitigations](#12-risks--mitigations)
13. [Future Enhancements](#13-future-enhancements)
14. [Appendix](#14-appendix)

---

## 1. Executive Summary

### 1.1 Product Overview

A modern, user-friendly Customer Relationship Management (CRM) system designed specifically for small and medium-sized businesses. The system features a sleek dark-themed interface with purple undertones, offering comprehensive customer management, multi-channel communication tracking, and intelligent automation capabilities.

### 1.2 Problem Statement

Small and medium businesses struggle with:
- Fragmented customer data across multiple platforms (email, phone, spreadsheets)
- Inefficient manual processes for tracking customer interactions
- Lack of centralized communication history
- Poor visibility into customer complaints and their resolution status
- Limited automation leading to wasted time on routine tasks
- Difficulty scaling customer management as business grows

### 1.3 Proposed Solution

A unified platform that combines:
- **Centralized Customer Management**: All customer data in one place
- **Multi-Channel Communication Tracking**: Emails, calls, complaints, logs
- **Intelligent Automation**: Auto-categorization, routing, and notifications
- **Conversational Interfaces**: Both internal (for teams) and external (for customers)
- **Modern UX**: Dark-themed, intuitive interface optimized for productivity

### 1.4 Target Market

**Primary Users:**
- Small and Medium Business (SMB) owners (5-50 employees)
- Industries: B2B services, retail, consulting, manufacturing, technology

**Secondary Users:**
- Sales teams
- Customer support teams
- Administrative staff
- Business operations managers

### 1.5 Value Proposition

| User Segment | Core Value |
|--------------|------------|
| **Business Owners** | Complete visibility into customer relationships, reduced operational overhead |
| **Sales Teams** | Faster customer lookup, automated logging, improved follow-up tracking |
| **Support Teams** | Efficient complaint management, reduced resolution time, SLA tracking |
| **Administrators** | Centralized user management, role-based access control, audit trails |

### 1.6 Business Objectives

1. **Operational Efficiency**: Reduce time spent on manual data entry by 50%
2. **Customer Satisfaction**: Decrease complaint resolution time by 40%
3. **Team Productivity**: Enable teams to manage 3x more customers with same resources
4. **Data Centralization**: Eliminate data silos and provide single source of truth
5. **Scalability**: Support business growth from 5 to 50+ employees without system changes

### 1.7 Timeline & Delivery

**⚡ AGGRESSIVE TIMELINE: 8 WEEKS (2 MONTHS) TOTAL DELIVERY**

- **Phase 1 (Weeks 1-2):** Core MVP - Auth, Customers, Logs
- **Phase 2 (Weeks 3-4):** Email Integration, Advanced Search
- **Phase 3 (Weeks 5-6):** Complaints, SLA, Automation, Taiga
- **Phase 4 (Weeks 7-8):** VoIP, RBAC, Testing, Launch

**Requirements for Success:**
- 2-3 experienced full-stack developers (React + Python + Firebase)
- Full-time commitment, no distractions
- Pre-configured Firebase project and API credentials
- Ruthless scope control (no feature additions during 8 weeks)
- Daily standups and progress tracking

---

## 2. Product Vision & Objectives

### 2.1 Vision Statement

*"To empower small and medium businesses with enterprise-grade CRM capabilities through an intuitive, intelligent, and affordable platform that grows with their business."*

### 2.2 Product Goals

#### Primary Goals (MVP)
1. ✅ Provide an intuitive, modern interface for managing customer relationships
2. ✅ Centralize all customer interactions (emails, calls, complaints, logs) in one place
3. ✅ Enable multi-tenant architecture for multiple independent businesses
4. ✅ Implement role-based access control for secure collaboration
5. ✅ Integrate with Gmail for automated email tracking

#### Secondary Goals (Post-MVP)
6. ⭕ Enable conversational interfaces for both internal teams and external customers
7. ⭕ Automate routine tasks (email sorting, notifications, data entry)
8. ⭕ Integrate VoIP for in-app calling capabilities
9. ⭕ Provide voice command functionality for hands-free operation
10. ⭕ Connect with third-party issue tracking (Taiga)

### 2.3 Key Principles

1. **User-Centric Design**: Every feature must solve a real user problem
2. **Mobile-First**: Functionality must work seamlessly on mobile devices
3. **Performance**: Speed and responsiveness are non-negotiable
4. **Security**: Protect customer data with enterprise-grade security
5. **Scalability**: Architecture must support growth from day one
6. **Automation**: Reduce manual work wherever possible

### 2.4 Out of Scope (For MVP)

- ❌ iOS native application (web responsive only)
- ❌ Multi-language support
- ❌ Offline mode
- ❌ Payment gateway integration
- ❌ Document/contract management
- ❌ Social media monitoring
- ❌ WhatsApp/Slack integrations
- ❌ Advanced BI/analytics dashboard
- ❌ Custom workflow builder

---

## 3. Target Users & Personas

### Persona 1: Sarah - Business Owner

**Demographics:**
- Age: 35-50
- Role: CEO/Founder of 15-person B2B services company
- Tech Savvy: Moderate

**Goals:**
- Grow business without losing personal touch with customers
- Have visibility into all customer interactions
- Ensure no customer inquiries fall through the cracks
- Make data-driven decisions

**Pain Points:**
- Currently using spreadsheets + email + sticky notes
- Loses track of customer conversations
- Can't easily see which customers need attention
- Spends too much time on administrative tasks

**Use Cases:**
- Check daily dashboard for business health
- Review open complaints and critical issues
- Search for specific customer history before important calls
- Assign team members to new customers

**Success Criteria:**
- Can access any customer information in < 30 seconds
- Receives alerts for critical complaints
- Spends 50% less time on administrative tasks

---

### Persona 2: Mike - Sales Representative

**Demographics:**
- Age: 25-40
- Role: Sales rep managing 50-100 active prospects/customers
- Tech Savvy: High

**Goals:**
- Track all customer touchpoints
- Never miss a follow-up
- Close more deals faster
- Reduce time spent on data entry

**Pain Points:**
- Forgets to log calls and emails
- Misses follow-up deadlines
- Can't remember conversation history before calls
- Wastes time searching for customer information

**Use Cases:**
- Log customer calls immediately after hanging up
- Review customer timeline before sales call
- Search for customers by various criteria
- Use voice commands while driving to log notes

**Success Criteria:**
- Logging a call takes < 30 seconds
- Can find any customer info in < 15 seconds
- Never misses a scheduled follow-up
- Increases sales by 20% through better tracking

---

### Persona 3: Lisa - Customer Support Agent

**Demographics:**
- Age: 22-35
- Role: Support agent handling complaints and inquiries
- Tech Savvy: Moderate to High

**Goals:**
- Resolve customer complaints quickly
- Meet SLA requirements
- Provide excellent customer service
- Track resolution progress

**Pain Points:**
- Complaints arrive via multiple channels (email, phone, chat)
- Difficult to track complaint status
- No visibility into SLA deadlines
- Can't easily escalate complex issues

**Use Cases:**
- Create complaint tickets from emails/calls
- Update complaint status as progress is made
- Escalate technical issues to development team (Taiga)
- Check SLA countdown before end of day

**Success Criteria:**
- Creates complaint ticket in < 1 minute
- Clearly sees which complaints need immediate attention
- Reduces average resolution time by 30%
- Meets 95% of SLA deadlines

---

### Persona 4: Alex - IT Administrator

**Demographics:**
- Age: 28-45
- Role: Admin managing system and user access
- Tech Savvy: Very High

**Goals:**
- Ensure data security
- Manage user permissions efficiently
- Monitor system health
- Support integration needs

**Pain Points:**
- Manual user provisioning is time-consuming
- Difficult to audit who has access to what
- No visibility into system usage
- Integration setup is complex

**Use Cases:**
- Add/remove users and assign roles
- Review audit logs for compliance
- Configure integrations (Gmail, Taiga, VoIP)
- Monitor system performance and errors

**Success Criteria:**
- Can provision new user in < 5 minutes
- Complete visibility into access controls
- Zero security incidents
- All integrations running smoothly

---

## 4. Success Metrics

### 4.1 Product Success Metrics (KPIs)

#### Adoption Metrics
| Metric | Target | Measurement |
|--------|--------|-------------|
| **User Activation Rate** | 80% within 7 days | % of invited users who complete onboarding |
| **Daily Active Users (DAU)** | 70% of total users | Users who log in daily |
| **Feature Adoption** | 60% for core features | % of users who use each feature monthly |
| **User Retention (30-day)** | 85% | % of users still active after 30 days |

#### Efficiency Metrics
| Metric | Target | Measurement |
|--------|--------|-------------|
| **Time to Log Entry** | < 30 seconds | Average time from action to logged entry |
| **Time to Find Customer** | < 15 seconds | Average time from search to viewing customer |
| **Email Auto-Link Success** | 90% | % of emails correctly linked to customers |
| **Complaint Resolution Time** | 30% reduction | Average time from creation to resolution |

#### Quality Metrics
| Metric | Target | Measurement |
|--------|--------|-------------|
| **System Uptime** | 99.0% | % of time system is available |
| **Page Load Time** | < 2 seconds | 95th percentile load time |
| **Search Latency** | < 1 second | Time to return search results |
| **Email Sync Delay** | < 5 minutes | Time from email receipt to CRM sync |

#### Business Metrics
| Metric | Target | Measurement |
|--------|--------|-------------|
| **Customer Records per User** | 50-100 | Average number of customers managed |
| **Logs per Day per User** | 5-10 | Daily logging activity |
| **Customer Satisfaction (NPS)** | 40+ | Net Promoter Score |
| **Support Ticket Reduction** | 50% | Reduction in user support requests |

### 4.2 Feature-Specific Metrics

#### Email Integration
- ✅ 90% of emails auto-linked to correct customer
- ✅ < 5 minute sync delay
- ✅ 80% email categorization accuracy

#### Complaint Management
- ✅ 95% SLA adherence
- ✅ 30% reduction in resolution time
- ✅ 4.0+ customer satisfaction rating post-resolution

#### Conversational Interface
- ✅ 70% query accuracy for internal bot
- ✅ 50% deflection rate for external bot
- ✅ < 2 second response time

#### Voice Commands
- ✅ 85% command recognition accuracy
- ✅ 30% of mobile users adopt voice features
- ✅ < 3 second command execution time

### 4.3 Measurement & Reporting

**Tracking Tools:**
- Google Analytics for user behavior
- Firebase Analytics for mobile app
- Custom dashboard for business metrics
- Weekly automated reports to stakeholders

**Review Cadence:**
- Daily: System health and uptime
- Weekly: User adoption and engagement
- Monthly: Business impact and feature performance
- Quarterly: Strategic goal alignment

---

## 5. Technical Architecture

### 5.1 Technology Stack

#### Frontend Technologies
| Component | Technology | Version | Purpose |
|-----------|-----------|---------|---------|
| **Web Framework** | React | 18.x | Single-page application |
| **UI Framework** | TailwindCSS | 3.x | Styling and responsive design |
| **State Management** | React Context/Redux | Latest | Application state |
| **HTTP Client** | Axios | Latest | API communication |
| **Real-time Updates** | Firebase SDK | 9.x | Live data synchronization |
| **Rich Text Editor** | Quill / Draft.js | Latest | Log entry descriptions |
| **Date/Time** | date-fns | Latest | Date manipulation |
| **Forms** | React Hook Form | Latest | Form handling |
| **Routing** | React Router | 6.x | Navigation |

#### Mobile Technologies
| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Platform** | Android (Kotlin) | Native mobile app |
| **Min SDK** | Android 8.0 (API 26) | Minimum Android version |
| **Architecture** | MVVM | Clean architecture pattern |
| **Networking** | Retrofit + OkHttp | API communication |
| **Database** | Room + Firebase | Local + cloud storage |
| **Dependency Injection** | Hilt | DI framework |

#### Backend Technologies
| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Language** | Python | 3.10+ |
| **Framework** | FastAPI / Flask | REST API framework |
| **Database** | Firebase Firestore | NoSQL cloud database |
| **Authentication** | Firebase Auth | User authentication |
| **File Storage** | Firebase Storage | File/attachment storage |
| **Background Jobs** | Celery + Redis | Async task processing |
| **Email Processing** | n8n + Gmail API | Email automation |
| **VoIP** | Twilio SDK (TBD) | Voice calling |

#### Integration & Automation
| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Workflow Automation** | n8n | Email routing, automation |
| **Messaging** | Telegram Bot API | Notifications, chatbot |
| **Issue Tracking** | Taiga API | External issue management |
| **API Documentation** | OpenAPI/Swagger | API specification |

### 5.2 System Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                        CLIENT LAYER                              │
│                                                                   │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐  │
│  │ Web App      │  │ Mobile App   │  │ Telegram Bot         │  │
│  │ (React +     │  │ (Kotlin)     │  │ (External/Internal)  │  │
│  │  TailwindCSS)│  │              │  │                      │  │
│  └──────┬───────┘  └──────┬───────┘  └──────────┬───────────┘  │
│         │                  │                      │              │
└─────────┼──────────────────┼──────────────────────┼──────────────┘
          │                  │                      │
          │                  │                      │
          └──────────────────┴──────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                     API GATEWAY LAYER                            │
│                                                                   │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │  Python Backend (FastAPI)                                   │ │
│  │  - REST API endpoints                                       │ │
│  │  - Authentication middleware                                │ │
│  │  - Business logic                                           │ │
│  │  - Tenant isolation                                         │ │
│  └────────────────────────────────────────────────────────────┘ │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
          │
          │
          ▼
┌─────────────────────────────────────────────────────────────────┐
│                      SERVICE LAYER                               │
│                                                                   │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────────┐   │
│  │ Firebase │  │ Firebase │  │ Firebase │  │ Redis        │   │
│  │ Auth     │  │ Firestore│  │ Storage  │  │ (Cache)      │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────────┘   │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
          │
          │
          ▼
┌─────────────────────────────────────────────────────────────────┐
│                   INTEGRATION LAYER                              │
│                                                                   │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────────┐   │
│  │ n8n      │  │ Gmail    │  │ Telegram │  │ Taiga API    │   │
│  │ Workflow │  │ API      │  │ Bot API  │  │              │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────────┘   │
│                                                                   │
│  ┌──────────┐  ┌──────────────────────────────────────────┐   │
│  │ VoIP     │  │ Future Integrations                       │   │
│  │ Provider │  │ (WhatsApp, Slack, etc.)                  │   │
│  └──────────┘  └──────────────────────────────────────────┘   │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

### 5.3 Data Flow

#### Email Integration Flow
```
1. Email arrives at Gmail
2. Gmail API triggers webhook to n8n
3. n8n workflow processes email:
   - Extracts sender, subject, content
   - Identifies customer (via email lookup)
   - Categorizes email (sales, support, complaint)
   - Determines priority
4. n8n calls Python Backend API
5. Backend creates log entry in Firestore
6. Firebase triggers real-time update to connected clients
7. User receives notification (if applicable)
```

#### Complaint Creation Flow
```
1. User creates complaint via web/mobile
2. Frontend validates and sends to API
3. Backend:
   - Creates complaint record in Firestore
   - Generates unique ticket number
   - Applies auto-assignment rules
   - Sets SLA deadlines
   - Creates timeline entry
4. If integration enabled:
   - Creates linked Taiga issue
   - Stores Taiga issue ID
5. Notifications sent:
   - Assigned user (Telegram/Email)
   - Customer (confirmation email)
6. Real-time update pushed to all connected clients
```

#### Voice Command Flow
```
1. User presses voice button / says wake word
2. Audio captured by client (web/mobile)
3. Audio sent to Speech-to-Text API
4. Text transcription received
5. Backend NLP engine:
   - Identifies intent (search, create, update, etc.)
   - Extracts entities (customer name, date, etc.)
   - Determines required action
6. Action executed via normal API
7. Result returned to user (visual + optional audio)
```

### 5.4 Database Architecture

#### Firestore Collections Structure

```
/tenants
  /{tenantId}
    - companyName
    - subdomain
    - branding
    - subscription
    - settings
    - createdAt

/users
  /{userId}
    - tenantId
    - email
    - displayName
    - role
    - permissions[]
    - preferences
    - lastLogin
    - createdAt

/customers
  /{customerId}
    - tenantId
    - companyName
    - contactPerson
    - additionalContacts[]
    - address
    - tags[]
    - customFields
    - status
    - assignedTo
    - createdAt
    - updatedAt

/logs
  /{logId}
    - tenantId
    - customerId
    - threadId (optional)
    - type
    - category
    - subject
    - description
    - attachments[]
    - tags[]
    - createdBy
    - createdAt

/complaints
  /{complaintId}
    - ticketNumber
    - tenantId
    - customerId
    - title
    - description
    - category
    - severity
    - status
    - assignedTo
    - taigaIssueId
    - sla
    - timeline[]
    - resolution
    - internalComments[]
    - customerUpdates[]
    - createdAt

/emails
  /{emailId}
    - tenantId
    - customerId (if linked)
    - gmailMessageId
    - threadId
    - from
    - to
    - subject
    - body
    - attachments[]
    - category
    - priority
    - linkedLogId
    - receivedAt

/calls
  /{callId}
    - tenantId
    - customerId
    - phoneNumber
    - direction (inbound/outbound)
    - duration
    - recordingUrl
    - outcome
    - notes
    - userId
    - linkedLogId
    - createdAt
```

#### Security Rules

**Firestore Security Rules (Example):**
```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    
    // Helper function: Check if user is authenticated
    function isAuthenticated() {
      return request.auth != null;
    }
    
    // Helper function: Get user's tenant ID
    function getUserTenant() {
      return get(/databases/$(database)/documents/users/$(request.auth.uid)).data.tenantId;
    }
    
    // Helper function: Check if user has role
    function hasRole(role) {
      return get(/databases/$(database)/documents/users/$(request.auth.uid)).data.role == role;
    }
    
    // Tenants collection
    match /tenants/{tenantId} {
      allow read: if isAuthenticated() && getUserTenant() == tenantId;
      allow write: if hasRole('tenant_admin') && getUserTenant() == tenantId;
    }
    
    // Customers collection
    match /customers/{customerId} {
      allow read: if isAuthenticated() && 
                     resource.data.tenantId == getUserTenant();
      allow create: if isAuthenticated() && 
                       request.resource.data.tenantId == getUserTenant();
      allow update, delete: if isAuthenticated() && 
                               resource.data.tenantId == getUserTenant() &&
                               (hasRole('tenant_admin') || hasRole('manager'));
    }
    
    // Similar rules for other collections...
  }
}
```

### 5.5 API Specifications

#### Core API Endpoints

**Authentication**
```
POST   /api/v1/auth/login
POST   /api/v1/auth/logout
POST   /api/v1/auth/refresh
GET    /api/v1/auth/me
```

**Customers**
```
GET    /api/v1/customers              # List customers (with pagination)
GET    /api/v1/customers/:id          # Get customer details
POST   /api/v1/customers              # Create customer
PUT    /api/v1/customers/:id          # Update customer
DELETE /api/v1/customers/:id          # Delete customer
GET    /api/v1/customers/:id/timeline # Get customer timeline
GET    /api/v1/customers/search       # Search customers
```

**Logs**
```
GET    /api/v1/logs                   # List logs
GET    /api/v1/logs/:id               # Get log details
POST   /api/v1/logs                   # Create log
PUT    /api/v1/logs/:id               # Update log
DELETE /api/v1/logs/:id               # Delete log
POST   /api/v1/logs/:id/attachments   # Upload attachment
```

**Complaints**
```
GET    /api/v1/complaints             # List complaints
GET    /api/v1/complaints/:id         # Get complaint details
POST   /api/v1/complaints             # Create complaint
PUT    /api/v1/complaints/:id         # Update complaint
PATCH  /api/v1/complaints/:id/status  # Update status
POST   /api/v1/complaints/:id/comments # Add internal comment
POST   /api/v1/complaints/:id/updates  # Send customer update
GET    /api/v1/complaints/:id/taiga   # Get linked Taiga issue
```

**Email**
```
GET    /api/v1/emails                 # List emails
GET    /api/v1/emails/:id             # Get email details
POST   /api/v1/emails/send            # Send email
POST   /api/v1/emails/:id/link        # Link email to customer
```

**Search**
```
POST   /api/v1/search                 # Global search
```

**Users & Access**
```
GET    /api/v1/users                  # List users (admin only)
POST   /api/v1/users/invite           # Invite user
PUT    /api/v1/users/:id/role         # Update user role
DELETE /api/v1/users/:id              # Deactivate user
```

**Integrations**
```
POST   /api/v1/integrations/taiga/connect
POST   /api/v1/integrations/gmail/sync
POST   /api/v1/integrations/telegram/webhook
```

**Conversational Interface**
```
POST   /api/v1/chat/message           # Send message to bot
GET    /api/v1/chat/history           # Get chat history
```

### 5.6 Scalability Considerations

#### Current Scale (MVP Target)
- **Users**: 5-15 concurrent users per tenant
- **Tenants**: 5-10 active tenants
- **Customers**: 200-500 per tenant
- **Logs**: 100-300 per day per tenant
- **Emails**: 50-200 per day per tenant

#### Future Scale (6-12 months)
- **Users**: 50-100 concurrent users per tenant
- **Tenants**: 50-100 active tenants
- **Customers**: 5,000-10,000 per tenant
- **Logs**: 1,000-5,000 per day per tenant
- **Emails**: 500-2,000 per day per tenant

#### Scaling Strategy
1. **Database Optimization**:
   - Implement compound indexes for frequent queries
   - Use Firestore pagination (cursor-based)
   - Implement data archiving for old records (> 1 year)
   
2. **Caching**:
   - Redis for frequently accessed data
   - Cache customer lists, user profiles
   - Invalidate cache on updates
   
3. **API Optimization**:
   - Implement rate limiting per user/tenant
   - Use connection pooling
   - Implement request queuing for heavy operations
   
4. **Frontend Optimization**:
   - Lazy loading of components
   - Virtual scrolling for long lists
   - Debounced search queries
   - Optimistic UI updates
   
5. **Background Processing**:
   - Async processing for email sync
   - Queue-based processing for bulk operations
   - Scheduled jobs for cleanup tasks

---

## 6. Feature Requirements

### Feature Priority Levels
- **P0 (Critical)**: Must have for MVP, system doesn't work without it
- **P1 (High)**: Important for user satisfaction, include in MVP if time permits
- **P2 (Medium)**: Nice to have, defer to Phase 2/3
- **P3 (Low)**: Future enhancement

---

### 6.1 Feature: Authentication & Authorization
**Priority**: P0 (Critical)  
**Epic**: User Management  
**Phase**: 1 (MVP)

#### Description
Secure user authentication and authorization system using Firebase Auth, with support for multiple tenants and role-based access control.

#### User Stories
1. **As a new user**, I want to sign up with email/password so that I can access the CRM
2. **As a returning user**, I want to log in with my credentials so that I can resume work
3. **As a user**, I want to reset my password if I forget it
4. **As a tenant admin**, I want to invite team members so they can collaborate
5. **As a super admin**, I want to manage all tenants and users

#### Functional Requirements

**FR-AUTH-001: User Registration**
- Allow new users to sign up with email and password
- Validate email format and password strength
- Require email verification before first login
- Auto-assign to tenant based on invitation or create new tenant

**FR-AUTH-002: User Login**
- Support email/password authentication via Firebase Auth
- Implement "Remember Me" functionality (30-day session)
- Redirect to appropriate dashboard based on role
- Track last login timestamp

**FR-AUTH-003: Password Reset**
- Send password reset email via Firebase
- Allow user to set new password via secure link
- Expire reset link after 24 hours

**FR-AUTH-004: Session Management**
- Maintain active session for 24 hours with activity
- Auto-logout after 24 hours of inactivity
- Support concurrent sessions (multiple devices)
- Allow user to view and revoke active sessions

**FR-AUTH-005: Role-Based Access Control**
- Support roles: Super Admin, Tenant Admin, Manager, Sales Rep, Support Agent, Viewer
- Enforce permissions at API level
- Dynamically hide/show UI elements based on permissions
- Prevent privilege escalation

#### Acceptance Criteria
- ✅ User can register with valid email and strong password
- ✅ User receives verification email within 2 minutes
- ✅ User can log in and access appropriate dashboard
- ✅ Password reset works and link expires after 24 hours
- ✅ Sessions auto-logout after 24 hours
- ✅ Users cannot access resources beyond their permissions
- ✅ All authentication API calls complete in < 500ms

#### Technical Implementation
- **Frontend**: Firebase SDK for authentication
- **Backend**: Firebase Admin SDK for token verification
- **Database**: User records in Firestore with role/permissions
- **Security**: JWT tokens, HTTPS only, secure password hashing

#### Dependencies
- Firebase project setup
- Email service configuration

#### Risks & Mitigations
| Risk | Mitigation |
|------|------------|
| Firebase Auth downtime | Implement graceful error handling, show user-friendly messages |
| Password strength issues | Enforce minimum requirements (8+ chars, uppercase, lowercase, number) |
| Session hijacking | Use secure tokens, HTTPS only, implement session timeout |

---

### 6.2 Feature: Multi-Tenancy Architecture
**Priority**: P0 (Critical)  
**Epic**: Core Infrastructure  
**Phase**: 1 (MVP)

#### Description
Complete data isolation between different companies (tenants) sharing the same CRM instance, with tenant-specific configuration and branding.

#### User Stories
1. **As a business owner**, I want my company data completely isolated from others
2. **As a tenant admin**, I want to customize branding for my organization
3. **As a super admin**, I want to manage multiple tenant accounts
4. **As a developer**, I want automatic tenant filtering on all queries

#### Functional Requirements

**FR-TENANT-001: Tenant Isolation**
- All database records must include tenantId
- Automatic tenant filtering on all queries
- No cross-tenant data access permitted
- Firestore security rules enforce tenant boundaries

**FR-TENANT-002: Tenant Creation**
- New tenant created during first user registration
- Assign unique tenant ID (UUID)
- Create default settings and configuration
- Setup tenant admin account

**FR-TENANT-003: Tenant Configuration**
- Subdomain or tenant identifier (e.g., acme.yourcrm.com)
- Custom branding (logo, primary color, secondary color)
- Company information (name, address, contact)
- Timezone and locale settings

**FR-TENANT-004: Tenant Management (Super Admin)**
- View all tenants
- Create/edit tenant settings
- Activate/deactivate tenants
- View tenant usage statistics

**FR-TENANT-005: Data Partitioning**
- All Firestore collections include tenantId
- Compound indexes for tenant-based queries
- Prevent accidental cross-tenant queries

#### Acceptance Criteria
- ✅ New tenant created automatically on first user registration
- ✅ All data queries filtered by tenantId
- ✅ User from Tenant A cannot access any data from Tenant B
- ✅ Tenant admin can customize logo and colors
- ✅ Security rules prevent cross-tenant access
- ✅ All queries include tenant context (verified via logs)

#### Technical Implementation
```python
# Example: Automatic tenant filtering middleware
@app.before_request
def inject_tenant():
    if request.path.startswith('/api/'):
        user = get_current_user()
        g.tenant_id = user['tenantId']

# Example: Firestore query with tenant filter
def get_customers(tenant_id, limit=50):
    return db.collection('customers') \
             .where('tenantId', '==', tenant_id) \
             .limit(limit) \
             .stream()
```

#### Dependencies
- User authentication system
- Firestore database setup

#### Risks & Mitigations
| Risk | Mitigation |
|------|------------|
| Data leakage between tenants | Comprehensive security rules testing, automated tests |
| Performance degradation with many tenants | Proper indexing, query optimization |
| Tenant subdomain conflicts | Validate subdomain uniqueness on creation |

---

### 6.3 Feature: Customer Management (CRUD)
**Priority**: P0 (Critical)  
**Epic**: Customer Management  
**Phase**: 1 (MVP)

#### Description
Complete customer relationship management with ability to create, read, update, and delete customer records, including contact information, company details, and custom fields.

#### User Stories
1. **As a sales rep**, I want to add new customers quickly so I can start tracking them
2. **As a user**, I want to view complete customer information in one place
3. **As a manager**, I want to update customer details when information changes
4. **As a user**, I want to search and filter customers easily
5. **As a manager**, I want to archive/delete customers who are no longer active

#### Functional Requirements

**FR-CUST-001: Create Customer**
- Form with fields: company name, contact person (first/last name, email, phone, role)
- Optional fields: additional contacts, address, tags, custom fields
- Validate email format and phone format
- Auto-assign customer to creator (unless specified)
- Support bulk import via CSV

**FR-CUST-002: View Customer**
- Display all customer information in organized sections
- Show customer status (Active, Inactive, Prospect)
- Display assigned team member
- Show creation date and last updated date
- Quick actions: Call, Email, Add Log, Edit

**FR-CUST-003: Update Customer**
- Edit any field except system-generated (ID, creation date)
- Track update history (who changed what and when)
- Validate data before saving
- Support partial updates (don't require all fields)

**FR-CUST-004: Delete/Archive Customer**
- Soft delete (mark as inactive) by default
- Permanent delete only for tenant_admin role
- Warn if customer has associated data (logs, complaints)
- Option to delete or archive associated data

**FR-CUST-005: Customer List View**
- Table view with columns: Company, Contact, Phone, Email, Status, Assigned To
- Grid/card view option
- Pagination (50 customers per page)
- Sort by: Name, Created Date, Last Activity
- Filter by: Status, Assigned To, Tags, Date Range

**FR-CUST-006: Custom Fields**
- Allow tenant admin to define custom fields
- Field types: text, number, date, dropdown, checkbox
- Custom fields available on customer form
- Display custom fields in customer view

**FR-CUST-007: Tags**
- Add/remove tags to customers
- Tag autocomplete from existing tags
- Filter customers by tags
- Tag management (rename, delete, merge tags)

#### Acceptance Criteria
- ✅ User can create customer in < 1 minute
- ✅ All required fields validated before save
- ✅ Customer list loads in < 2 seconds (for 500 customers)
- ✅ Search returns results in < 1 second
- ✅ Updates immediately reflected across all connected clients
- ✅ Deleted customers don't appear in main list but recoverable
- ✅ Custom fields work for all field types
- ✅ Tags autocomplete and filter correctly

#### UI Mockup Description

**Customer List Page:**
```
┌─────────────────────────────────────────────────────────┐
│ [🔍 Search customers...]              [+ Add Customer]  │
├─────────────────────────────────────────────────────────┤
│ Filters: [All Status ▼] [All Users ▼] [Tags ▼]        │
├─────────────────────────────────────────────────────────┤
│ Company         │ Contact       │ Phone      │ Status  │
├─────────────────────────────────────────────────────────┤
│ Acme Corp       │ John Smith    │ 555-0100  │ ● Active│
│ Beta Industries │ Jane Doe      │ 555-0200  │ ● Active│
│ Gamma LLC       │ Bob Johnson   │ 555-0300  │ ○ Prospect│
│ ...             │ ...           │ ...       │ ...     │
├─────────────────────────────────────────────────────────┤
│ < Previous    Page 1 of 10    Next >                   │
└─────────────────────────────────────────────────────────┘
```

**Customer Detail Page:**
```
┌─────────────────────────────────────────────────────────┐
│ [← Back] Acme Corp                    [Edit] [Archive]  │
├─────────────────────────────────────────────────────────┤
│ 📞 Call │ ✉ Email │ 📝 Add Log                          │
├──────────────────────────┬──────────────────────────────┤
│ Company Information      │  Timeline                    │
│ ────────────────────     │  ────────                    │
│ Contact: John Smith      │  [All] [Calls] [Emails]      │
│ Email: john@acme.com     │                              │
│ Phone: 555-0100          │  📧 Email sent - 2h ago      │
│ Status: Active           │  📞 Call logged - 5h ago     │
│ Assigned: Mike S.        │  📝 Note added - 1d ago      │
│ Tags: [VIP] [Tech]       │  📋 Sample sent - 3d ago     │
│                          │  ...                         │
│ Address:                 │  [Load more]                 │
│ 123 Main St              │                              │
│ New York, NY 10001       │                              │
│                          │                              │
└──────────────────────────┴──────────────────────────────┘
```

#### Technical Implementation

**Database Schema:**
```javascript
{
  id: "cust_abc123",
  tenantId: "tenant_xyz789",
  companyName: "Acme Corp",
  contactPerson: {
    firstName: "John",
    lastName: "Smith",
    email: "john@acme.com",
    phone: "+15550100",
    role: "CEO"
  },
  additionalContacts: [],
  address: {
    street: "123 Main St",
    city: "New York",
    state: "NY",
    zip: "10001",
    country: "USA"
  },
  tags: ["VIP", "Tech"],
  customFields: {
    industry: "Technology",
    employeeCount: 50
  },
  status: "active",
  assignedTo: "user_mike123",
  createdAt: "2025-10-01T10:00:00Z",
  updatedAt: "2025-10-20T15:30:00Z",
  createdBy: "user_mike123"
}
```

**API Endpoints:**
```
GET    /api/v1/customers?page=1&limit=50&status=active
GET    /api/v1/customers/:id
POST   /api/v1/customers
PUT    /api/v1/customers/:id
DELETE /api/v1/customers/:id
GET    /api/v1/customers/search?q=acme
POST   /api/v1/customers/import (CSV upload)
```

#### Dependencies
- Authentication system
- Multi-tenancy architecture
- File upload service (for bulk import)

#### Risks & Mitigations
| Risk | Mitigation |
|------|------------|
| Duplicate customer creation | Implement duplicate detection (fuzzy match on company name + email) |
| Data validation errors | Comprehensive frontend and backend validation |
| Performance with large datasets | Pagination, indexing, virtual scrolling |
| Bulk import errors | Validate CSV before import, show preview, allow corrections |

---

### 6.4 Feature: Comprehensive Logging System
**Priority**: P0 (Critical)  
**Epic**: Activity Tracking  
**Phase**: 1 (MVP)

#### Description
Record and track all interactions, samples, and people associated with customers. Supports multiple log types with rich text descriptions, attachments, and automatic logging from integrations.

#### User Stories
1. **As a sales rep**, I want to quickly log customer calls so I can track interactions
2. **As a user**, I want to add detailed notes with formatting and attachments
3. **As a manager**, I want to view all activity logs for a customer in chronological order
4. **As a support agent**, I want emails and calls to be automatically logged
5. **As a user**, I want to edit or delete my own logs

#### Functional Requirements

**FR-LOG-001: Log Types**
Support multiple log types:
- **Call**: Phone conversations (inbound/outbound)
- **Email**: Email communications (auto-logged or manual)
- **Meeting**: In-person or virtual meetings
- **Note**: General notes and observations
- **Sample**: Product samples sent to customer
- **Demo**: Product demonstrations conducted
- **Quote**: Quotes or proposals sent
- **Other**: Miscellaneous interactions

**FR-LOG-002: Create Log**
- Select customer (required)
- Select log type (required)
- Enter subject/title (required, max 200 chars)
- Enter description (optional, rich text editor)
- Add attachments (optional, max 10MB per file, max 5 files)
- Add tags (optional, autocomplete)
- Optionally link to thread (for grouped logs)
- Auto-fill timestamp (editable)
- Auto-fill creator (current user)

**FR-LOG-003: Rich Text Editor**
- Formatting: Bold, italic, underline, strikethrough
- Lists: Ordered and unordered
- Links: Insert hyperlinks
- Mentions: @mention team members (triggers notification)
- Code blocks: For technical discussions
- Emoji support

**FR-LOG-004: Attachments**
- Supported file types: PDF, DOC, XLS, images (JPG, PNG), ZIP
- Upload via drag-and-drop or file picker
- Show upload progress
- Preview images inline
- Download attachments
- Delete attachments (if owner of log)

**FR-LOG-005: View Logs**
- Timeline view (chronological, most recent first)
- Filter by type, date range, creator, tags
- Search within logs
- Expandable/collapsible details
- Show preview with "Read more" link

**FR-LOG-006: Edit/Delete Logs**
- Edit own logs within 24 hours of creation
- Managers can edit any logs
- Show "Edited" indicator with timestamp
- Soft delete (archive) logs
- Permanent delete only for admins

**FR-LOG-007: Auto-Logging**
- Automatically create log entries from:
  - Email sync (Gmail API)
  - Call completion (VoIP integration)
  - Meeting invites (Calendar integration - future)
- Allow user to edit auto-generated logs
- Option to disable auto-logging per user

**FR-LOG-008: Bulk Operations**
- Export logs to CSV/PDF
- Bulk delete selected logs
- Bulk tag addition

#### Acceptance Criteria
- ✅ User can create log entry in < 30 seconds
- ✅ Rich text editor supports all formatting options
- ✅ File upload works via drag-and-drop
- ✅ Attachments under 10MB upload successfully
- ✅ Logs appear in customer timeline immediately
- ✅ Auto-logged emails appear within 5 minutes
- ✅ Search returns relevant logs in < 1 second
- ✅ Edits are tracked with timestamp and editor name
- ✅ @mentions trigger notifications

#### UI Mockup Description

**Create Log Form:**
```
┌─────────────────────────────────────────────┐
│ Create Log Entry                       [×]  │
├─────────────────────────────────────────────┤
│ Customer: [Acme Corp          ▼]           │
│ Type:     [Call               ▼]           │
│ Subject:  [________________________]        │
│                                             │
│ Description:                                │
│ ┌─────────────────────────────────────────┐ │
│ │ [B I U] [List] [Link] [@] [Emoji]      │ │
│ │                                         │ │
│ │ Discussed Q4 roadmap...                │ │
│ │                                         │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ Attachments: [📎 Choose files]              │
│                                             │
│ Tags: [VIP] [×] [Roadmap] [×]              │
│       [+ Add tag]                           │
│                                             │
│ Date: [2025-10-24] [15:30]                 │
│                                             │
│         [Cancel]  [Save Log]                │
└─────────────────────────────────────────────┘
```

**Timeline View (in Customer Detail):**
```
┌─────────────────────────────────────────────┐
│ Timeline                                    │
│ [All] [Calls] [Emails] [Notes] [Samples]   │
│ [🔍 Search logs...]                         │
├─────────────────────────────────────────────┤
│ 📞 Call - Discussed Q4 roadmap              │
│    John Smith • 2 hours ago                 │
│    "Talked about new features and pricing...│
│    [Read more]                              │
│                                             │
│ ✉ Email - Re: Proposal                     │
│    Auto-logged • 5 hours ago                │
│    "Thanks for the detailed proposal. We... │
│    [Read more] [View in Gmail]              │
│                                             │
│ 📝 Note - Customer feedback                 │
│    Mike S. • 1 day ago                      │
│    "Customer mentioned they need better...  │
│    [Read more] [Edit]                       │
│                                             │
│ 📦 Sample - Sent product demo kit           │
│    Sarah L. • 3 days ago                    │
│    Tracking: #TRACK12345                    │
│    [View details]                           │
│                                             │
│         [Load more activities]              │
└─────────────────────────────────────────────┘
```

#### Technical Implementation

**Database Schema:**
```javascript
{
  id: "log_abc123",
  tenantId: "tenant_xyz789",
  customerId: "cust_abc123",
  threadId: null, // Optional: for grouped logs
  type: "call",
  category: "sales",
  subject: "Discussed Q4 roadmap",
  description: "<p>Talked about <strong>new features</strong>...</p>",
  attachments: [
    {
      filename: "roadmap.pdf",
      url: "https://storage/.../roadmap.pdf",
      size: 245678,
      type: "application/pdf",
      uploadedAt: "2025-10-24T15:32:00Z"
    }
  ],
  tags: ["VIP", "Roadmap"],
  createdAt: "2025-10-24T15:30:00Z",
  createdBy: "user_mike123",
  updatedAt: null,
  updatedBy: null,
  isAutoLogged: false,
  sourceType: "manual" // manual, email, call, calendar
}
```

**API Endpoints:**
```
GET    /api/v1/logs?customerId=xxx&type=call&page=1
GET    /api/v1/logs/:id
POST   /api/v1/logs
PUT    /api/v1/logs/:id
DELETE /api/v1/logs/:id
POST   /api/v1/logs/:id/attachments
DELETE /api/v1/logs/:id/attachments/:attachmentId
GET    /api/v1/logs/search?q=roadmap
POST   /api/v1/logs/export (CSV/PDF)
```

#### Dependencies
- Customer management system
- File storage (Firebase Storage)
- Rich text editor library (Quill.js or Draft.js)
- Email integration (for auto-logging)

#### Risks & Mitigations
| Risk | Mitigation |
|------|------------|
| Large attachments slow down page | Lazy load attachments, show thumbnails only |
| Rich text XSS vulnerabilities | Sanitize HTML input, use trusted library |
| Auto-logged emails create spam | Allow users to configure auto-log rules |
| Storage costs for attachments | Implement file size limits, compression |

---

### 6.5 Feature: Customer History & Timeline
**Priority**: P0 (Critical)  
**Epic**: Customer Management  
**Phase**: 1 (MVP)

#### Description
Comprehensive, chronological view of all customer interactions with support for multiple simultaneous interaction threads (e.g., Project A and Support Issue B running concurrently).

#### User Stories
1. **As a sales rep**, I want to see complete customer history before a call
2. **As a support agent**, I want to view all complaints for a customer
3. **As a manager**, I want to understand customer relationship over time
4. **As a user**, I want to track multiple projects with the same customer separately
5. **As a user**, I want to quickly switch between different interaction streams

#### Functional Requirements

**FR-HIST-001: Timeline Display**
- Chronological display of all events (newest first)
- Each event shows: Type icon, Title, Creator, Timestamp, Preview
- Color-coded by event type:
  - Calls: Blue
  - Emails: Green
  - Complaints: Red
  - Samples: Purple
  - Notes: Gray
- Expandable/collapsible detail view

**FR-HIST-002: Event Types**
Display all types of interactions:
- Log entries (all types)
- Complaints (created, status changes, resolutions)
- Emails (sent/received)
- Calls (inbound/outbound)
- Samples sent
- Quotes/proposals
- Invoices (if applicable)
- System events (customer created, assigned to changed)

**FR-HIST-003: Multiple Interaction Threads**
- Support creating separate threads for different projects/issues
- Each thread has a name (e.g., "Q4 Contract Renewal", "Technical Support Case #123")
- Ability to create new thread from timeline
- Events can be assigned to specific threads
- Thread selector/filter at top of timeline
- Visual indication of which thread an event belongs to

**FR-HIST-004: Thread Management**
- Create thread: Name, Description, Start date
- Assign events to thread (drag-and-drop or edit event)
- Close/Archive thread
- Reopen thread if needed
- Thread summary: Event count, date range, status

**FR-HIST-005: Filtering & Search**
- Filter by event type (multi-select)
- Filter by date range (presets: Today, This Week, This Month, Custom)
- Filter by thread
- Filter by creator/team member
- Search within timeline (event titles and descriptions)
- Save filter presets

**FR-HIST-006: Timeline Navigation**
- Infinite scroll (load more as user scrolls)
- Jump to date functionality
- "Back to top" button
- Pagination option (50 events per page)

**FR-HIST-007: Quick Actions**
- Quick reply (for emails)
- Quick call (launch call interface)
- Add note to event (commentary)
- Share timeline section (export to PDF)

#### Acceptance Criteria
- ✅ Complete customer history loads in < 2 seconds
- ✅ Timeline displays minimum 50 events without lag
- ✅ Threads visually distinct and easy to navigate
- ✅ Filter changes apply instantly (< 500ms)
- ✅ Search returns results in < 1 second
- ✅ Events update in real-time across all connected clients
- ✅ Timeline scrolling is smooth (60fps)
- ✅ Works on mobile with touch gestures

#### UI Mockup Description

**Timeline with Threads:**
```
┌─────────────────────────────────────────────────────────┐
│ Customer History: Acme Corp                             │
├─────────────────────────────────────────────────────────┤
│ Thread: [All Threads ▼] [+ New Thread]                  │
│         ├─ All Activity                                  │
│         ├─ 📂 Q4 Contract Renewal (12 events)           │
│         ├─ 📂 Technical Support Case #456 (8 events)    │
│         └─ 📂 Archived Threads (3)                       │
├─────────────────────────────────────────────────────────┤
│ Filter: [All Types ▼] [All Time ▼] [All Users ▼]       │
│ [🔍 Search timeline...]                                  │
├─────────────────────────────────────────────────────────┤
│                                                          │
│ ┌─────────────────────────────────────────────────┐    │
│ │ 📞 CALL • Q4 Contract Renewal                   │    │
│ │ Mike S. • 2 hours ago                           │    │
│ │ "Discussed renewal terms and pricing options..." │    │
│ │ [Expand] [Add Note] [Reply]                     │    │
│ └─────────────────────────────────────────────────┘    │
│                                                          │
│ ┌─────────────────────────────────────────────────┐    │
│ │ ✉ EMAIL • Q4 Contract Renewal                  │    │
│ │ Auto-logged • 5 hours ago                       │    │
│ │ "Re: Pricing proposal for Q4"                   │    │
│ │ [Expand] [View in Gmail]                        │    │
│ └─────────────────────────────────────────────────┘    │
│                                                          │
│ ┌─────────────────────────────────────────────────┐    │
│ │ 🔴 COMPLAINT • Technical Support Case #456      │    │
│ │ Sarah L. • 1 day ago • Status: In Progress      │    │
│ │ "Login issues with mobile app"                  │    │
│ │ [View Details] [Update Status]                  │    │
│ └─────────────────────────────────────────────────┘    │
│                                                          │
│ ┌─────────────────────────────────────────────────┐    │
│ │ 📝 NOTE • General                               │    │
│ │ Mike S. • 3 days ago                            │    │
│ │ "Customer mentioned interest in new features"   │    │
│ │ [Edit] [Delete]                                 │    │
│ └─────────────────────────────────────────────────┘    │
│                                                          │
│               [Load more activities]                     │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

**Expanded Event View:**
```
┌─────────────────────────────────────────────────────────┐
│ 📞 CALL • Q4 Contract Renewal                    [Collapse] │
├─────────────────────────────────────────────────────────┤
│ Date: October 24, 2025 at 3:30 PM                      │
│ Creator: Mike S.                                        │
│ Duration: 45 minutes                                    │
│ Thread: Q4 Contract Renewal                             │
│ Tags: [VIP] [Contract] [Pricing]                        │
├─────────────────────────────────────────────────────────┤
│ Description:                                            │
│                                                          │
│ Had detailed discussion about Q4 contract renewal.      │
│ Key points:                                             │
│ • Interested in upgrading to Enterprise tier            │
│ • Needs custom onboarding for new team members          │
│ • Wants 10% discount for annual commitment              │
│ • Decision deadline: November 15                        │
│                                                          │
│ Next steps:                                             │
│ • Send updated proposal by October 28                   │
│ • Schedule follow-up call for November 1                │
│                                                          │
│ Attachments:                                            │
│ 📄 meeting-notes.pdf (124 KB)                           │
│                                                          │
├─────────────────────────────────────────────────────────┤
│ Comments (2)                                            │
│ Sarah L.: "Great progress! I'll prepare the proposal"   │
│ 2 hours ago                                             │
│                                                          │
│ [Add comment...]                                         │
├─────────────────────────────────────────────────────────┤
│ [Edit] [Delete] [Move to Thread...] [Create Task]      │
└─────────────────────────────────────────────────────────┘
```

#### Technical Implementation

**Data Model for Threads:**
```javascript
{
  id: "thread_abc123",
  tenantId: "tenant_xyz789",
  customerId: "cust_abc123",
  name: "Q4 Contract Renewal",
  description: "Annual contract renewal discussion",
  status: "active", // active, closed, archived
  createdAt: "2025-10-01T00:00:00Z",
  createdBy: "user_mike123",
  closedAt: null,
  eventCount: 12,
  lastActivityAt: "2025-10-24T15:30:00Z"
}
```

**Timeline Query:**
```python
def get_customer_timeline(tenant_id, customer_id, thread_id=None, 
                          event_types=None, start_date=None, 
                          end_date=None, limit=50):
    query = db.collection('logs') \
              .where('tenantId', '==', tenant_id) \
              .where('customerId', '==', customer_id) \
              .order_by('createdAt', 'desc') \
              .limit(limit)
    
    if thread_id:
        query = query.where('threadId', '==', thread_id)
    
    if event_types:
        query = query.where('type', 'in', event_types)
    
    # Similar filters for complaints, emails, etc.
    
    return query.stream()
```

**API Endpoints:**
```
GET /api/v1/customers/:id/timeline?thread=xxx&types=call,email&from=2025-10-01
GET /api/v1/customers/:id/threads
POST /api/v1/customers/:id/threads
PUT /api/v1/threads/:id
DELETE /api/v1/threads/:id
POST /api/v1/logs/:id/move-to-thread
```

#### Dependencies
- Customer management
- Logging system
- Complaint system
- Email integration

#### Risks & Mitigations
| Risk | Mitigation |
|------|------------|
| Performance with 100+ events | Implement pagination, virtual scrolling |
| Complex filtering slows queries | Proper indexing, cache frequently accessed data |
| Thread organization becomes confusing | Clear UI, limit to 10 active threads, archive old ones |
| Real-time updates cause UI jumps | Smooth animations, indicate new items above fold |

---

### 6.6 Feature: Advanced Search
**Priority**: P0 (Critical)  
**Epic**: Search & Discovery  
**Phase**: 1 (MVP)

#### Description
Powerful, fast search functionality across all CRM data (customers, logs, emails, complaints) with advanced filtering, fuzzy matching, and saved searches.

#### User Stories
1. **As a user**, I want to quickly find any customer by name, email, or company
2. **As a sales rep**, I want to search within customer notes for specific keywords
3. **As a support agent**, I want to find all complaints related to a specific issue
4. **As a manager**, I want to save common searches for quick access
5. **As a user**, I want search suggestions as I type

#### Functional Requirements

**FR-SEARCH-001: Global Search**
- Search bar always visible in header
- Search scope includes: Customers, Logs, Emails, Complaints, Tags
- Real-time search as user types (debounced 300ms)
- Show results in dropdown with categories
- Click result to navigate to detail page
- Keyboard navigation (arrow keys, enter)

**FR-SEARCH-002: Search Customers**
- Search fields: Company name, contact name, email, phone, tags
- Fuzzy matching for typos (e.g., "jhon" finds "John")
- Partial matching (e.g., "acme" finds "Acme Corp", "Acme Industries")
- Return up to 10 results instantly

**FR-SEARCH-003: Search Logs & Notes**
- Full-text search in log subject and description
- Search by log type, creator, date range
- Return matching logs with highlighted keywords
- Option to search within specific customer

**FR-SEARCH-004: Search Emails**
- Search email subject, body, sender, recipient
- Filter by date sent/received
- Search attachments (filename only)
- Link to original email in Gmail (if available)

**FR-SEARCH-005: Search Complaints**
- Search complaint title, description, ticket number
- Filter by status, severity, category
- Search by assigned team member
- Show SLA status in results

**FR-SEARCH-006: Advanced Search**
- Modal with detailed filters
- Boolean operators: AND, OR, NOT
- Field-specific search (e.g., email:john@acme.com)
- Date range pickers
- Multi-select filters (tags, types, users)
- Preview results count before executing

**FR-SEARCH-007: Saved Searches**
- Save frequently used search queries
- Name saved searches
- Quick access from dropdown
- Edit/delete saved searches
- Share saved searches with team (future)

**FR-SEARCH-008: Search Suggestions**
- Autocomplete based on recent searches
- Suggest customers based on partial input
- Suggest tags
- Show "Did you mean...?" for typos

**FR-SEARCH-009: Search History**
- Track last 10 searches per user
- Quick re-run previous search
- Clear search history option

#### Acceptance Criteria
- ✅ Global search returns results in < 1 second
- ✅ Fuzzy matching catches common typos (tested with 20 variations)
- ✅ Search works across 500+ customer records
- ✅ Advanced search supports all filter combinations
- ✅ Saved searches load instantly
- ✅ Search suggestions appear within 300ms
- ✅ Keyboard navigation works perfectly
- ✅ Search results highlight matching keywords
- ✅ No results state is clear and helpful

#### UI Mockup Description

**Global Search Bar:**
```
┌─────────────────────────────────────────────────────────┐
│ Header                                                   │
│ [🔍 Search customers, logs, emails...    ]  Advanced ▼  │
│                                                          │
│ ┌──────────── Search Results ──────────────┐           │
│ │ CUSTOMERS (3)                             │           │
│ │ 📄 Acme Corp - john@acme.com              │           │
│ │ 📄 Acme Industries - jane@acmei.com       │           │
│ │ 📄 Acme LLC - bob@acmellc.com             │           │
│ │                                            │           │
│ │ LOGS (5)                                   │           │
│ │ 📝 Discussed Q4 roadmap - Acme Corp       │           │
│ │ 📞 Follow-up call about pricing - ...     │           │
│ │                                            │           │
│ │ COMPLAINTS (1)                             │           │
│ │ 🔴 #1234 - Login issues - Acme Corp       │           │
│ │                                            │           │
│ │ [View all 9 results...]                    │           │
│ └────────────────────────────────────────────┘           │
└─────────────────────────────────────────────────────────┘
```

**Advanced Search Modal:**
```
┌─────────────────────────────────────────────────────────┐
│ Advanced Search                                    [×]  │
├─────────────────────────────────────────────────────────┤
│ Search in: [✓ Customers] [✓ Logs] [✓ Emails] [✓ Complaints] │
│                                                          │
│ Keywords: [____________________________]                 │
│                                                          │
│ ┌─ Customer Filters ────────────────────────────┐      │
│ │ Status:      [Active ▼]                       │      │
│ │ Assigned to: [All Users ▼]                    │      │
│ │ Tags:        [VIP] [×] [Tech] [×]             │      │
│ │ Created:     [2025-01-01] to [2025-10-24]     │      │
│ └───────────────────────────────────────────────┘      │
│                                                          │
│ ┌─ Log Filters ─────────────────────────────────┐      │
│ │ Type:        [All Types ▼]                     │      │
│ │ Creator:     [All Users ▼]                     │      │
│ │ Date range:  [Last 30 days ▼]                 │      │
│ └───────────────────────────────────────────────┘      │
│                                                          │
│ Results: ~45 matches                                    │
│                                                          │
│ Save this search: [My VIP customers]    [✓ Save]       │
│                                                          │
│         [Reset]  [Cancel]  [Search]                     │
└─────────────────────────────────────────────────────────┘
```

**Search Results Page:**
```
┌─────────────────────────────────────────────────────────┐
│ Search results for "acme pricing"              [Refine] │
├─────────────────────────────────────────────────────────┤
│ Showing 45 results                                      │
│                                                          │
│ [Customers] [Logs] [Emails] [Complaints] [All]          │
├─────────────────────────────────────────────────────────┤
│ 📄 Acme Corp                                            │
│    Contact: John Smith • john@acme.com                  │
│    Tags: VIP, Enterprise                                │
│    Last activity: 2 hours ago                           │
│    [View Customer]                                       │
│                                                          │
│ 📝 Discussed pricing options for Q4                     │
│    Customer: Acme Corp • Mike S. • 5 hours ago          │
│    "...discussed various pricing tiers and discount..."  │
│    [View Log]                                            │
│                                                          │
│ ✉ Re: Pricing proposal                                 │
│    From: john@acme.com • 1 day ago                      │
│    "Thanks for the detailed pricing breakdown. We..."    │
│    [View Email]                                          │
│                                                          │
│ ...more results...                                      │
│                                                          │
│         < Previous    Page 1 of 5    Next >             │
└─────────────────────────────────────────────────────────┘
```

#### Technical Implementation

**Search Architecture:**

For MVP, use Firestore's built-in text search with manual indexing:

```python
# Example: Search customers by name or email
def search_customers(tenant_id, query, limit=10):
    # Normalize query
    query_lower = query.lower()
    
    # Search by company name
    results_by_name = db.collection('customers') \
        .where('tenantId', '==', tenant_id) \
        .where('companyNameLower', '>=', query_lower) \
        .where('companyNameLower', '<=', query_lower + '\uf8ff') \
        .limit(limit) \
        .stream()
    
    # Search by email
    results_by_email = db.collection('customers') \
        .where('tenantId', '==', tenant_id) \
        .where('contactPerson.email', '>=', query_lower) \
        .where('contactPerson.email', '<=', query_lower + '\uf8ff') \
        .limit(limit) \
        .stream()
    
    # Merge and deduplicate results
    return merge_deduplicate(results_by_name, results_by_email)
```

**For better search (Phase 2), use Algolia or Elasticsearch:**

```python
# With Algolia
def search_with_algolia(tenant_id, query, filters=None):
    results = algolia_client.search({
        'query': query,
        'filters': f'tenantId:{tenant_id}',
        'hitsPerPage': 50,
        'typoTolerance': True,
        'attributesToHighlight': ['companyName', 'description']
    })
    return results
```

**Database Indexes:**
```
Customers:
  - Composite index: tenantId + companyNameLower (ascending)
  - Composite index: tenantId + email (ascending)

Logs:
  - Composite index: tenantId + subject (ascending)
  - Full-text index on description (if supported)

Complaints:
  - Composite index: tenantId + ticketNumber
  - Composite index: tenantId + title (ascending)
```

**API Endpoints:**
```
GET /api/v1/search?q=acme&scope=customers,logs&limit=10
GET /api/v1/search/advanced (with POST body for complex filters)
GET /api/v1/search/suggestions?q=acm
GET /api/v1/search/saved
POST /api/v1/search/saved
DELETE /api/v1/search/saved/:id
```

#### Dependencies
- All data models (Customers, Logs, Emails, Complaints)
- Database indexes configured
- Optional: Algolia or Elasticsearch for advanced search (Phase 2)

#### Risks & Mitigations
| Risk | Mitigation |
|------|------------|
| Firestore search limitations | Start simple, migrate to Algolia/Elasticsearch in Phase 2 |
| Slow search with large datasets | Proper indexing, limit results, pagination |
| Fuzzy matching inaccuracy | Use proven library (fuzzywuzzy), tune thresholds |
| Search query injection | Sanitize inputs, use parameterized queries |
| Expensive third-party search service | Start with free tier, optimize usage |

---

### 6.7 Feature: Email Integration (Gmail API via n8n)
**Priority**: P0 (Critical)  
**Epic**: Communication  
**Phase**: 1 (MVP)

#### Description
Seamless integration with Gmail for two-way email synchronization, automatic email-to-customer linking, and email management directly from the CRM.

#### User Stories
1. **As a user**, I want my Gmail emails automatically synced to CRM
2. **As a sales rep**, I want emails auto-linked to the right customer
3. **As a user**, I want to send emails from within the CRM
4. **As a manager**, I want to see all email communications with each customer
5. **As a user**, I want email templates for common responses

#### Functional Requirements

**FR-EMAIL-001: Gmail Authentication**
- OAuth 2.0 authentication with Gmail
- Request necessary scopes (read, send, modify)
- Store refresh tokens securely
- Handle token expiration and renewal

**FR-EMAIL-002: Email Sync (Inbound)**
- Sync emails from Gmail every 5 minutes
- Pull last 30 days of emails on initial sync
- Incremental sync for new emails
- Sync email metadata: sender, recipient, subject, date, thread
- Download email body (HTML and plain text)
- Download attachments (optional, configurable)

**FR-EMAIL-003: Auto-Linking to Customers**
- Match email address to customer contact email
- Match email domain to customer company domain
- Fuzzy matching for similar names/companies
- Manual linking if auto-link fails
- Option to unlink and relink

**FR-EMAIL-004: Email Display**
- Threaded conversation view
- Render HTML emails safely (sanitize)
- Display attachments with download links
- Show email labels/tags from Gmail
- Indicate read/unread status

**FR-EMAIL-005: Send Email from CRM**
- Compose new email
- Reply to existing email
- Forward email
- CC/BCC support
- Attachment upload
- Email sent via Gmail API (appears in Gmail Sent folder)

**FR-EMAIL-006: Email Templates**
- Create reusable email templates
- Template variables (customer name, company, user name)
- Category templates (sales, support, follow-up)
- Insert template into compose window
- Edit before sending

**FR-EMAIL-007: Email Categorization**
- Auto-categorize: Sales, Support, Complaint, General
- Use n8n workflow for categorization logic
- Manual recategorization allowed
- Display category badge on email

**FR-EMAIL-008: Email Notifications**
- Notify assigned user of new emails
- Option to disable notifications per user
- Digest mode: Daily summary of emails
- Mobile push notifications (future)

**FR-EMAIL-009: BCC to CRM**
- Provide unique BCC address per user (e.g., mike+crm@yourcrm.com)
- Emails BCC'd to this address auto-imported
- Useful for external email clients
- Auto-link based on To/From addresses

#### Acceptance Criteria
- ✅ Emails sync within 5 minutes of receipt in Gmail
- ✅ 90% of emails correctly auto-linked to customers
- ✅ Email threads properly grouped
- ✅ HTML emails render correctly and safely
- ✅ Attachments downloadable
- ✅ Sent emails appear in Gmail within 30 seconds
- ✅ Templates insert with variables replaced
- ✅ Email categorization 80% accurate

#### Technical Implementation

**n8n Workflow for Email Sync:**
```
Trigger: Gmail - Watch for new emails (every 5 minutes)
  ↓
Extract: Parse email data (from, to, subject, body, attachments)
  ↓
Function: Identify customer (lookup by email address)
  ↓
HTTP Request: Call CRM API to create email record
  ↓
Function: Categorize email (sales/support/complaint/general)
  ↓
HTTP Request: Update email with category
  ↓
IF: High priority email
  THEN: Telegram notification to assigned user
```

**Database Schema:**
```javascript
{
  id: "email_abc123",
  tenantId: "tenant_xyz789",
  customerId: "cust_abc123", // null if not linked
  gmailMessageId: "1829abc...",
  gmailThreadId: "thread_xyz...",
  from: {
    name: "John Smith",
    email: "john@acme.com"
  },
  to: ["mike@yourcrm.com"],
  cc: [],
  bcc: [],
  subject: "Re: Pricing proposal",
  bodyHtml: "<p>Thanks for the detailed...</p>",
  bodyPlainText: "Thanks for the detailed...",
  attachments: [
    {
      filename: "proposal.pdf",
      mimeType: "application/pdf",
      size: 245678,
      gmailAttachmentId: "att_123"
    }
  ],
  category: "sales",
  priority: "normal",
  labels: ["INBOX", "IMPORTANT"],
  isRead: true,
  linkedLogId: "log_abc123",
  receivedAt: "2025-10-24T10:00:00Z",
  syncedAt: "2025-10-24T10:03:00Z"
}
```

**API Endpoints:**
```
GET    /api/v1/emails?customerId=xxx&page=1
GET    /api/v1/emails/:id
POST   /api/v1/emails/send
POST   /api/v1/emails/:id/link (link to customer)
PUT    /api/v1/emails/:id/category
GET    /api/v1/emails/templates
POST   /api/v1/emails/templates
```

**Gmail API Integration:**
```python
from googleapiclient.discovery import build

def sync_gmail_emails(user_credentials, last_sync_timestamp):
    service = build('gmail', 'v1', credentials=user_credentials)
    
    # Query for emails since last sync
    query = f'after:{last_sync_timestamp}'
    results = service.users().messages().list(
        userId='me', q=query, maxResults=50
    ).execute()
    
    messages = results.get('messages', [])
    
    for msg in messages:
        # Get full message details
        message = service.users().messages().get(
            userId='me', id=msg['id'], format='full'
        ).execute()
        
        # Extract and process email data
        process_email(message)
```

#### Dependencies
- Gmail API credentials and OAuth setup
- n8n instance running
- Customer management system

#### Risks & Mitigations
| Risk | Mitigation |
|------|------------|
| Gmail API quota limits (1 billion quota units/day) | Batch requests, cache data, incremental sync only |
| Email matching failures | Provide manual linking UI, improve matching algorithm |
| Large attachments slow sync | Make attachment download optional, download on demand |
| OAuth token expiration | Automatic refresh token handling, re-auth flow |
| n8n downtime causes sync failures | Queue-based retry mechanism, error alerts |

---

### 6.8 Feature: Complaint Management System
**Priority**: P1 (High)  
**Epic**: Customer Support  
**Phase**: 1 (MVP)

#### Description
Dedicated system for logging, tracking, prioritizing, and resolving customer complaints with SLA tracking and customer communication.

#### User Stories
1. **As a support agent**, I want to quickly create complaint tickets from emails/calls
2. **As a support agent**, I want to track complaint resolution progress
3. **As a customer**, I want to receive updates on my complaint status
4. **As a manager**, I want to see overdue complaints highlighted
5. **As a user**, I want to escalate complex issues to external systems (Taiga)

#### Functional Requirements

**FR-COMP-001: Create Complaint**
- Form fields: Customer (required), Title, Description, Category, Severity
- Auto-generate unique ticket number (e.g., #CRM-1234)
- Attach files/screenshots
- Assign to user or auto-assign based on rules
- Set SLA deadlines automatically based on severity
- Create from email (one-click conversion)

**FR-COMP-002: Complaint Lifecycle**
States: New → Acknowledged → In Progress → Resolved → Closed
- **New**: Just created, not yet reviewed
- **Acknowledged**: Reviewed, working on it
- **In Progress**: Actively being worked on
- **Resolved**: Solution provided, awaiting customer confirmation
- **Closed**: Customer confirmed resolution
- Track timestamp for each status change

**FR-COMP-003: SLA Management**
- Define SLA rules by severity:
  - Critical: Response 1 hour, Resolution 4 hours
  - High: Response 4 hours, Resolution 24 hours
  - Medium: Response 24 hours, Resolution 72 hours
  - Low: Response 72 hours, Resolution 1 week
- Display SLA countdown timers
- Highlight overdue complaints (red)
- Send notifications 2 hours before SLA breach

**FR-COMP-004: Assignment & Escalation**
- Manual assignment to team member
- Auto-assignment rules:
  - Round-robin across support agents
  - Based on category (billing → finance team)
  - Based on customer (VIP → senior agent)
- Escalation: Reassign to manager if overdue
- Escalation to Taiga for technical issues (see Feature 6.9)

**FR-COMP-005: Internal Communication**
- Internal comments (not visible to customer)
- @mention team members in comments
- Attach files to comments
- Edit/delete own comments

**FR-COMP-006: Customer Communication**
- Send updates to customer via email
- Template messages: "We're working on it", "Resolution provided", etc.
- Customer can reply via email (threaded)
- Track all customer communication in timeline

**FR-COMP-007: Resolution & Closure**
- Add resolution notes
- Mark as resolved
- Request customer satisfaction rating (1-5 stars)
- Auto-close after 7 days if no customer response
- Reopen if customer replies after closure

**FR-COMP-008: Complaint Views**
- **Kanban Board**: Columns for each status, drag-and-drop
- **List View**: Sortable table with filters
- **My Complaints**: Assigned to current user
- **Overdue**: Breaching or breached SLA
- **All Complaints**: Manager view

**FR-COMP-009: Analytics**
- Average resolution time
- Complaints by category
- Complaints by severity
- Team member performance
- SLA adherence rate
- Customer satisfaction average

#### Acceptance Criteria
- ✅ Create complaint in < 1 minute
- ✅ Ticket number auto-generated and unique
- ✅ SLA deadlines calculated automatically
- ✅ Status changes trigger customer email notifications
- ✅ Overdue complaints highlighted in red
- ✅ Drag-and-drop on Kanban works smoothly
- ✅ Customer satisfaction rating collected for 70% of resolved complaints
- ✅ Internal comments clearly distinguished from customer updates

#### UI Mockup Description

**Complaint Kanban Board:**
```
┌─────────────────────────────────────────────────────────────────┐
│ Complaints  [+ New Complaint]  [My Complaints] [Overdue] [All]  │
├─────────────────────────────────────────────────────────────────┤
│ [🔍 Search...]  [Filter: All Categories ▼] [Sort: Due Date ▼]  │
├───────────┬──────────────┬──────────────┬──────────────┬────────┤
│   NEW (3) │ ACKNOWLEDGED │ IN PROGRESS  │  RESOLVED    │ CLOSED │
│           │      (2)     │      (5)     │      (2)     │  (12)  │
├───────────┼──────────────┼──────────────┼──────────────┼────────┤
│ ┌───────┐ │ ┌──────────┐ │ ┌──────────┐ │ ┌──────────┐ │        │
│ │#CRM-  │ │ │#CRM-1232 │ │ │#CRM-1230 │ │ │#CRM-1225 │ │  ...   │
│ │1234   │ │ │Login err │ │ │App crash │ │ │Billing   │ │        │
│ │       │ │ │🔴 Critical│ │ │🟡 Medium │ │ │🟢 Low    │ │        │
│ │Payment│ │ │Acme Corp │ │ │Beta Inc  │ │ │Gamma LLC │ │        │
│ │issue  │ │ │Sarah L.  │ │ │Mike S.   │ │ │John D.   │ │        │
│ │🔴 High│ │ │⏰ 45m left│ │ │⏰ 18h left│ │ │✓ Resolved│ │        │
│ │Acme C.│ │ │          │ │ │          │ │ │          │ │        │
│ │Unassg │ │ │          │ │ │          │ │ │          │ │        │
│ │⚠️ SLA! │ │ │          │ │ │          │ │ │          │ │        │
│ └───────┘ │ └──────────┘ │ └──────────┘ │ └──────────┘ │        │
│           │              │              │              │        │
│ ┌───────┐ │ ┌──────────┐ │ ┌──────────┐ │ ┌──────────┐ │        │
│ │...    │ │ │...       │ │ │...       │ │ │...       │ │        │
│ └───────┘ │ └──────────┘ │ └──────────┘ │ └──────────┘ │        │
└───────────┴──────────────┴──────────────┴──────────────┴────────┘
```

**Complaint Detail:**
```
┌─────────────────────────────────────────────────────────────────┐
│ [← Back] Complaint #CRM-1234  [Edit] [Close] [Escalate to Taiga]│
├─────────────────────────────────────────────────────────────────┤
│ Payment processing issue - ACME CORP                            │
│ Status: IN PROGRESS  •  Severity: 🔴 HIGH  •  Category: Billing │
│ Assigned to: Sarah L.  •  Created: Oct 24, 2025                 │
├──────────────────────────┬──────────────────────────────────────┤
│ Details                  │  Activity Timeline                   │
│ ─────────────           │  ─────────────────                   │
│                          │  [Customer Updates] [Internal Only]  │
│ Description:             │                                      │
│ Customer unable to       │  📧 Customer Update sent - 1h ago    │
│ process payment for      │  "We're working on fixing the issue" │
│ invoice #INV-9876.       │                                      │
│ Error: "Card declined"   │  💬 Internal Comment - 2h ago        │
│                          │  Sarah: "Contacted payment gateway"  │
│ SLA Status:              │                                      │
│ Response: ✓ Met (30m)    │  🔄 Status changed - 3h ago          │
│ Resolution: ⏰ 18h left  │  New → In Progress                   │
│                          │                                      │
│ Attachments:             │  📧 Complaint created - 3h ago       │
│ 📷 screenshot.png        │  Via email from john@acme.com        │
│ 📄 invoice.pdf           │                                      │
│                          │  [Load more...]                      │
│ Linked Issues:           │                                      │
│ 🔗 Taiga: None           │                                      │
│                          │                                      │
│ Customer Satisfaction:   │                                      │
│ Not yet resolved         │                                      │
│                          │                                      │
├──────────────────────────┴──────────────────────────────────────┤
│ Send Customer Update                                            │
│ ┌─────────────────────────────────────────────────────────────┐ │
│ │ [Use Template ▼]                                            │ │
│ │                                                              │ │
│ │ Hi John,                                                    │ │
│ │                                                              │ │
│ │ We've identified the issue...                               │ │
│ │                                                              │ │
│ └─────────────────────────────────────────────────────────────┘ │
│ [📎 Attach]                              [Send Update]          │
├─────────────────────────────────────────────────────────────────┤
│ Internal Comment                                                │
│ ┌─────────────────────────────────────────────────────────────┐ │
│ │ @Mike can you check payment gateway logs?                   │ │
│ └─────────────────────────────────────────────────────────────┘ │
│                                       [Add Comment]             │
└─────────────────────────────────────────────────────────────────┘
```

#### Technical Implementation

**Database Schema:**
```javascript
{
  id: "comp_abc123",
  ticketNumber: "CRM-1234",
  tenantId: "tenant_xyz789",
  customerId: "cust_abc123",
  title: "Payment processing issue",
  description: "Customer unable to process payment...",
  category: "billing",
  severity: "high",
  status: "in_progress",
  assignedTo: "user_sarah123",
  taigaIssueId: null,
  priority: 2, // 1=highest, 5=lowest
  sla: {
    responseDeadline: "2025-10-24T11:00:00Z",
    resolutionDeadline: "2025-10-25T10:00:00Z",
    responseMetAt: "2025-10-24T10:30:00Z",
    resolutionMetAt: null
  },
  timeline: [
    {
      timestamp: "2025-10-24T10:00:00Z",
      action: "created",
      userId: "user_sarah123",
      details: "Complaint created from email"
    },
    {
      timestamp: "2025-10-24T10:05:00Z",
      action: "status_changed",
      userId: "user_sarah123",
      details: "Changed from New to In Progress"
    }
  ],
  resolution: {
    notes: null,
    resolvedAt: null,
    resolvedBy: null,
    customerSatisfaction: null
  },
  internalComments: [
    {
      id: "comment_123",
      userId: "user_sarah123",
      comment: "@Mike can you check payment gateway logs?",
      mentions: ["user_mike123"],
      timestamp: "2025-10-24T11:00:00Z"
    }
  ],
  customerUpdates: [
    {
      id: "update_123",
      message: "We're working on fixing the issue...",
      timestamp: "2025-10-24T12:00:00Z",
      sentBy: "user_sarah123",
      emailSent: true
    }
  ],
  attachments: [
    {
      filename: "screenshot.png",
      url: "https://storage/.../screenshot.png",
      size: 125000,
      uploadedAt: "2025-10-24T10:02:00Z"
    }
  ],
  createdAt: "2025-10-24T10:00:00Z",
  createdBy: "user_sarah123",
  updatedAt: "2025-10-24T12:00:00Z"
}
```

**SLA Calculation Logic:**
```python
def calculate_sla_deadlines(severity, created_at):
    sla_rules = {
        'critical': {'response_hours': 1, 'resolution_hours': 4},
        'high': {'response_hours': 4, 'resolution_hours': 24},
        'medium': {'response_hours': 24, 'resolution_hours': 72},
        'low': {'response_hours': 72, 'resolution_hours': 168}
    }
    
    rules = sla_rules[severity]
    response_deadline = created_at + timedelta(hours=rules['response_hours'])
    resolution_deadline = created_at + timedelta(hours=rules['resolution_hours'])
    
    return {
        'responseDeadline': response_deadline,
        'resolutionDeadline': resolution_deadline
    }
```

**API Endpoints:**
```
GET    /api/v1/complaints?status=in_progress&assignedTo=me
GET    /api/v1/complaints/:id
POST   /api/v1/complaints
PUT    /api/v1/complaints/:id
PATCH  /api/v1/complaints/:id/status
POST   /api/v1/complaints/:id/comments
POST   /api/v1/complaints/:id/customer-updates
POST   /api/v1/complaints/:id/resolve
GET    /api/v1/complaints/overdue
GET    /api/v1/complaints/analytics
```

#### Dependencies
- Customer management
- Email integration (for notifications)
- User management (for assignment)
- Taiga integration (for escalation)

#### Risks & Mitigations
| Risk | Mitigation |
|------|------------|
| SLA deadlines not met | Proactive alerts, auto-escalation rules |
| Complaints lost/forgotten | Daily overdue report, dashboard widgets |
| Customer not satisfied with resolution | Follow-up process, satisfaction ratings |
| Performance with 100+ open complaints | Pagination, indexing, caching |

---

### 6.9 Feature: Third-Party Issue Tracking (Taiga Integration)
**Priority**: P1 (High)  
**Epic**: Integrations  
**Phase**: 2

#### Description
Integration with Taiga open-source project management platform for advanced issue tracking, especially for technical issues requiring development team involvement.

#### User Stories
1. **As a support agent**, I want to escalate technical complaints to the development team
2. **As a developer**, I want to work on issues in Taiga without switching tools
3. **As a support agent**, I want to see Taiga issue status updates in CRM
4. **As a manager**, I want visibility into all linked Taiga issues

#### Functional Requirements

**FR-TAIGA-001: Authentication**
- Store Taiga API credentials per tenant
- Support API key or username/password authentication
- Test connection before saving
- Settings page for Taiga configuration

**FR-TAIGA-002: Project Mapping**
- Map CRM tenant to Taiga project
- Select Taiga project from dropdown
- Support multiple Taiga projects per tenant
- Auto-map based on complaint category (optional)

**FR-TAIGA-003: Create Issue in Taiga**
- One-click "Escalate to Taiga" button on complaint
- Create Taiga user story or task
- Map complaint fields to Taiga fields:
  - Title → Subject
  - Description → Description
  - Severity → Priority
  - Customer name → Tags
- Attach files from complaint to Taiga issue
- Store Taiga issue ID in complaint record

**FR-TAIGA-004: Sync Taiga Status to CRM**
- Poll Taiga API every 15 minutes for status updates
- Update CRM complaint status when Taiga issue status changes
- Status mapping:
  - Taiga "New" → CRM "Acknowledged"
  - Taiga "In Progress" → CRM "In Progress"
  - Taiga "Ready for test" → CRM "In Progress"
  - Taiga "Done" → CRM "Resolved"
- Add timeline entry in CRM for each Taiga status change

**FR-TAIGA-005: Comment Sync (Optional)**
- Sync Taiga comments to CRM (as internal comments)
- Option to post CRM internal comments to Taiga
- Avoid infinite loops (track sync direction)

**FR-TAIGA-006: Display Taiga Link**
- Show Taiga issue link in complaint detail
- Display Taiga issue status badge
- One-click to open Taiga issue in new tab
- Show last sync timestamp

**FR-TAIGA-007: Webhook Support (Advanced)**
- Accept webhooks from Taiga for real-time updates
- Validate webhook signatures
- Update CRM immediately on Taiga changes
- Reduces sync delay from 15 minutes to seconds

#### Acceptance Criteria
- ✅ Taiga issue created within 30 seconds of escalation
- ✅ Issue includes all complaint details and attachments
- ✅ Status syncs every 15 minutes (or real-time with webhooks)
- ✅ Status mapping is accurate 100% of the time
- ✅ Taiga link opens correct issue
- ✅ No sync conflicts or data loss

#### Technical Implementation

**Taiga API Calls:**
```python
import requests

class TaigaClient:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }
    
    def create_user_story(self, project_id, subject, description, tags=[]):
        endpoint = f'{self.base_url}/api/v1/userstories'
        payload = {
            'project': project_id,
            'subject': subject,
            'description': description,
            'tags': tags
        }
        response = requests.post(endpoint, json=payload, headers=self.headers)
        return response.json()
    
    def get_user_story(self, story_id):
        endpoint = f'{self.base_url}/api/v1/userstories/{story_id}'
        response = requests.get(endpoint, headers=self.headers)
        return response.json()
    
    def add_comment(self, story_id, comment):
        endpoint = f'{self.base_url}/api/v1/userstories/{story_id}/comments'
        payload = {'comment': comment}
        response = requests.post(endpoint, json=payload, headers=self.headers)
        return response.json()
```

**Escalation Flow:**
```python
def escalate_complaint_to_taiga(complaint_id):
    # 1. Get complaint details
    complaint = get_complaint(complaint_id)
    
    # 2. Get Taiga config for tenant
    taiga_config = get_taiga_config(complaint['tenantId'])
    
    # 3. Create Taiga user story
    taiga_client = TaigaClient(taiga_config['baseUrl'], taiga_config['apiKey'])
    story = taiga_client.create_user_story(
        project_id=taiga_config['projectId'],
        subject=f"[CRM-{complaint['ticketNumber']}] {complaint['title']}",
        description=complaint['description'],
        tags=[complaint['category'], complaint['customerId']]
    )
    
    # 4. Update complaint with Taiga issue ID
    update_complaint(complaint_id, {
        'taigaIssueId': story['id'],
        'taigaIssueUrl': story['permalink']
    })
    
    # 5. Add timeline entry
    add_timeline_entry(complaint_id, {
        'action': 'escalated_to_taiga',
        'details': f"Created Taiga issue #{story['ref']}"
    })
    
    # 6. Notify team
    send_notification(complaint['assignedTo'], 
                      f"Complaint #{complaint['ticketNumber']} escalated to Taiga")
    
    return story
```

**Sync Status Job (runs every 15 minutes):**
```python
def sync_taiga_statuses():
    # Get all complaints with linked Taiga issues
    complaints_with_taiga = db.collection('complaints') \
        .where('taigaIssueId', '!=', None) \
        .where('status', 'in', ['acknowledged', 'in_progress']) \
        .stream()
    
    for complaint in complaints_with_taiga:
        complaint_data = complaint.to_dict()
        
        # Get Taiga issue status
        taiga_config = get_taiga_config(complaint_data['tenantId'])
        taiga_client = TaigaClient(taiga_config['baseUrl'], taiga_config['apiKey'])
        taiga_issue = taiga_client.get_user_story(complaint_data['taigaIssueId'])
        
        # Map Taiga status to CRM status
        crm_status = map_taiga_status_to_crm(taiga_issue['status_extra_info']['name'])
        
        # Update if status changed
        if crm_status != complaint_data['status']:
            update_complaint_status(complaint.id, crm_status)
            add_timeline_entry(complaint.id, {
                'action': 'taiga_status_updated',
                'details': f"Taiga issue moved to {taiga_issue['status_extra_info']['name']}"
            })
```

**Database Schema Addition:**
```javascript
// Add to Complaint schema
{
  taigaIssueId: 12345,
  taigaIssueRef: "US-42",
  taigaIssueUrl: "https://tree.taiga.io/project/myproject/us/42",
  taigaLastSyncedAt: "2025-10-24T15:00:00Z"
}

// Taiga Configuration (per tenant)
{
  tenantId: "tenant_xyz789",
  taigaBaseUrl: "https://api.taiga.io",
  taigaApiKey: "encrypted_api_key",
  taigaProjectId: 12345,
  taigaProjectName: "CRM Customer Issues",
  statusMappings: {
    "New": "acknowledged",
    "In progress": "in_progress",
    "Ready for test": "in_progress",
    "Done": "resolved"
  }
}
```

**API Endpoints:**
```
POST   /api/v1/complaints/:id/escalate-to-taiga
GET    /api/v1/taiga/config
PUT    /api/v1/taiga/config
POST   /api/v1/taiga/test-connection
POST   /api/v1/taiga/webhook (receive Taiga webhooks)
GET    /api/v1/taiga/projects (list available projects)
```

#### Dependencies
- Complaint management system
- Taiga instance (cloud or self-hosted)
- Background job scheduler (for sync)

#### Risks & Mitigations
| Risk | Mitigation |
|------|------------|
| Taiga API downtime | Queue failed requests, retry with exponential backoff |
| API rate limiting | Respect rate limits, batch requests |
| Status mapping confusion | Clear documentation, customizable mappings |
| Webhook security | Validate signatures, use HTTPS, IP whitelist |

---

### 6.10 Feature: Call Integration (VoIP)
**Priority**: P1 (High)  
**Epic**: Communication  
**Phase**: 3

#### Description
Enable users to make and receive calls directly from the CRM using VoIP integration, with automatic call logging and recording capabilities.

#### User Stories
1. **As a sales rep**, I want to click on a phone number to initiate a call
2. **As a user**, I want calls automatically logged in customer history
3. **As a manager**, I want to listen to call recordings for training
4. **As a user**, I want to take notes during the call

#### Functional Requirements

**FR-CALL-001: Click-to-Call**
- Click phone number anywhere in CRM to initiate call
- Works from customer list, customer detail, contact cards
- Display dialer interface (dialpad, mute, hold, hangup)
- Show call duration timer

**FR-CALL-002: VoIP Provider Integration**
- Integrate with Twilio or similar VoIP provider
- WebRTC for browser-based calls
- Native dialer integration for mobile app
- SIP trunk support for existing PBX systems

**FR-CALL-003: Incoming Calls**
- Pop-up notification when call received
- Display caller information (if matched to customer)
- Option to answer or decline
- Route to assigned user if customer has one

**FR-CALL-004: Call Controls**
- Mute/unmute microphone
- Hold/resume call
- Transfer call to another user
- Conference calling (3-way)
- Dialpad (for IVR navigation)

**FR-CALL-005: Automatic Call Logging**
- Create log entry automatically when call ends
- Capture: Customer, Duration, Direction (inbound/outbound)
- Pre-fill log form with call details
- Allow user to add notes before saving
- Option to disable auto-logging

**FR-CALL-006: Call Recording**
- Enable/disable recording per call
- Notify participants that call is recorded (legal requirement)
- Store recordings in Firebase Storage
- Link recording to call log
- Playback interface with transcript (future)

**FR-CALL-007: In-Call Notes**
- Notepad interface during call
- Real-time autosave
- Notes transferred to log entry
- Rich text formatting

**FR-CALL-008: Call History**
- View all calls for a customer
- Filter by direction, duration, outcome
- Search within call notes
- Export call reports

#### Acceptance Criteria
- ✅ Click-to-call initiates call within 3 seconds
- ✅ All calls automatically logged within 5 seconds of hangup
- ✅ Call quality is clear (minimal latency, no dropouts)
- ✅ Recordings playback correctly
- ✅ In-call notes saved reliably
- ✅ Works on web and mobile platforms

#### Technical Implementation

**Twilio Integration:**
```javascript
// Web: Using Twilio Client SDK
import { Device } from '@twilio/voice-sdk';

async function initiateCall(phoneNumber) {
  // Get Twilio token from backend
  const token = await fetch('/api/v1/calls/token').then(r => r.json());
  
  // Initialize Twilio Device
  const device = new Device(token);
  
  device.on('ready', () => {
    console.log('Device ready');
  });
  
  // Make call
  const call = await device.connect({
    params: {
      To: phoneNumber,
      customerId: currentCustomerId
    }
  });
  
  // Handle call events
  call.on('accept', () => {
    console.log('Call accepted');
    startCallTimer();
  });
  
  call.on('disconnect', () => {
    console.log('Call ended');
    stopCallTimer();
    promptForCallNotes();
  });
}
```

**Backend: Generate Twilio Token:**
```python
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import VoiceGrant

def generate_twilio_token(user_id):
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    api_key = os.getenv('TWILIO_API_KEY')
    api_secret = os.getenv('TWILIO_API_SECRET')
    
    # Create access token
    token = AccessToken(account_sid, api_key, api_secret, identity=user_id)
    
    # Create Voice grant
    voice_grant = VoiceGrant(
        outgoing_application_sid=os.getenv('TWILIO_TWIML_APP_SID'),
        incoming_allow=True
    )
    
    token.add_grant(voice_grant)
    
    return token.to_jwt()
```

**Auto-Create Call Log:**
```python
def on_call_completed(call_sid, customer_id, duration, recording_url=None):
    # Get call details from Twilio
    call = twilio_client.calls(call_sid).fetch()
    
    # Create log entry
    log_entry = {
        'tenantId': get_tenant_id(),
        'customerId': customer_id,
        'type': 'call',
        'subject': f"Call with {call.to}",
        'description': '',
        'callDetails': {
            'direction': call.direction,
            'duration': duration,
            'from': call.from_,
            'to': call.to,
            'status': call.status,
            'recordingUrl': recording_url
        },
        'createdAt': firestore.SERVER_TIMESTAMP,
        'createdBy': get_current_user_id()
    }
    
    db.collection('logs').add(log_entry)
```

**API Endpoints:**
```
GET    /api/v1/calls/token
POST   /api/v1/calls/initiate
POST   /api/v1/calls/webhook (Twilio status callbacks)
GET    /api/v1/calls/history?customerId=xxx
GET    /api/v1/calls/:id/recording
```

#### Dependencies
- Twilio account and phone numbers
- Customer management
- Logging system

#### Risks & Mitigations
| Risk | Mitigation |
|------|------------|
| Call quality issues | Use reliable VoIP provider, test thoroughly |
| High Twilio costs | Monitor usage, set budget alerts, optimize |
| Recording storage costs | Compress recordings, delete after 90 days |
| Legal compliance (recording consent) | Display clear notification, local laws research |

---

### 6.11 Feature: Conversational Interface (AI Chatbot)
**Priority**: P1 (High)  
**Epic**: AI & Automation  
**Phase**: 2-3

#### Description
Dual-purpose conversational interface: (1) Internal chatbot for CRM users to interact with the system using natural language, and (2) External customer-facing chatbot for support inquiries.

*(Due to length, providing summary)*

**Internal Chatbot Capabilities:**
- Natural language queries: "Show me VIP customers from last month"
- Quick actions: "Create a log for Acme Corp"
- Search: "Find customers in New York"
- Analytics: "How many complaints this week?"

**External Chatbot Capabilities:**
- Check order status
- Submit support requests
- Schedule appointments
- Get business hours/FAQs

**Technology**: OpenAI API or similar NLP engine, with intent recognition and entity extraction.

---

## 7. Data Models

### 7.1 Complete Entity Relationship Diagram

```
┌──────────┐       ┌──────────┐       ┌──────────┐
│  Tenant  │◄─────►│   User   │       │ Customer │
└──────────┘       └──────────┘       └──────────┘
     │                  │                    │
     │                  │                    │
     │                  ▼                    │
     │            ┌──────────┐               │
     └───────────►│   Log    │◄──────────────┘
                  └──────────┘
                        │
                        │
                  ┌──────────┐
                  │ Email    │
                  └──────────┘
                        │
                        │
                  ┌──────────┐       ┌──────────┐
                  │Complaint │◄─────►│  Taiga   │
                  └──────────┘       └──────────┘
                        │
                        │
                  ┌──────────┐
                  │   Call   │
                  └──────────┘
```

### 7.2 Core Entity Schemas

*(Schemas provided in detail in individual feature sections above)*

Key entities:
- Tenant
- User
- Customer
- Log Entry
- Email
- Complaint
- Call
- Thread
- Taiga Configuration

---

## 8. User Interface Specifications

### 8.1 Design System

**Color Palette:**
```
Primary Background:   #1a1a2e  (Dark navy)
Secondary Background: #16213e  (Darker blue)
Card Background:      #0f3460  (Deep blue)
Primary Accent:       #6C63FF  (Purple)
Secondary Accent:     #9F7AEA  (Light purple)
Success:              #10B981  (Green)
Warning:              #F59E0B  (Orange)
Error:                #EF4444  (Red)
Text Primary:         #F9FAFB  (Off-white)
Text Secondary:       #D1D5DB  (Gray)
Border:               #374151  (Dark gray)
```

**Typography:**
- **Headings**: Inter or Poppins (Bold)
- **Body**: Inter (Regular)
- **Monospace**: JetBrains Mono (for code, IDs)

**Spacing**: 8px base unit (8, 16, 24, 32, 48, 64, 96)

**Components**:
- Buttons: Rounded (8px), with hover states
- Cards: Rounded (12px), subtle shadow
- Inputs: Rounded (6px), focus ring in purple
- Modals: Centered, backdrop blur

### 8.2 Key Page Layouts

*(Mockups provided in feature sections above)*

Core pages:
1. **Dashboard**: Metrics, recent activity, quick actions
2. **Customer List**: Table/grid with filters
3. **Customer Detail**: Info + timeline + tabs
4. **Complaint Kanban**: Drag-and-drop board
5. **Complaint Detail**: Full complaint view with communication
6. **Search Results**: Categorized results
7. **Settings**: User profile, integrations, team management

### 8.3 Responsive Design

- **Desktop**: Full layout (1920x1080 optimal)
- **Tablet**: Condensed sidebar, adjusted grid (768x1024)
- **Mobile**: Bottom navigation, stacked layout (375x667)

---

## 9. Integration Requirements

### 9.1 Gmail API via n8n
*(Detailed in Feature 6.7)*

**Key Requirements:**
- OAuth 2.0 authentication
- Webhook-triggered workflows
- Email parsing and categorization
- Two-way sync (receive and send)

### 9.2 Telegram Bot
**Purpose:** Notifications and conversational interface

**Setup:**
- Create bot via BotFather
- Get bot token
- Set webhook to CRM backend

**Commands:**
- `/start` - Introduction
- `/status` - Show assigned complaints
- `/search [query]` - Search CRM
- `/help` - Command list

### 9.3 Taiga API
*(Detailed in Feature 6.9)*

**Key Requirements:**
- API key or OAuth authentication
- Create user stories/tasks
- Sync status bidirectionally
- Optional webhook for real-time updates

### 9.4 VoIP (Twilio)
*(Detailed in Feature 6.10)*

**Key Requirements:**
- Twilio account with phone number
- Voice SDK for web/mobile
- TwiML apps for call flow
- Recording and storage

---

## 10. Non-Functional Requirements

### 10.1 Performance

| Metric | Requirement | Measurement Method |
|--------|-------------|-------------------|
| **Page Load Time** | < 2 seconds | Lighthouse, Real User Monitoring |
| **API Response Time** | < 500ms (p95) | Application logs, APM tools |
| **Search Latency** | < 1 second | Custom benchmarks |
| **Email Sync Delay** | < 5 minutes | Monitoring dashboard |
| **Database Query Time** | < 200ms (p95) | Firebase performance monitoring |
| **Mobile App Launch** | < 3 seconds | Analytics |

### 10.2 Scalability

**Current Scale (MVP):**
- 5-15 concurrent users per tenant
- 5-10 active tenants
- 200-500 customers per tenant
- 100-300 logs/day per tenant

**Future Scale (12 months):**
- 50-100 concurrent users per tenant
- 50-100 active tenants
- 5,000-10,000 customers per tenant
- 1,000-5,000 logs/day per tenant

**Scaling Strategy:**
- Horizontal scaling of backend (containerized)
- Firebase automatic scaling
- CDN for static assets
- Database indexing and query optimization
- Caching layer (Redis) for frequently accessed data

### 10.3 Security

**Authentication & Authorization:**
- Firebase Auth with email/password
- JWT tokens for API access
- Session timeout: 24 hours
- Password requirements: min 8 chars, uppercase, lowercase, number
- Role-based access control (RBAC) enforced at API level

**Data Protection:**
- HTTPS/TLS 1.3 for all communications
- Data encrypted at rest (Firebase default AES-256)
- Encrypted backups
- Secure credential storage (environment variables, not in code)
- API keys rotated every 90 days

**Privacy & Compliance:**
- GDPR considerations (data export, deletion)
- Customer data isolated by tenant
- Audit logs for sensitive operations
- No third-party tracking scripts

**Application Security:**
- Input validation on all forms
- SQL injection prevention (using Firestore, not SQL)
- XSS prevention (sanitize HTML)
- CSRF protection
- Rate limiting on API endpoints
- Dependency vulnerability scanning

### 10.4 Availability & Reliability

**Uptime Target:** 99.0% (allows ~7 hours downtime/month)

**Backup Strategy:**
- Daily automated Firestore backups
- 30-day retention period
- Backup stored in separate region
- Monthly backup restore tests

**Disaster Recovery:**
- Recovery Time Objective (RTO): 4 hours
- Recovery Point Objective (RPO): 24 hours (daily backups)
- Documented recovery procedures
- Tested quarterly

**Monitoring & Alerting:**
- Uptime monitoring (Pingdom, UptimeRobot)
- Error tracking (Sentry)
- Performance monitoring (Firebase Performance)
- Log aggregation (Cloud Logging)
- Alerts for: API errors, high latency, failed backups, security events

### 10.5 Usability

**Accessibility:**
- WCAG 2.1 Level AA compliance (goal)
- Keyboard navigation support
- Screen reader compatibility
- High contrast mode option
- Minimum font size: 14px
- Color contrast ratio: 4.5:1 minimum

**User Experience:**
- Maximum 3 clicks to common actions
- Contextual help tooltips
- Undo functionality for destructive actions
- Confirmation dialogs for delete operations
- Loading indicators for all async operations
- Error messages clear and actionable

**Onboarding:**
- Interactive tutorial for first-time users
- Contextual tips on first use of features
- Documentation and help center
- Video tutorials (future)

### 10.6 Compatibility

**Web Browsers:**
- Chrome 90+ ✅
- Firefox 88+ ✅
- Safari 14+ ✅
- Edge 90+ ✅

**Mobile:**
- Android 8.0+ (Kotlin native app) ✅
- iOS: Responsive web (Safari) ✅

**Screen Resolutions:**
- Desktop: 1920x1080 (optimal), 1366x768 (minimum)
- Tablet: 768x1024
- Mobile: 375x667 (minimum)

### 10.7 Maintainability

**Code Quality:**
- Code reviews required for all changes
- Automated testing (unit, integration, E2E)
- Code coverage target: 70%+
- Linting and formatting enforced (ESLint, Black)

**Documentation:**
- API documentation (OpenAPI/Swagger)
- Code comments for complex logic
- README files in each module
- Architecture decision records (ADRs)

**Deployment:**
- CI/CD pipeline (GitHub Actions or similar)
- Automated testing in pipeline
- Staging environment for pre-production testing
- Blue-green deployment strategy
- Rollback capability

---

## 11. Development Roadmap

**🚀 TOTAL TIMELINE: 8 WEEKS (2 MONTHS)**

> **CRITICAL CONSTRAINT:** Aggressive 2-month delivery timeline requires focused scope, experienced team, and disciplined execution.

---

### Phase 1: Core MVP (Weeks 1-2) ⚡ CRITICAL

**Timeline**: 2 weeks  
**Team Required**: 2-3 full-stack developers working full-time  
**Goal**: Functional CRM with basic customer management

#### Week 1: Foundation (Days 1-7)

**Days 1-2: Setup & Authentication**
- [ ] Firebase project setup (Firestore, Auth, Hosting, Storage)
- [ ] Python backend skeleton (FastAPI with CORS)
- [ ] React frontend boilerplate (Vite + TailwindCSS + React Router)
- [ ] Basic authentication (email/password login/register)
- [ ] User model and session management
- [ ] Protected routes and auth middleware

**Days 3-5: Multi-Tenancy & Users**
- [ ] Multi-tenant architecture (tenantId in all collections)
- [ ] Firestore security rules (tenant isolation)
- [ ] User management (invite users via email)
- [ ] Basic roles (admin/user only for MVP)
- [ ] Basic admin dashboard
- [ ] User list and status management

**Days 6-7: Customer Management**
- [ ] Customer data model (name, email, phone, company, address, tags)
- [ ] Backend API: Customer CRUD endpoints
- [ ] Frontend: Customer list view (table with pagination)
- [ ] Frontend: Add/Edit customer modal/form
- [ ] Frontend: Customer detail page (basic info display)
- [ ] Basic validation (email format, required fields)

#### Week 2: Logging & Core Features (Days 8-14)

**Days 8-10: Logging System**
- [ ] Log data model (type, subject, description, attachments, tags)
- [ ] Backend API: Log CRUD endpoints
- [ ] Frontend: Create log modal (select customer, type, add description)
- [ ] Frontend: Log list view in customer detail page
- [ ] File upload for attachments (Firebase Storage, max 10MB)
- [ ] Support log types: Call, Email, Meeting, Note, Sample

**Days 11-12: Search & Timeline**
- [ ] Basic search API (customer name, email, company)
- [ ] Frontend: Global search bar with results dropdown
- [ ] Customer timeline view (chronological logs, newest first)
- [ ] Filter logs by type (checkboxes)
- [ ] Basic tags functionality (add/remove tags)
- [ ] Expandable log details in timeline

**Days 13-14: Polish & Deploy**
- [ ] Dark theme implementation (TailwindCSS dark classes)
- [ ] Purple accent colors (#6C63FF)
- [ ] Responsive design (mobile-friendly, breakpoints)
- [ ] Error handling and loading states (spinners, toasts)
- [ ] Form validation feedback
- [ ] Deploy to Firebase Hosting
- [ ] Basic smoke testing and critical bug fixes
- [ ] Demo preparation

#### Phase 1 Deliverables

✅ **Working Features:**
- User authentication (register, login, logout, session management)
- Multi-tenant architecture (complete data isolation)
- Customer management (create, read, update, delete, list with pagination)
- Activity logging (manual entry: calls, emails, notes, meetings, samples)
- Basic search (customers by name, email, company)
- Customer timeline (chronological view of all logs)
- File attachments (upload, download, preview images)
- Tags (add tags to customers and logs)
- Responsive web UI (desktop + tablet + mobile)
- Dark theme with purple accents

❌ **Not Included (Phase 2+):**
- Automatic email sync from Gmail
- Complaint management system
- Advanced search (fuzzy matching, filters, saved searches)
- Full role-based permissions (only basic admin/user distinction)
- Taiga integration
- VoIP calling
- AI chatbot
- Voice commands
- Mobile native app
- Email templates
- Interaction threads

#### Success Criteria
- [x] Demo-ready for stakeholders
- [x] 3-5 pilot users can use the system
- [x] Can create 10+ customers and 20+ logs without issues
- [x] Page load < 3 seconds
- [x] No critical bugs (blocking bugs fixed)
- [x] Deployed and accessible via public URL
- [x] Basic documentation (how to add customer, create log)

#### Risk Mitigation for 2-Week Sprint
- **Daily standups** to track progress and blockers
- **Ruthless scope control** - no feature creep
- **Pre-configured Firebase** project before Day 1
- **Code reviews kept minimal** - focus on shipping
- **Manual testing** only (no automated tests for MVP)
- **Technical debt tracked** for Phase 2 cleanup

---

### Phase 2: Communication & Search (Weeks 3-4)

**Timeline**: 2 weeks  
**Goal**: Email integration and advanced search

#### Week 3: Email Integration (Days 15-21)

**Days 15-17: Gmail API Setup**
- [ ] Gmail API credentials and OAuth 2.0 configuration
- [ ] n8n installation and workspace setup
- [ ] Email sync workflow (Gmail webhook → n8n → CRM API)
- [ ] Email data model (gmailMessageId, from, to, subject, body, attachments)
- [ ] Backend API: Email CRUD endpoints
- [ ] Handle email threading (Gmail threadId)

**Days 18-21: Email Features**
- [ ] Email list view (inbox-style with threading)
- [ ] Email detail view (render HTML safely with DOMPurify)
- [ ] Auto-link emails to customers (match by email address)
- [ ] Manual link/unlink emails to customers (dropdown selector)
- [ ] Send email from CRM (compose modal)
- [ ] Email templates (3-5 basic templates: intro, follow-up, thank you)
- [ ] BCC to CRM feature (unique email per user)

#### Week 4: Advanced Search & Timeline (Days 22-28)

**Days 22-24: Search Enhancement**
- [ ] Advanced search modal (multiple filter fields)
- [ ] Search across customers, logs, and emails
- [ ] Fuzzy matching implementation (simple Levenshtein distance)
- [ ] Date range filters (start date, end date)
- [ ] Tag filters (multi-select)
- [ ] Search suggestions/autocomplete (recent searches)
- [ ] Saved searches (store in user preferences)

**Days 25-28: Timeline & Threads**
- [ ] Thread data model (group related logs/emails)
- [ ] Create/manage threads (name, description)
- [ ] Assign logs to threads
- [ ] Enhanced timeline with thread filtering
- [ ] Email integration in unified timeline
- [ ] Quick actions on timeline items (reply, log call, etc.)
- [ ] Export timeline to PDF (basic formatting)
- [ ] Thread switching UI (tabs or dropdown)

#### Phase 2 Deliverables

✅ **Added Features:**
- Gmail email sync (automatic, every 5 minutes)
- Auto-link emails to customers (85%+ accuracy)
- Send emails from CRM (via Gmail API)
- Email templates (customizable)
- BCC to CRM (for external email clients)
- Advanced search (filters, fuzzy matching, date range)
- Saved searches
- Interaction threads (organize related activities)
- Enhanced unified timeline (emails + logs + threads)
- Export timeline to PDF

#### Success Criteria
- [x] Emails sync within 5 minutes of arrival
- [x] 85%+ emails auto-linked correctly
- [x] Search returns results in < 1 second
- [x] Users can send emails without leaving CRM
- [x] HTML emails render safely
- [x] Threads help organize complex customer interactions

---

### Phase 3: Support & Automation (Weeks 5-6)

**Timeline**: 2 weeks  
**Goal**: Complaint management and intelligent automation

#### Week 5: Complaint Management (Days 29-35)

**Days 29-31: Complaint System Foundation**
- [ ] Complaint data model (ticket#, status, severity, category, SLA)
- [ ] Backend API: Complaint CRUD endpoints
- [ ] Auto-generate ticket numbers (CRM-0001, CRM-0002, etc.)
- [ ] SLA calculation logic (by severity: Critical=4h, High=24h, Medium=72h, Low=1wk)
- [ ] Kanban board UI (columns for each status)
- [ ] Drag-and-drop between status columns (react-beautiful-dnd)

**Days 32-35: Complaint Features**
- [ ] Complaint detail page/modal (full information)
- [ ] Internal comments (team-only, with @mentions)
- [ ] Customer updates (send email to customer)
- [ ] Status workflow enforcement (New → Acknowledged → In Progress → Resolved → Closed)
- [ ] Attachment support (screenshots, documents)
- [ ] Overdue complaint alerts (red border, notification)
- [ ] Assignment rules (manual and auto-assign round-robin)
- [ ] Basic analytics widget (total, open, overdue counts)

#### Week 6: Automation & Integrations (Days 36-42)

**Days 36-38: Email Automation**
- [ ] n8n workflow: Auto-categorize incoming emails (sales/support/complaint/general)
- [ ] n8n workflow: Auto-assign emails to users (by category or round-robin)
- [ ] Priority detection (keywords: urgent, ASAP, critical)
- [ ] Automated email notifications (new assignment, mention, overdue)
- [ ] Email-to-complaint conversion (one-click)
- [ ] Complaint-to-email auto-responses (acknowledgment template)

**Days 39-42: Taiga Integration & Notifications**
- [ ] Taiga API authentication (API key storage)
- [ ] Taiga connection test in settings
- [ ] Create Taiga user story from complaint (one-click escalation)
- [ ] Sync Taiga status to CRM (polling every 15 minutes)
- [ ] Display Taiga issue link in complaint detail
- [ ] Telegram bot setup (BotFather)
- [ ] Telegram notifications (new complaint, overdue alert, mentions)
- [ ] Telegram commands (/status, /search, /help)

#### Phase 3 Deliverables

✅ **Added Features:**
- Complete complaint management system
- Kanban board for complaints (drag-and-drop)
- SLA tracking with visual countdown timers
- Overdue complaint alerts
- Internal comments with @mentions
- Customer update emails
- Automated email categorization (75%+ accuracy)
- Automated email assignment
- Priority detection
- Email-to-complaint conversion
- Taiga integration (escalation, status sync)
- Telegram bot (notifications and basic commands)

#### Success Criteria
- [x] Complaints tracked from creation to resolution
- [x] SLA breaches highlighted clearly
- [x] 75%+ email auto-categorization accuracy
- [x] Taiga issues created and synced successfully
- [x] Telegram notifications delivered within 1 minute
- [x] Users can manage 20+ concurrent complaints

---

### Phase 4: Advanced Features & Launch (Weeks 7-8)

**Timeline**: 2 weeks  
**Goal**: VoIP, polish, comprehensive testing, and production launch

#### Week 7: VoIP & Advanced Features (Days 43-49)

**Days 43-45: Call Integration**
- [ ] Twilio account setup and phone number purchase
- [ ] Twilio Voice SDK integration (web)
- [ ] Click-to-call implementation (WebRTC)
- [ ] Call interface (dialpad, mute, hold, hangup)
- [ ] Call logging (auto-create log on hangup)
- [ ] In-call notes (scratchpad that transfers to log)
- [ ] Call history view (per customer)
- [ ] Call recording (enable/disable, legal notice)
- [ ] Recording playback interface

**Days 46-49: Polish & Advanced Features**
- [ ] Full role-based access control (6 roles: Super Admin, Tenant Admin, Manager, Sales Rep, Support Agent, Viewer)
- [ ] Permissions matrix implementation (CRUD permissions per role)
- [ ] User permissions management UI (assign roles, custom permissions)
- [ ] Analytics dashboard (KPI widgets: customers, logs, complaints, emails)
- [ ] Charts (complaint trends, resolution time, email volume)
- [ ] Export reports (PDF, CSV for customers and complaints)
- [ ] Bulk operations (import customers via CSV, bulk delete)
- [ ] Activity audit log (track all create/update/delete actions)

#### Week 8: Testing & Launch (Days 50-56)

**Days 50-52: Comprehensive Testing**
- [ ] Feature testing checklist (all features, all roles)
- [ ] Cross-browser testing (Chrome, Firefox, Safari, Edge)
- [ ] Mobile responsive testing (iOS Safari, Android Chrome)
- [ ] Security testing (tenant isolation, XSS, CSRF, injection)
- [ ] Performance testing (page load, API response times)
- [ ] Load testing (simulate 50 concurrent users with Artillery or k6)
- [ ] Bug triage and fixes (critical and high-priority only)

**Days 53-56: Launch Preparation & Go-Live**
- [ ] Production environment setup (separate from dev/staging)
- [ ] Environment variables and secrets management
- [ ] Backup configuration (daily automated backups to separate region)
- [ ] Disaster recovery plan documented
- [ ] Monitoring setup (Sentry for errors, UptimeRobot for availability)
- [ ] Performance monitoring (Firebase Performance, custom metrics)
- [ ] User documentation (help center articles, screenshots)
- [ ] Video tutorials (3-5 short videos: getting started, key features)
- [ ] Onboarding tutorial (in-app guided tour)
- [ ] Final deployment to production
- [ ] Smoke testing in production
- [ ] **🚀 LAUNCH!**
- [ ] User onboarding (invite first 20 users)
- [ ] Feedback collection setup (in-app feedback widget)

#### Phase 4 Deliverables

✅ **Added Features:**
- VoIP call integration (click-to-call from web)
- Call logging and recording
- In-call notes
- Full RBAC system (6 roles with granular permissions)
- User permissions management
- Analytics dashboard (metrics and charts)
- Export reports (PDF, CSV)
- Bulk operations (import, delete)
- Activity audit log
- Production monitoring and alerts
- User documentation and tutorials
- Onboarding experience

✅ **Production Ready:**
- Deployed to production environment
- Monitoring and alerting active
- Backup and disaster recovery configured
- Security hardened
- Performance optimized
- User documentation complete
- Support system in place
- Ready for real users at scale

#### Success Criteria
- [x] All P0 and P1 features working
- [x] Zero critical bugs, < 5 high-priority bugs
- [x] Page load < 2 seconds (95th percentile)
- [x] API response < 500ms (95th percentile)
- [x] 99% uptime target configured
- [x] 20+ users onboarded and actively using
- [x] Positive user feedback (NPS 40+)
- [x] All performance metrics met
- [x] Security audit passed

---

## 📊 8-Week Timeline Summary

| Week | Phase | Focus | Key Deliverables | Team Size |
|------|-------|-------|------------------|-----------|
| **1-2** | Phase 1 | Core MVP | Auth, Multi-tenancy, Customers, Logs, Basic UI | 2-3 devs |
| **3-4** | Phase 2 | Communication | Email sync, Send emails, Advanced search, Threads | 2-3 devs |
| **5-6** | Phase 3 | Support & Automation | Complaints, SLA, Taiga, Email automation, Telegram | 2-4 devs |
| **7-8** | Phase 4 | Advanced & Launch | VoIP, RBAC, Analytics, Testing, Production launch | 3-4 devs |

**Total Effort:** ~200-240 developer-days (2-3 devs × 8 weeks × 5 days)

---

## 🎯 Feature Priority Matrix (8-Week Delivery)

### P0 - Must-Have (Weeks 1-2)
- ✅ Authentication & Multi-tenancy
- ✅ Customer CRUD
- ✅ Logging system (manual)
- ✅ Basic search
- ✅ Customer timeline
- ✅ File attachments

### P1 - Should-Have (Weeks 3-4)
- ✅ Email integration (Gmail sync)
- ✅ Send emails from CRM
- ✅ Email templates
- ✅ Advanced search (filters, fuzzy)
- ✅ Interaction threads

### P1 - Should-Have (Weeks 5-6)
- ✅ Complaint management
- ✅ SLA tracking
- ✅ Email automation
- ✅ Taiga integration
- ✅ Telegram notifications

### P1 - Should-Have (Weeks 7-8)
- ✅ VoIP calling (basic)
- ✅ Full RBAC
- ✅ Analytics dashboard
- ✅ Audit logs

### P2 - Nice-to-Have (Post-Launch / Future)
- ❌ AI Chatbot (conversational interface)
- ❌ Voice commands (speech-to-text)
- ❌ Android mobile app (Kotlin)
- ❌ iOS app
- ❌ WhatsApp integration
- ❌ Slack integration
- ❌ Multi-language support
- ❌ Advanced ML/AI features (sentiment analysis, churn prediction)
- ❌ Custom workflow builder
- ❌ Payment gateway integration
- ❌ Document management / e-signatures

---

## ⚠️ Critical Success Factors for 8-Week Delivery

### Team Requirements
✅ **2-3 experienced full-stack developers** (React + Python + Firebase)  
✅ **Full-time commitment** (no other projects)  
✅ **Minimal meetings** (daily 15-min standup only)  
✅ **Pre-existing expertise** (no learning curve time)

### Process Requirements
✅ **Ruthless scope control** - NO feature additions during 8 weeks  
✅ **Daily progress tracking** - Burndown chart, blockers resolved immediately  
✅ **Technical debt accepted** - Clean up in maintenance phase  
✅ **Manual testing only** - Automated tests post-launch  
✅ **Code reviews lightweight** - Async, < 30 min turnaround  

### Technical Requirements
✅ **Firebase project pre-configured** before Day 1  
✅ **Gmail API credentials ready** before Week 3  
✅ **Twilio account setup** before Week 7  
✅ **n8n instance running** before Week 3  
✅ **Development environments ready** (local + staging)

### Risk Mitigation
✅ **Buffer time built in** - 1-2 days per phase for slippage  
✅ **Parallel work streams** - Frontend/backend developed simultaneously  
✅ **Feature flags** - Deploy incomplete features hidden  
✅ **Rollback plan** - Can revert to previous stable version  
✅ **Daily backups** - Starting Week 1  

---

## 📅 Daily Standup Format (15 minutes)

**Each developer answers:**
1. What did I complete yesterday?
2. What will I complete today?
3. Any blockers?

**Track:**
- Features completed (checkboxes in roadmap)
- Current sprint velocity
- Risk items (behind schedule, new blockers)

**Action:**
- Resolve blockers immediately
- Re-prioritize if needed
- Celebrate wins!

---

## 🚨 Red Flags to Watch

| Red Flag | Action |
|----------|--------|
| **> 2 days behind schedule** | Cut scope, move features to next phase |
| **Critical bugs piling up** | Stop new features, fix bugs first |
| **Team member unavailable** | Immediate backup plan, reassign work |
| **Integration not working** | Escalate immediately, find alternative |
| **Performance issues early** | Address immediately, don't defer |

---

## 🎉 Launch Checklist (Day 56)

- [ ] All P0 and P1 features working
- [ ] Production environment deployed
- [ ] Monitoring and alerts configured
- [ ] Backups running daily
- [ ] Security review completed
- [ ] Performance benchmarks met
- [ ] User documentation published
- [ ] Support email/system ready
- [ ] 20+ users invited and onboarded
- [ ] Feedback mechanism in place
- [ ] Celebration planned! 🍾

---

## 12. Risks & Mitigations

### 12.1 Technical Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| **Firebase costs exceed budget** | Medium | High | Monitor usage closely, implement pagination, optimize queries, set budget alerts |
| **Gmail API quota limits** | Medium | High | Implement rate limiting, use batch requests, queue processing, consider incremental sync |
| **VoIP integration complexity** | High | Medium | Start with simpler solution (Twilio), detailed integration planning, allocate extra time |
| **Multi-tenancy data leakage** | Low | Critical | Rigorous testing, security audit, tenant filters on all queries, Firestore security rules |
| **NLP/Chatbot accuracy issues** | High | Medium | Start with rule-based, gradually add ML, user feedback loop, set realistic expectations |
| **Performance degradation at scale** | Medium | High | Load testing, proper indexing, caching strategy, horizontal scaling plan |
| **Third-party service downtime** | Medium | Medium | Graceful degradation, retry mechanisms, queue-based processing, status page |

### 12.2 Operational Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| **Data loss** | Low | Critical | Daily backups, redundancy, disaster recovery plan, quarterly restore tests |
| **Service downtime** | Medium | High | Health monitoring, alerts, rollback procedures, staging environment, blue-green deployment |
| **Security breach** | Low | Critical | Regular security audits, encryption, access controls, vulnerability scanning, incident response plan |
| **User adoption failure** | Medium | High | User research, onboarding program, training materials, feedback loops, iterative improvements |
| **Key personnel unavailable** | Medium | Medium | Documentation, code reviews, knowledge sharing, backup resources |

### 12.3 Business Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| **Competitors launch similar product** | High | Medium | Focus on unique value props, build moat (integrations, data), rapid iteration |
| **Market demand lower than expected** | Medium | High | Validate with pilot customers, flexible pricing, expand target market |
| **Integration partner changes API** | Medium | Medium | Monitor partner announcements, abstract integrations, have fallback options |

---

## 13. Future Enhancements

### 13.1 Post-MVP Features (Phase 5+)

**Messaging Integrations:**
- WhatsApp Business API integration
- Slack integration for team notifications
- SMS integration for customer communication

**Advanced AI/ML:**
- Predictive analytics (customer churn, upsell opportunities)
- Sentiment analysis on customer communications
- Smart suggestions (next best action)
- Anomaly detection (unusual customer behavior)

**Mobile:**
- iOS native app (Swift)
- Offline mode with sync
- Push notifications

**Workflow Automation:**
- Visual workflow builder (no-code)
- Trigger-action automation rules
- Scheduled tasks and reminders

**Advanced Features:**
- Calendar integration (Google Calendar, Outlook)
- Payment gateway integration (Stripe)
- Contract/document management
- E-signature integration (DocuSign)
- Social media monitoring
- Advanced BI dashboard with custom reports
- Multi-language support
- White-label option for resellers

### 13.2 Technical Improvements

- Migrate search to Algolia/Elasticsearch for better performance
- Implement GraphQL API for flexible data fetching
- Add WebSocket support for real-time collaboration
- Implement service mesh for microservices architecture (if needed)
- Add comprehensive E2E testing suite
- Performance optimization (lazy loading, code splitting)

---

## 14. Appendix

### 14.1 Glossary

| Term | Definition |
|------|------------|
| **API** | Application Programming Interface - allows software to communicate |
| **CRM** | Customer Relationship Management |
| **Firestore** | Google's NoSQL cloud database |
| **JWT** | JSON Web Token - used for authentication |
| **MVP** | Minimum Viable Product |
| **NLP** | Natural Language Processing |
| **OAuth** | Open Authorization standard for access delegation |
| **RBAC** | Role-Based Access Control |
| **SLA** | Service Level Agreement |
| **SMB** | Small and Medium Business |
| **VoIP** | Voice over Internet Protocol |
| **Webhook** | HTTP callback triggered by events |

### 14.2 References

**Documentation:**
- Firebase: https://firebase.google.com/docs
- Gmail API: https://developers.google.com/gmail/api
- Taiga API: https://docs.taiga.io/api.html
- Twilio Voice API: https://www.twilio.com/docs/voice
- n8n: https://docs.n8n.io/
- Telegram Bot API: https://core.telegram.org/bots/api

**Design Resources:**
- TailwindCSS: https://tailwindcss.com/docs
- Material Design: https://material.io/
- WCAG Guidelines: https://www.w3.org/WAI/WCAG21/quickref/

### 14.3 Assumptions

1. **Access to Services:** You have access to required APIs (Gmail, Taiga, VoIP provider)
2. **Firebase Tier:** Free tier sufficient for initial development, paid tier for production
3. **User Devices:** Users have modern browsers and devices (last 2 years)
4. **Internet Connectivity:** Internet connection required (no offline mode in MVP)
5. **Language:** English language only in MVP
6. **Email Provider:** Gmail is primary email provider (Outlook/others in future)
7. **Technical Expertise:** Development team familiar with React, Python, Firebase
8. **Development Time:** Realistic timeline assumes dedicated full-time team
9. **User Training:** Users receive basic training/onboarding
10. **Legal Compliance:** Call recording and data storage comply with local laws (customer responsibility)

### 14.4 Open Questions

1. **VoIP Provider:** Which VoIP provider to use? (Twilio, Vonage, custom)
2. **NLP Engine:** Build custom or use OpenAI API/similar?
3. **Hosting:** Firebase only or hybrid with VPS for backend?
4. **Pricing Model:** Subscription tiers and pricing?
5. **Email Limits:** Gmail API quota sufficient for all customers?
6. **Recording Storage:** Keep call recordings indefinitely or purge after X days?
7. **Mobile Priority:** Android first or develop both platforms simultaneously?
8. **Taiga Self-Hosted:** Support self-hosted Taiga or cloud only?

### 14.5 Approval & Sign-off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| **Product Owner** | _______________ | _______________ | __________ |
| **Engineering Lead** | _______________ | _______________ | __________ |
| **Design Lead** | _______________ | _______________ | __________ |
| **QA Lead** | _______________ | _______________ | __________ |
| **Business Stakeholder** | _______________ | _______________ | __________ |

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-10-24 | AI Assistant | Initial PRD creation - comprehensive document |

---

**END OF PRODUCT REQUIREMENTS DOCUMENT**

---

### Next Steps

1. **Review & Approve:** Stakeholders review and provide feedback
2. **Technical Deep Dive:** Engineering team validates technical approach
3. **Design Kickoff:** Design team creates detailed mockups and prototypes
4. **Sprint Planning:** Break down Phase 1 into 2-week sprints
5. **Environment Setup:** Configure Firebase, Gmail API, development environments
6. **Development Begins:** Start with authentication and multi-tenancy (Week 1-2)

**Questions or Need Clarification?** Contact the Product Team.

