# CRM Database Schema - Firebase Firestore

## Overview

This document outlines the complete database schema for the CRM system using Firebase Firestore (NoSQL). The schema is designed for multi-tenancy, scalability, and efficient querying.

---

## Database Architecture Principles

### 1. Multi-Tenancy Strategy
- **Tenant Isolation**: All documents include `tenantId` field for data segregation
- **Security Rules**: Firestore rules enforce tenant-level access control
- **Scalability**: Each tenant's data is logically separated but physically in same collections

### 2. Data Modeling Approach
- **Denormalization**: Duplicate data where needed for query performance
- **Subcollections**: Used for 1-to-many relationships (e.g., customer → logs)
- **References**: Use document references for many-to-many relationships
- **Composite Indexes**: Required for complex queries (defined below)

### 3. Naming Conventions
- Collections: plural, lowercase (e.g., `customers`, `users`)
- Fields: camelCase (e.g., `firstName`, `createdAt`)
- IDs: Auto-generated Firestore IDs or custom format (e.g., `TICKET-20251022-001`)

---

## Collections Structure

```
firestore (root)
│
├── tenants/
│   └── {tenantId}/
│       ├── (document fields)
│       └── settings/ (subcollection)
│
├── users/
│   └── {userId}/
│       ├── (document fields)
│       └── activity_logs/ (subcollection)
│
├── customers/
│   └── {customerId}/
│       ├── (document fields)
│       ├── logs/ (subcollection)
│       ├── threads/ (subcollection)
│       ├── complaints/ (subcollection)
│       └── files/ (subcollection)
│
├── complaints/
│   └── {complaintId}/
│       ├── (document fields)
│       ├── timeline/ (subcollection)
│       ├── comments/ (subcollection)
│       └── attachments/ (subcollection)
│
├── logs/
│   └── {logId}/
│       ├── (document fields)
│       └── attachments/ (subcollection)
│
├── emails/
│   └── {emailId}/
│       ├── (document fields)
│       └── thread/ (subcollection)
│
├── calls/
│   └── {callId}/
│       └── (document fields)
│
├── conversations/
│   └── {conversationId}/
│       ├── (document fields)
│       └── messages/ (subcollection)
│
├── automation_rules/
│   └── {ruleId}/
│       └── (document fields)
│
├── taiga_integrations/
│   └── {integrationId}/
│       └── (document fields)
│
├── notifications/
│   └── {notificationId}/
│       └── (document fields)
│
├── audit_logs/
│   └── {auditId}/
│       └── (document fields)
│
└── system_config/
    └── {configKey}/
        └── (document fields)
```

---

## Detailed Collection Schemas

### 1. `tenants` Collection

**Path**: `/tenants/{tenantId}`

**Purpose**: Store tenant/organization information for multi-tenancy

```javascript
{
  // Document ID: auto-generated or custom (e.g., "acme-corp")
  id: string,
  
  // Basic Information
  companyName: string,                    // "Acme Corporation"
  subdomain: string,                       // "acme" (for acme.yourcrm.com)
  
  // Branding
  branding: {
    logo: string,                          // URL to logo image
    primaryColor: string,                  // "#6C63FF"
    secondaryColor: string,                // "#9F7AEA"
    favicon: string                        // URL to favicon
  },
  
  // Subscription
  subscription: {
    plan: string,                          // "free", "starter", "professional", "enterprise"
    status: string,                        // "active", "suspended", "cancelled", "trial"
    startDate: timestamp,
    expiryDate: timestamp,
    billingEmail: string,
    maxUsers: number,                      // License limit
    maxCustomers: number,
    features: [string]                     // ["email_integration", "voice_commands", "taiga"]
  },
  
  // Contact Info
  adminUserId: string,                     // Reference to users collection
  contactEmail: string,
  contactPhone: string,
  
  // Address
  address: {
    street: string,
    city: string,
    state: string,
    zipCode: string,
    country: string
  },
  
  // Settings
  settings: {
    timezone: string,                      // "America/New_York"
    dateFormat: string,                    // "MM/DD/YYYY"
    timeFormat: string,                    // "12h" or "24h"
    currency: string,                      // "USD"
    language: string,                      // "en"
    
    // Feature toggles
    features: {
      emailIntegration: boolean,
      voiceCommands: boolean,
      taigaIntegration: boolean,
      callRecording: boolean,
      aiChatbot: boolean
    },
    
    // Notification preferences
    notifications: {
      email: boolean,
      telegram: boolean,
      inApp: boolean
    }
  },
  
  // Usage Stats (for billing/analytics)
  usage: {
    activeUsers: number,
    totalCustomers: number,
    storageUsedMB: number,
    apiCallsThisMonth: number
  },
  
  // Metadata
  status: string,                          // "active", "suspended", "deleted"
  createdAt: timestamp,
  updatedAt: timestamp,
  createdBy: string                        // User ID
}
```

**Subcollection**: `/tenants/{tenantId}/settings/{settingKey}`
- Custom settings per tenant
- API keys (encrypted)
- Integration credentials

**Indexes Required**:
- `subdomain` (unique)
- `status` + `subscription.status`
- `createdAt`

---

### 2. `users` Collection

**Path**: `/users/{userId}`

**Purpose**: Store user accounts (team members)

```javascript
{
  // Document ID: Firebase Auth UID
  id: string,
  
  // Tenant Association
  tenantId: string,                        // Reference to tenants collection
  
  // Basic Info
  email: string,                           // Unique, from Firebase Auth
  displayName: string,                     // "John Doe"
  firstName: string,
  lastName: string,
  phone: string,
  avatar: string,                          // URL to profile image
  
  // Role & Permissions
  role: string,                            // "super_admin", "tenant_admin", "manager", "sales_rep", "support_agent", "viewer"
  permissions: [string],                   // ["customers.read", "customers.write", "complaints.manage"]
  department: string,                      // "Sales", "Support", "Management"
  
  // Authentication
  authProvider: string,                    // "email", "google", "microsoft"
  lastLogin: timestamp,
  lastLoginIp: string,
  passwordChangedAt: timestamp,
  
  // Status
  status: string,                          // "active", "inactive", "suspended"
  isEmailVerified: boolean,
  
  // Preferences
  preferences: {
    theme: string,                         // "dark", "light"
    language: string,                      // "en"
    timezone: string,
    
    // Notification settings
    notifications: {
      email: {
        enabled: boolean,
        newComplaint: boolean,
        assignedTask: boolean,
        mentions: boolean,
        dailyDigest: boolean
      },
      telegram: {
        enabled: boolean,
        chatId: string,                    // Telegram chat ID
        newComplaint: boolean,
        urgentOnly: boolean
      },
      inApp: {
        enabled: boolean,
        sound: boolean,
        desktop: boolean
      }
    },
    
    // UI preferences
    ui: {
      sidebarCollapsed: boolean,
      defaultView: string,                 // "list", "grid", "kanban"
      itemsPerPage: number
    }
  },
  
  // Work Info
  workInfo: {
    title: string,                         // "Sales Manager"
    hireDate: timestamp,
    managerId: string,                     // Reference to another user
    teamMembers: [string]                  // Array of user IDs (if manager)
  },
  
  // Stats
  stats: {
    totalCustomers: number,
    activeComplaints: number,
    resolvedComplaints: number,
    totalCalls: number,
    totalEmails: number
  },
  
  // Metadata
  createdAt: timestamp,
  updatedAt: timestamp,
  createdBy: string,
  lastModifiedBy: string,
  
  // Soft delete
  deletedAt: timestamp | null,
  deletedBy: string | null
}
```

**Subcollection**: `/users/{userId}/activity_logs/{activityId}`
- Track user actions for audit trail
- Login history
- Important changes made

**Indexes Required**:
- `tenantId` + `status`
- `tenantId` + `role`
- `email` (unique)
- `lastLogin`

---

### 3. `customers` Collection

**Path**: `/customers/{customerId}`

**Purpose**: Store customer/client information

```javascript
{
  // Document ID: auto-generated
  id: string,
  
  // Tenant Association
  tenantId: string,
  
  // Company Information
  companyName: string,                     // "XYZ Industries"
  industry: string,                        // "Manufacturing", "Retail", etc.
  companySize: string,                     // "1-10", "11-50", "51-200", etc.
  website: string,
  
  // Primary Contact
  primaryContact: {
    firstName: string,
    lastName: string,
    fullName: string,                      // Denormalized for search
    email: string,
    phone: string,
    mobile: string,
    title: string,                         // "CEO", "Purchasing Manager"
    department: string
  },
  
  // Additional Contacts
  contacts: [{
    id: string,                            // Unique ID for this contact
    firstName: string,
    lastName: string,
    fullName: string,
    email: string,
    phone: string,
    mobile: string,
    title: string,
    department: string,
    isPrimary: boolean,
    notes: string
  }],
  
  // Address
  address: {
    street: string,
    street2: string,
    city: string,
    state: string,
    zipCode: string,
    country: string,
    
    // Shipping address if different
    shippingAddress: {
      street: string,
      city: string,
      state: string,
      zipCode: string,
      country: string
    }
  },
  
  // Business Details
  businessDetails: {
    taxId: string,
    vatNumber: string,
    registrationNumber: string,
    yearEstablished: number
  },
  
  // CRM Status
  status: string,                          // "lead", "prospect", "active", "inactive", "churned"
  stage: string,                           // "new", "qualified", "proposal", "negotiation", "closed-won", "closed-lost"
  source: string,                          // "website", "referral", "cold-call", "trade-show"
  priority: string,                        // "low", "medium", "high", "vip"
  
  // Assignment
  assignedTo: string,                      // User ID (primary account owner)
  assignedTeam: [string],                  // Array of user IDs (supporting team)
  
  // Financial
  financial: {
    currency: string,                      // "USD"
    lifetimeValue: number,
    totalRevenue: number,
    averageOrderValue: number,
    creditLimit: number,
    paymentTerms: string,                  // "Net 30", "Due on Receipt"
    lastPurchaseDate: timestamp,
    lastPurchaseAmount: number
  },
  
  // Tags & Categories
  tags: [string],                          // ["vip", "enterprise", "needs-attention"]
  categories: [string],                    // ["software", "consulting"]
  
  // Custom Fields (flexible for different business needs)
  customFields: {
    field_name: any                        // Dynamic custom fields
  },
  
  // Social Media
  socialMedia: {
    linkedin: string,
    twitter: string,
    facebook: string
  },
  
  // Communication Preferences
  communicationPreferences: {
    preferredChannel: string,              // "email", "phone", "telegram"
    doNotCall: boolean,
    doNotEmail: boolean,
    bestTimeToCall: string,                // "morning", "afternoon", "evening"
    timezone: string
  },
  
  // Activity Summary (denormalized for quick access)
  activitySummary: {
    totalLogs: number,
    totalCalls: number,
    totalEmails: number,
    totalComplaints: number,
    openComplaints: number,
    lastContactDate: timestamp,
    lastContactType: string,               // "call", "email", "meeting"
    nextFollowUpDate: timestamp,
    totalSamples: number
  },
  
  // Relationship
  relationship: {
    accountType: string,                   // "customer", "partner", "vendor"
    relationshipStartDate: timestamp,
    parentCompanyId: string,               // If subsidiary
    subsidiaries: [string]                 // Array of customer IDs
  },
  
  // Search Optimization (denormalized)
  searchTerms: [string],                   // Lowercase terms for fuzzy search
  
  // Metadata
  createdAt: timestamp,
  updatedAt: timestamp,
  createdBy: string,                       // User ID
  lastModifiedBy: string,
  
  // Soft delete
  deletedAt: timestamp | null,
  deletedBy: string | null
}
```

**Subcollections**:

1. **`/customers/{customerId}/logs/{logId}`** - Customer-specific logs
2. **`/customers/{customerId}/threads/{threadId}`** - Interaction threads
3. **`/customers/{customerId}/complaints/{complaintId}`** - Customer complaints (reference)
4. **`/customers/{customerId}/files/{fileId}`** - Attached files/documents
5. **`/customers/{customerId}/notes/{noteId}`** - Quick notes

**Indexes Required**:
- `tenantId` + `status`
- `tenantId` + `assignedTo`
- `tenantId` + `status` + `priority`
- `tenantId` + `tags` (array-contains)
- `tenantId` + `companyName`
- `tenantId` + `primaryContact.email`
- `tenantId` + `createdAt` (desc)
- `tenantId` + `activitySummary.lastContactDate` (desc)
- Full-text search on `searchTerms`

---

### 4. `logs` Collection

**Path**: `/logs/{logId}`

**Purpose**: Store all activity logs (calls, emails, meetings, notes, samples)

```javascript
{
  // Document ID: auto-generated
  id: string,
  
  // Tenant Association
  tenantId: string,
  
  // Associated Entities
  customerId: string,                      // Reference to customers collection
  customerName: string,                    // Denormalized for quick display
  
  // Thread/Grouping
  threadId: string | null,                 // Groups related logs together
  parentLogId: string | null,              // For replies/follow-ups
  
  // Log Type & Category
  type: string,                            // "call", "email", "meeting", "note", "sample", "task", "other"
  category: string,                        // "sales", "support", "general", "follow-up"
  subType: string | null,                  // For type="call": "inbound", "outbound"
  
  // Content
  subject: string,                         // Brief title
  description: string,                     // Rich text (HTML or Markdown)
  plainText: string,                       // Plain text version for search
  
  // Call-specific fields (if type="call")
  callDetails: {
    direction: string,                     // "inbound", "outbound"
    duration: number,                      // Duration in seconds
    phoneNumber: string,
    recordingUrl: string | null,
    outcome: string,                       // "answered", "voicemail", "no-answer", "busy"
    disposition: string,                   // "interested", "not-interested", "callback", "closed"
    callProvider: string                   // "twilio", "vonage"
  } | null,
  
  // Email-specific fields (if type="email")
  emailDetails: {
    messageId: string,                     // Gmail message ID
    threadId: string,                      // Gmail thread ID
    from: string,
    to: [string],
    cc: [string],
    bcc: [string],
    direction: string,                     // "inbound", "outbound"
    isRead: boolean,
    labels: [string]
  } | null,
  
  // Meeting-specific fields (if type="meeting")
  meetingDetails: {
    startTime: timestamp,
    endTime: timestamp,
    location: string,
    attendees: [{
      name: string,
      email: string,
      attended: boolean
    }],
    meetingType: string,                   // "in-person", "video", "phone"
    meetingLink: string | null
  } | null,
  
  // Sample-specific fields (if type="sample")
  sampleDetails: {
    productName: string,
    quantity: number,
    trackingNumber: string | null,
    dateSent: timestamp,
    dateReceived: timestamp | null,
    recipientName: string,
    recipientAddress: string,
    status: string                         // "sent", "delivered", "returned"
  } | null,
  
  // Attachments
  attachments: [{
    id: string,
    filename: string,
    url: string,                           // Firebase Storage URL
    storagePath: string,
    mimeType: string,
    size: number,                          // Bytes
    uploadedBy: string,
    uploadedAt: timestamp
  }],
  
  // Tags & Labels
  tags: [string],
  labels: [string],
  
  // Priority & Status
  priority: string,                        // "low", "normal", "high"
  status: string,                          // "draft", "completed", "pending", "cancelled"
  isImportant: boolean,
  isFlagged: boolean,
  
  // Task-related (if this log is a task)
  taskDetails: {
    dueDate: timestamp | null,
    completedDate: timestamp | null,
    isCompleted: boolean,
    reminder: timestamp | null
  } | null,
  
  // Automation
  source: string,                          // "manual", "email_sync", "call_integration", "automation"
  automationRuleId: string | null,
  
  // Mentions
  mentions: [string],                      // User IDs mentioned in description
  
  // Visibility
  visibility: string,                      // "public", "private", "team"
  visibleToUsers: [string],                // Specific user IDs (if visibility="private")
  
  // Search Optimization
  searchableContent: string,               // Combined searchable text
  
  // Metadata
  createdAt: timestamp,
  updatedAt: timestamp,
  createdBy: string,                       // User ID
  lastModifiedBy: string,
  
  // Soft delete
  deletedAt: timestamp | null,
  deletedBy: string | null
}
```

**Subcollection**: `/logs/{logId}/attachments/{attachmentId}`
- Detailed attachment metadata
- Version history

**Indexes Required**:
- `tenantId` + `customerId` + `createdAt` (desc)
- `tenantId` + `type` + `createdAt` (desc)
- `tenantId` + `createdBy` + `createdAt` (desc)
- `tenantId` + `threadId`
- `tenantId` + `tags` (array-contains)
- `tenantId` + `status`
- `tenantId` + `taskDetails.dueDate`

---

### 5. `complaints` Collection

**Path**: `/complaints/{complaintId}`

**Purpose**: Track customer complaints and issues

```javascript
{
  // Document ID: auto-generated
  id: string,
  
  // Unique Ticket Number (for customer reference)
  ticketNumber: string,                    // "TICKET-20251022-001" (auto-generated, sequential)
  
  // Tenant Association
  tenantId: string,
  
  // Customer
  customerId: string,
  customerName: string,                    // Denormalized
  customerEmail: string,                   // Denormalized
  
  // Complaint Details
  title: string,                           // Brief summary
  description: string,                     // Detailed description (rich text)
  
  // Classification
  category: string,                        // "product", "service", "billing", "delivery", "technical", "other"
  subCategory: string | null,              // More specific categorization
  productAffected: string | null,          // Product name/SKU
  
  // Severity & Priority
  severity: string,                        // "low", "medium", "high", "critical"
  priority: number,                        // 1-5 (calculated based on severity + other factors)
  impact: string,                          // "individual", "team", "company-wide"
  urgency: string,                         // "low", "medium", "high"
  
  // Status
  status: string,                          // "new", "acknowledged", "in_progress", "pending_customer", "resolved", "closed", "reopened"
  resolution: string | null,               // "fixed", "workaround", "duplicate", "not_a_bug", "wont_fix"
  
  // Assignment
  assignedTo: string | null,               // User ID
  assignedTeam: string | null,             // "support", "technical", "billing"
  assignedAt: timestamp | null,
  
  // SLA (Service Level Agreement)
  sla: {
    responseDeadline: timestamp,           // Must respond by
    resolutionDeadline: timestamp,         // Must resolve by
    responseTime: number | null,           // Actual response time in minutes
    resolutionTime: number | null,         // Actual resolution time in minutes
    isResponseOverdue: boolean,
    isResolutionOverdue: boolean,
    breachedAt: timestamp | null
  },
  
  // Timestamps
  acknowledgedAt: timestamp | null,
  acknowledgedBy: string | null,
  firstResponseAt: timestamp | null,
  firstResponseBy: string | null,
  resolvedAt: timestamp | null,
  resolvedBy: string | null,
  closedAt: timestamp | null,
  closedBy: string | null,
  reopenedAt: timestamp | null,
  
  // Resolution Details
  resolutionDetails: {
    summary: string,
    rootCause: string,
    actionsTaken: string,
    preventiveMeasures: string,
    timeSpent: number,                     // Minutes
    customerSatisfaction: number | null,   // 1-5 rating
    customerFeedback: string | null
  } | null,
  
  // Escalation
  escalation: {
    isEscalated: boolean,
    escalatedAt: timestamp | null,
    escalatedTo: string | null,            // User ID
    escalatedBy: string | null,
    escalationLevel: number,               // 1, 2, 3
    escalationReason: string | null
  },
  
  // Taiga Integration
  taigaIntegration: {
    isLinked: boolean,
    taigaIssueId: string | null,
    taigaProjectId: string | null,
    taigaUrl: string | null,
    linkedAt: timestamp | null,
    linkedBy: string | null,
    syncStatus: string                     // "synced", "pending", "failed"
  },
  
  // Communication
  communicationChannel: string,            // "email", "phone", "chat", "telegram", "web"
  lastCustomerUpdate: timestamp | null,
  lastInternalUpdate: timestamp | null,
  notificationsEnabled: boolean,
  
  // Attachments
  attachments: [{
    id: string,
    filename: string,
    url: string,
    mimeType: string,
    size: number,
    uploadedBy: string,                    // "customer" or user ID
    uploadedAt: timestamp
  }],
  
  // Related Items
  relatedComplaintIds: [string],           // Similar/related complaints
  relatedLogIds: [string],                 // Related logs
  duplicateOf: string | null,              // If marked as duplicate
  
  // Tags
  tags: [string],
  
  // Metrics
  metrics: {
    viewCount: number,
    updateCount: number,
    commentCount: number,
    customerResponseCount: number,
    internalCommentCount: number,
    reopenCount: number
  },
  
  // Visibility
  isPublic: boolean,                       // Can customer see this?
  
  // Search
  searchableText: string,                  // Combined text for search
  
  // Metadata
  createdAt: timestamp,
  updatedAt: timestamp,
  createdBy: string,                       // User ID or "customer"
  lastModifiedBy: string,
  
  // Soft delete
  deletedAt: timestamp | null,
  deletedBy: string | null
}
```

**Subcollections**:

1. **`/complaints/{complaintId}/timeline/{eventId}`**
```javascript
{
  id: string,
  timestamp: timestamp,
  eventType: string,                       // "created", "status_changed", "assigned", "commented", "resolved", "escalated"
  userId: string | null,
  userName: string,
  oldValue: any | null,
  newValue: any | null,
  details: string,
  automated: boolean                       // Was this action automated?
}
```

2. **`/complaints/{complaintId}/comments/{commentId}`**
```javascript
{
  id: string,
  content: string,
  commentType: string,                     // "internal", "customer_facing"
  authorId: string,
  authorName: string,
  authorType: string,                      // "user", "customer", "system"
  mentions: [string],                      // User IDs mentioned
  attachments: [object],
  isEdited: boolean,
  editedAt: timestamp | null,
  createdAt: timestamp
}
```

3. **`/complaints/{complaintId}/attachments/{attachmentId}`**
- Extended attachment metadata

**Indexes Required**:
- `tenantId` + `status` + `priority` (desc)
- `tenantId` + `assignedTo` + `status`
- `tenantId` + `customerId` + `createdAt` (desc)
- `tenantId` + `category`
- `tenantId` + `severity`
- `tenantId` + `sla.isResolutionOverdue` + `status`
- `tenantId` + `createdAt` (desc)
- `ticketNumber` (unique)
- `tenantId` + `tags` (array-contains)

---

### 6. `threads` Collection

**Path**: `/threads/{threadId}`

**Purpose**: Group related logs/interactions for same customer (concurrent conversations)

```javascript
{
  // Document ID: auto-generated
  id: string,
  
  // Tenant Association
  tenantId: string,
  
  // Customer
  customerId: string,
  customerName: string,
  
  // Thread Info
  name: string,                            // "Project Alpha", "Support Issue", "Sales Opportunity"
  description: string,
  type: string,                            // "project", "support", "sales", "general"
  
  // Status
  status: string,                          // "active", "closed", "on_hold"
  
  // Assignment
  ownerId: string,                         // Primary owner
  participants: [string],                  // User IDs involved
  
  // Related Items
  logIds: [string],                        // References to logs
  complaintIds: [string],                  // Related complaints
  
  // Dates
  startDate: timestamp,
  expectedEndDate: timestamp | null,
  actualEndDate: timestamp | null,
  lastActivityDate: timestamp,
  
  // Metrics
  totalLogs: number,
  totalCalls: number,
  totalEmails: number,
  
  // Tags
  tags: [string],
  
  // Metadata
  createdAt: timestamp,
  updatedAt: timestamp,
  createdBy: string,
  
  // Soft delete
  deletedAt: timestamp | null
}
```

**Indexes Required**:
- `tenantId` + `customerId` + `status`
- `tenantId` + `ownerId`
- `tenantId` + `lastActivityDate` (desc)

---

### 7. `emails` Collection

**Path**: `/emails/{emailId}`

**Purpose**: Store email data synced from Gmail

```javascript
{
  // Document ID: Gmail message ID or auto-generated
  id: string,
  
  // Tenant Association
  tenantId: string,
  
  // Gmail Integration
  gmailMessageId: string,                  // Unique Gmail message ID
  gmailThreadId: string,                   // Gmail thread ID
  gmailLabels: [string],                   // Gmail labels
  
  // Customer Association
  customerId: string | null,               // Auto-linked or manual
  customerName: string | null,
  linkingConfidence: number | null,        // 0-1 (how confident auto-linking is)
  
  // Email Headers
  from: {
    name: string,
    email: string
  },
  to: [{
    name: string,
    email: string
  }],
  cc: [{
    name: string,
    email: string
  }],
  bcc: [{
    name: string,
    email: string
  }],
  replyTo: string | null,
  
  // Content
  subject: string,
  bodyHtml: string,                        // HTML content
  bodyText: string,                        // Plain text content
  snippet: string,                         // First 150 chars
  
  // Metadata
  date: timestamp,                         // Email sent date
  direction: string,                       // "inbound", "outbound"
  
  // Classification (Automated)
  category: string,                        // "sales", "support", "complaint", "general", "spam"
  sentiment: string | null,                // "positive", "neutral", "negative" (AI analysis)
  priority: string,                        // "low", "normal", "high", "urgent"
  isAutoClassified: boolean,
  classificationConfidence: number,        // 0-1
  
  // Status
  isRead: boolean,
  isStarred: boolean,
  isArchived: boolean,
  isTrashed: boolean,
  
  // Attachments
  hasAttachments: boolean,
  attachments: [{
    filename: string,
    mimeType: string,
    size: number,
    attachmentId: string,                  // Gmail attachment ID
    url: string | null                     // Stored in Firebase Storage
  }],
  
  // Thread Info
  inReplyTo: string | null,                // Message ID this is replying to
  references: [string],                    // Thread references
  
  // Assignment
  assignedTo: string | null,               // User ID (auto-assigned)
  assignedBy: string | null,               // "system" or user ID
  assignedAt: timestamp | null,
  
  // Actions
  hasBeenReplied: boolean,
  repliedAt: timestamp | null,
  repliedBy: string | null,
  
  // Automation
  automationRuleApplied: string | null,    // Rule ID that processed this
  automationActions: [string],             // ["assigned", "tagged", "categorized"]
  
  // Related Items
  logId: string | null,                    // Created log entry
  complaintId: string | null,              // Created complaint
  
  // Tags
  tags: [string],
  
  // Search
  searchableContent: string,               // Subject + body for search
  
  // Sync Status
  syncStatus: string,                      // "synced", "pending", "failed"
  syncedAt: timestamp,
  lastSyncAttempt: timestamp,
  
  // Metadata
  createdAt: timestamp,                    // When added to CRM
  updatedAt: timestamp
}
```

**Indexes Required**:
- `tenantId` + `gmailThreadId`
- `tenantId` + `customerId` + `date` (desc)
- `tenantId` + `assignedTo` + `isRead`
- `tenantId` + `category`
- `tenantId` + `direction` + `date` (desc)
- `tenantId` + `tags` (array-contains)

---

### 8. `calls` Collection

**Path**: `/calls/{callId}`

**Purpose**: Store call records from VoIP integration

```javascript
{
  // Document ID: auto-generated or provider call ID
  id: string,
  
  // Tenant Association
  tenantId: string,
  
  // Customer Association
  customerId: string | null,
  customerName: string | null,
  
  // Call Details
  direction: string,                       // "inbound", "outbound"
  from: string,                            // Phone number
  to: string,                              // Phone number
  
  // Status
  status: string,                          // "ringing", "in-progress", "completed", "failed", "no-answer", "busy", "cancelled"
  outcome: string,                         // "answered", "voicemail", "no-answer", "busy", "failed"
  
  // Timing
  startTime: timestamp,
  answerTime: timestamp | null,
  endTime: timestamp | null,
  duration: number,                        // Total duration in seconds
  talkTime: number,                        // Actual talk time in seconds
  ringTime: number,                        // Time spent ringing
  
  // Participants
  initiatedBy: string | null,              // User ID
  handledBy: string | null,                // User ID who answered
  transferredTo: string | null,            // User ID if transferred
  
  // Recording
  recordingEnabled: boolean,
  recordingUrl: string | null,             // URL to recording file
  recordingDuration: number | null,
  recordingConsent: boolean,               // Was consent obtained?
  
  // Transcription (future feature)
  transcription: string | null,
  transcriptionConfidence: number | null,
  
  // VoIP Provider
  provider: string,                        // "twilio", "vonage", "plivo"
  providerCallId: string,                  // Provider's unique call ID
  providerData: object,                    // Provider-specific metadata
  
  // Call Disposition
  disposition: string,                     // "interested", "not-interested", "callback", "voicemail", "wrong-number", "decision-maker-unavailable"
  notes: string,                           // Agent notes
  followUpRequired: boolean,
  followUpDate: timestamp | null,
  
  // Quality
  callQuality: string | null,              // "excellent", "good", "fair", "poor"
  callQualityScore: number | null,         // 0-5
  
  // Related Items
  logId: string | null,                    // Created log entry
  complaintId: string | null,              // If complaint was filed
  
  // Tags
  tags: [string],
  
  // Cost (if applicable)
  cost: number | null,
  currency: string | null,
  
  // Metadata
  createdAt: timestamp,
  updatedAt: timestamp
}
```

**Indexes Required**:
- `tenantId` + `customerId` + `startTime` (desc)
- `tenantId` + `handledBy` + `startTime` (desc)
- `tenantId` + `direction` + `startTime` (desc)
- `tenantId` + `status`
- `tenantId` + `disposition`

---

### 9. `conversations` Collection

**Path**: `/conversations/{conversationId}`

**Purpose**: Store chatbot conversations (both internal and external)

```javascript
{
  // Document ID: auto-generated
  id: string,
  
  // Tenant Association
  tenantId: string,
  
  // Type
  conversationType: string,                // "internal", "external"
  
  // Participants
  userId: string | null,                   // Internal user (if internal conversation)
  customerId: string | null,               // Customer (if external conversation)
  
  // Channel
  channel: string,                         // "web_chat", "telegram", "mobile_app"
  channelSpecific: {
    telegramChatId: string | null,
    sessionId: string | null
  },
  
  // Conversation State
  status: string,                          // "active", "closed", "escalated_to_human"
  intent: string | null,                   // Detected intent (e.g., "check_order_status", "file_complaint")
  
  // Escalation
  escalatedToUser: string | null,          // User ID if escalated
  escalatedAt: timestamp | null,
  escalationReason: string | null,
  
  // Context
  context: object,                         // Conversation context/memory
  
  // Metrics
  messageCount: number,
  botResponseCount: number,
  humanResponseCount: number,
  averageResponseTime: number,
  
  // Related Items
  createdLogId: string | null,
  createdComplaintId: string | null,
  
  // Quality
  customerSatisfaction: number | null,     // 1-5 rating
  wasHelpful: boolean | null,
  feedback: string | null,
  
  // Metadata
  startedAt: timestamp,
  lastMessageAt: timestamp,
  endedAt: timestamp | null,
  createdAt: timestamp,
  updatedAt: timestamp
}
```

**Subcollection**: `/conversations/{conversationId}/messages/{messageId}`
```javascript
{
  id: string,
  senderType: string,                      // "user", "customer", "bot", "system"
  senderId: string | null,                 // User/customer ID
  senderName: string,
  
  // Content
  content: string,
  contentType: string,                     // "text", "image", "file", "quick_reply"
  
  // For bot messages
  intent: string | null,
  confidence: number | null,
  
  // Quick replies
  quickReplies: [{
    text: string,
    value: string
  }] | null,
  
  // Attachments
  attachments: [object] | null,
  
  // Status
  isRead: boolean,
  readAt: timestamp | null,
  
  // Metadata
  timestamp: timestamp,
  createdAt: timestamp
}
```

**Indexes Required**:
- `tenantId` + `conversationType` + `status`
- `tenantId` + `userId`
- `tenantId` + `customerId`
- `tenantId` + `startedAt` (desc)
- `tenantId` + `channel`

---

### 10. `automation_rules` Collection

**Path**: `/automation_rules/{ruleId}`

**Purpose**: Store automation rules for email sorting, assignment, etc.

```javascript
{
  // Document ID: auto-generated
  id: string,
  
  // Tenant Association
  tenantId: string,
  
  // Rule Info
  name: string,                            // "Auto-assign support emails"
  description: string,
  
  // Rule Type
  ruleType: string,                        // "email_classification", "email_assignment", "complaint_routing", "notification"
  
  // Status
  isEnabled: boolean,
  
  // Trigger
  trigger: {
    eventType: string,                     // "email_received", "complaint_created", "customer_added"
    conditions: [{
      field: string,                       // "subject", "from", "category"
      operator: string,                    // "contains", "equals", "starts_with", "regex"
      value: any
    }]
  },
  
  // Actions
  actions: [{
    actionType: string,                    // "assign_to_user", "set_category", "add_tag", "send_notification", "create_log"
    parameters: object                     // Action-specific parameters
  }],
  
  // Execution
  executionOrder: number,                  // Priority (1 = first)
  stopIfMatched: boolean,                  // Stop processing other rules if this matches
  
  // Stats
  stats: {
    totalExecutions: number,
    successfulExecutions: number,
    failedExecutions: number,
    lastExecutedAt: timestamp | null
  },
  
  // Metadata
  createdAt: timestamp,
  updatedAt: timestamp,
  createdBy: string,
  lastModifiedBy: string,
  
  // Soft delete
  deletedAt: timestamp | null
}
```

**Indexes Required**:
- `tenantId` + `isEnabled` + `executionOrder`
- `tenantId` + `ruleType`

---

### 11. `taiga_integrations` Collection

**Path**: `/taiga_integrations/{integrationId}`

**Purpose**: Store Taiga integration data

```javascript
{
  // Document ID: auto-generated
  id: string,
  
  // Tenant Association
  tenantId: string,
  
  // Complaint Reference
  complaintId: string,
  complaintTicketNumber: string,
  
  // Taiga Details
  taigaProjectId: string,
  taigaProjectName: string,
  taigaIssueId: string,
  taigaIssueRef: string,                   // Issue reference number
  taigaIssueUrl: string,
  taigaIssueType: string,                  // "user_story", "task", "issue", "bug"
  
  // Mapping
  mapping: {
    crmStatus: string,
    taigaStatus: string,
    statusMapping: object                  // How statuses map between systems
  },
  
  // Sync
  syncDirection: string,                   // "crm_to_taiga", "taiga_to_crm", "bidirectional"
  syncStatus: string,                      // "synced", "pending", "conflict", "failed"
  lastSyncedAt: timestamp,
  lastSyncError: string | null,
  
  // Change Log
  changeLog: [{
    timestamp: timestamp,
    field: string,
    oldValue: any,
    newValue: any,
    source: string                         // "crm", "taiga"
  }],
  
  // Metadata
  createdAt: timestamp,
  createdBy: string,
  updatedAt: timestamp
}
```

**Indexes Required**:
- `tenantId` + `complaintId` (unique)
- `tenantId` + `taigaIssueId`
- `tenantId` + `syncStatus`

---

### 12. `notifications` Collection

**Path**: `/notifications/{notificationId}`

**Purpose**: Store in-app notifications for users

```javascript
{
  // Document ID: auto-generated
  id: string,
  
  // Tenant Association
  tenantId: string,
  
  // Recipient
  userId: string,                          // Recipient user ID
  
  // Notification Details
  type: string,                            // "complaint_assigned", "mention", "task_due", "email_received"
  title: string,
  message: string,
  
  // Related Entity
  entityType: string | null,               // "complaint", "customer", "log", "email"
  entityId: string | null,
  entityUrl: string | null,                // Deep link to entity
  
  // Status
  isRead: boolean,
  readAt: timestamp | null,
  
  // Priority
  priority: string,                        // "low", "normal", "high", "urgent"
  
  // Action
  actionLabel: string | null,              // "View Complaint", "Reply"
  actionUrl: string | null,
  
  // Icon & Color
  icon: string | null,
  color: string | null,
  
  // Grouping
  groupKey: string | null,                 // Group similar notifications
  
  // Expiry
  expiresAt: timestamp | null,
  
  // Metadata
  createdAt: timestamp,
  createdBy: string | null                 // "system" or user ID
}
```

**Indexes Required**:
- `userId` + `isRead` + `createdAt` (desc)
- `tenantId` + `userId` + `type`
- `userId` + `priority` + `isRead`

---

### 13. `audit_logs` Collection

**Path**: `/audit_logs/{auditId}`

**Purpose**: Track all important actions for compliance and debugging

```javascript
{
  // Document ID: auto-generated
  id: string,
  
  // Tenant Association
  tenantId: string,
  
  // Action
  action: string,                          // "customer.created", "complaint.status_changed", "user.role_changed"
  actionCategory: string,                  // "create", "update", "delete", "access", "export"
  
  // Actor
  userId: string | null,                   // Who performed the action
  userName: string,
  userEmail: string,
  userRole: string,
  
  // Target
  targetType: string,                      // "customer", "complaint", "user", "setting"
  targetId: string,
  targetName: string | null,
  
  // Changes
  changes: [{
    field: string,
    oldValue: any,
    newValue: any
  }] | null,
  
  // Context
  ipAddress: string,
  userAgent: string,
  location: string | null,                 // City, country
  
  // Request Details
  requestMethod: string | null,            // "GET", "POST", "PUT", "DELETE"
  requestPath: string | null,
  
  // Result
  status: string,                          // "success", "failed"
  errorMessage: string | null,
  
  // Risk Level
  riskLevel: string,                       // "low", "medium", "high", "critical"
  
  // Metadata
  timestamp: timestamp,
  createdAt: timestamp
}
```

**Indexes Required**:
- `tenantId` + `timestamp` (desc)
- `tenantId` + `userId` + `timestamp` (desc)
- `tenantId` + `action`
- `tenantId` + `targetType` + `targetId`
- `tenantId` + `riskLevel` + `timestamp` (desc)

---

### 14. `system_config` Collection

**Path**: `/system_config/{configKey}`

**Purpose**: Store system-wide configuration (super admin only)

```javascript
{
  // Document ID: config key (e.g., "email_providers", "feature_flags")
  id: string,
  
  // Config Data
  key: string,
  value: any,                              // Can be any type
  valueType: string,                       // "string", "number", "boolean", "object", "array"
  
  // Description
  description: string,
  category: string,                        // "email", "features", "limits", "security"
  
  // Validation
  validationRules: object | null,
  
  // Access
  isPublic: boolean,                       // Can be accessed by tenants?
  isSensitive: boolean,                    // Contains sensitive data?
  
  // Metadata
  createdAt: timestamp,
  updatedAt: timestamp,
  lastModifiedBy: string
}
```

---

## Composite Indexes

Firebase Firestore requires composite indexes for queries with multiple filters. Here are the required composite indexes:

### Customers
```
Collection: customers
Fields: tenantId (Ascending), status (Ascending), priority (Descending), createdAt (Descending)

Collection: customers
Fields: tenantId (Ascending), assignedTo (Ascending), status (Ascending)

Collection: customers
Fields: tenantId (Ascending), activitySummary.lastContactDate (Descending)
```

### Complaints
```
Collection: complaints
Fields: tenantId (Ascending), status (Ascending), priority (Descending)

Collection: complaints
Fields: tenantId (Ascending), assignedTo (Ascending), status (Ascending)

Collection: complaints
Fields: tenantId (Ascending), sla.isResolutionOverdue (Ascending), status (Ascending)

Collection: complaints
Fields: tenantId (Ascending), severity (Ascending), createdAt (Descending)
```

### Logs
```
Collection: logs
Fields: tenantId (Ascending), customerId (Ascending), createdAt (Descending)

Collection: logs
Fields: tenantId (Ascending), type (Ascending), createdAt (Descending)

Collection: logs
Fields: tenantId (Ascending), createdBy (Ascending), createdAt (Descending)
```

### Emails
```
Collection: emails
Fields: tenantId (Ascending), customerId (Ascending), date (Descending)

Collection: emails
Fields: tenantId (Ascending), assignedTo (Ascending), isRead (Ascending)

Collection: emails
Fields: tenantId (Ascending), category (Ascending), date (Descending)
```

### Calls
```
Collection: calls
Fields: tenantId (Ascending), customerId (Ascending), startTime (Descending)

Collection: calls
Fields: tenantId (Ascending), handledBy (Ascending), startTime (Descending)
```

---

## Firestore Security Rules

### Basic Structure

```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    
    // Helper functions
    function isAuthenticated() {
      return request.auth != null;
    }
    
    function getUserData() {
      return get(/databases/$(database)/documents/users/$(request.auth.uid)).data;
    }
    
    function getTenantId() {
      return getUserData().tenantId;
    }
    
    function getUserRole() {
      return getUserData().role;
    }
    
    function isSuperAdmin() {
      return isAuthenticated() && getUserRole() == 'super_admin';
    }
    
    function isTenantAdmin() {
      return isAuthenticated() && getUserRole() == 'tenant_admin';
    }
    
    function belongsToTenant(tenantId) {
      return isAuthenticated() && getTenantId() == tenantId;
    }
    
    function hasPermission(permission) {
      return isAuthenticated() && 
             permission in getUserData().permissions;
    }
    
    // Tenants collection
    match /tenants/{tenantId} {
      allow read: if belongsToTenant(tenantId) || isSuperAdmin();
      allow create: if isSuperAdmin();
      allow update: if (belongsToTenant(tenantId) && isTenantAdmin()) || isSuperAdmin();
      allow delete: if isSuperAdmin();
    }
    
    // Users collection
    match /users/{userId} {
      allow read: if isAuthenticated() && 
                     (request.auth.uid == userId || 
                      belongsToTenant(resource.data.tenantId));
      allow create: if isTenantAdmin() || isSuperAdmin();
      allow update: if (request.auth.uid == userId) || 
                       isTenantAdmin() || 
                       isSuperAdmin();
      allow delete: if isTenantAdmin() || isSuperAdmin();
    }
    
    // Customers collection
    match /customers/{customerId} {
      allow read: if belongsToTenant(resource.data.tenantId) && 
                     hasPermission('customers.read');
      allow create: if belongsToTenant(request.resource.data.tenantId) && 
                       hasPermission('customers.create');
      allow update: if belongsToTenant(resource.data.tenantId) && 
                       hasPermission('customers.update');
      allow delete: if belongsToTenant(resource.data.tenantId) && 
                       hasPermission('customers.delete');
      
      // Subcollections
      match /logs/{logId} {
        allow read, write: if belongsToTenant(get(/databases/$(database)/documents/customers/$(customerId)).data.tenantId);
      }
    }
    
    // Complaints collection
    match /complaints/{complaintId} {
      allow read: if belongsToTenant(resource.data.tenantId);
      allow create: if belongsToTenant(request.resource.data.tenantId);
      allow update: if belongsToTenant(resource.data.tenantId) && 
                       (hasPermission('complaints.update') || 
                        resource.data.assignedTo == request.auth.uid);
      allow delete: if belongsToTenant(resource.data.tenantId) && 
                       hasPermission('complaints.delete');
      
      // Subcollections
      match /{subCollection}/{docId} {
        allow read, write: if belongsToTenant(get(/databases/$(database)/documents/complaints/$(complaintId)).data.tenantId);
      }
    }
    
    // Logs collection
    match /logs/{logId} {
      allow read: if belongsToTenant(resource.data.tenantId);
      allow create: if belongsToTenant(request.resource.data.tenantId);
      allow update: if belongsToTenant(resource.data.tenantId) && 
                       (hasPermission('logs.update') || 
                        resource.data.createdBy == request.auth.uid);
      allow delete: if belongsToTenant(resource.data.tenantId) && 
                       hasPermission('logs.delete');
    }
    
    // Emails collection
    match /emails/{emailId} {
      allow read: if belongsToTenant(resource.data.tenantId);
      allow create: if belongsToTenant(request.resource.data.tenantId);
      allow update: if belongsToTenant(resource.data.tenantId);
      allow delete: if belongsToTenant(resource.data.tenantId) && isTenantAdmin();
    }
    
    // Calls collection
    match /calls/{callId} {
      allow read: if belongsToTenant(resource.data.tenantId);
      allow create: if belongsToTenant(request.resource.data.tenantId);
      allow update: if belongsToTenant(resource.data.tenantId);
      allow delete: if belongsToTenant(resource.data.tenantId) && isTenantAdmin();
    }
    
    // Notifications collection
    match /notifications/{notificationId} {
      allow read: if isAuthenticated() && resource.data.userId == request.auth.uid;
      allow create: if isAuthenticated();
      allow update: if isAuthenticated() && resource.data.userId == request.auth.uid;
      allow delete: if isAuthenticated() && resource.data.userId == request.auth.uid;
    }
    
    // Audit logs - read only
    match /audit_logs/{auditId} {
      allow read: if belongsToTenant(resource.data.tenantId) && 
                     (isTenantAdmin() || isSuperAdmin());
      allow write: if false; // Only server can write
    }
    
    // System config - super admin only
    match /system_config/{configKey} {
      allow read: if isSuperAdmin() || 
                     (isAuthenticated() && resource.data.isPublic == true);
      allow write: if isSuperAdmin();
    }
  }
}
```

---

## Data Relationships Diagram

```
┌─────────────┐
│   TENANTS   │
└──────┬──────┘
       │ 1:N
       ├──────────────────┬──────────────────┬──────────────────┐
       │                  │                  │                  │
       ▼                  ▼                  ▼                  ▼
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│    USERS    │    │  CUSTOMERS  │    │ COMPLAINTS  │    │    LOGS     │
└──────┬──────┘    └──────┬──────┘    └──────┬──────┘    └──────┬──────┘
       │                  │                  │                  │
       │                  │ 1:N              │ 1:N              │
       │                  ├──────────────────┤                  │
       │                  │                  │                  │
       │                  ▼                  ▼                  │
       │            ┌─────────────┐    ┌─────────────┐         │
       │            │   THREADS   │    │  TIMELINE   │         │
       │            └─────────────┘    └─────────────┘         │
       │                  │                                     │
       │                  │ 1:N                                 │
       │                  ▼                                     │
       │            ┌─────────────┐                            │
       │            │ THREAD LOGS │◄───────────────────────────┘
       │            └─────────────┘
       │
       ├──────────────────┬──────────────────┬──────────────────┐
       │                  │                  │                  │
       ▼                  ▼                  ▼                  ▼
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   EMAILS    │    │    CALLS    │    │CONVERSATIONS│    │NOTIFICATIONS│
└─────────────┘    └─────────────┘    └──────┬──────┘    └─────────────┘
                                              │
                                              │ 1:N
                                              ▼
                                        ┌─────────────┐
                                        │  MESSAGES   │
                                        └─────────────┘

┌─────────────┐           ┌─────────────┐
│ COMPLAINTS  │──────────►│    TAIGA    │
└─────────────┘  1:1      │INTEGRATIONS │
                          └─────────────┘
```

---

## Query Examples

### 1. Get all active customers for a tenant, ordered by last contact

```javascript
db.collection('customers')
  .where('tenantId', '==', tenantId)
  .where('status', '==', 'active')
  .orderBy('activitySummary.lastContactDate', 'desc')
  .limit(50)
  .get()
```

### 2. Get overdue high-priority complaints

```javascript
db.collection('complaints')
  .where('tenantId', '==', tenantId)
  .where('sla.isResolutionOverdue', '==', true)
  .where('priority', '>=', 4)
  .orderBy('priority', 'desc')
  .orderBy('createdAt', 'asc')
  .get()
```

### 3. Get customer timeline (all logs)

```javascript
db.collection('logs')
  .where('tenantId', '==', tenantId)
  .where('customerId', '==', customerId)
  .orderBy('createdAt', 'desc')
  .limit(100)
  .get()
```

### 4. Get unread emails assigned to user

```javascript
db.collection('emails')
  .where('tenantId', '==', tenantId)
  .where('assignedTo', '==', userId)
  .where('isRead', '==', false)
  .orderBy('date', 'desc')
  .get()
```

### 5. Get all calls for a customer

```javascript
db.collection('calls')
  .where('tenantId', '==', tenantId)
  .where('customerId', '==', customerId)
  .orderBy('startTime', 'desc')
  .get()
```

### 6. Full-text search on customers (using array-contains)

```javascript
// Add search terms to customer document as array
searchTerms: ['acme', 'corporation', 'john', 'doe', 'john.doe@acme.com']

// Query
db.collection('customers')
  .where('tenantId', '==', tenantId)
  .where('searchTerms', 'array-contains', searchTerm.toLowerCase())
  .get()
```

### 7. Get user's unread notifications

```javascript
db.collection('notifications')
  .where('userId', '==', userId)
  .where('isRead', '==', false)
  .orderBy('createdAt', 'desc')
  .limit(20)
  .get()
```

---

## Performance Optimization

### 1. Denormalization Strategy
- **Customer name/email** in logs, complaints → Avoid joins
- **Activity summary** in customer document → Quick dashboard stats
- **User name/role** in audit logs → Avoid lookups

### 2. Pagination
Always use pagination for large result sets:
```javascript
// First page
let first = db.collection('customers')
  .where('tenantId', '==', tenantId)
  .orderBy('createdAt', 'desc')
  .limit(25);

// Next page
let next = db.collection('customers')
  .where('tenantId', '==', tenantId)
  .orderBy('createdAt', 'desc')
  .startAfter(lastDocument)
  .limit(25);
```

### 3. Real-time Listeners
Use real-time listeners for critical data only:
```javascript
// Listen to assigned complaints
db.collection('complaints')
  .where('tenantId', '==', tenantId)
  .where('assignedTo', '==', userId)
  .where('status', '!=', 'closed')
  .onSnapshot(snapshot => {
    // Update UI
  });
```

### 4. Batch Operations
Use batch writes for multiple updates:
```javascript
const batch = db.batch();

// Update multiple documents
batch.update(customerRef, { status: 'inactive' });
batch.update(logRef, { customerId: null });
batch.delete(threadRef);

await batch.commit();
```

### 5. Cloud Functions for Heavy Operations
- Email auto-classification → Cloud Function
- Automated email sorting → Cloud Function
- SLA breach detection → Scheduled Cloud Function
- Analytics aggregation → Scheduled Cloud Function

---

## Backup & Recovery

### 1. Automated Backups
```javascript
// Schedule daily backups using Cloud Scheduler + Cloud Functions
exports.scheduledFirestoreBackup = functions.pubsub
  .schedule('0 2 * * *') // 2 AM daily
  .timeZone('America/New_York')
  .onRun(async (context) => {
    // Trigger Firestore export
    const projectId = process.env.GCP_PROJECT || process.env.GCLOUD_PROJECT;
    const databaseName = client.databasePath(projectId, '(default)');
    
    return client.exportDocuments({
      name: databaseName,
      outputUriPrefix: `gs://${bucket}/firestore-backups`,
      collectionIds: []
    });
  });
```

### 2. Retention Policy
- Daily backups: Keep for 7 days
- Weekly backups: Keep for 4 weeks
- Monthly backups: Keep for 12 months

---

## Migration Strategy

### Phase 1: Initial Setup
1. Create Firestore database
2. Set up collections
3. Configure indexes
4. Implement security rules

### Phase 2: Seed Data
1. Create super admin user
2. Create first tenant
3. Add sample customers
4. Test CRUD operations

### Phase 3: Integration
1. Connect Firebase Auth
2. Set up Cloud Functions
3. Configure n8n workflows
4. Test email sync

### Phase 4: Optimization
1. Monitor query performance
2. Add necessary indexes
3. Optimize security rules
4. Implement caching where needed

---

## Cost Estimation (Firebase Pricing)

### Expected Usage (Initial - 5-10 users, 500 customers):

| Operation | Monthly Estimate | Cost |
|-----------|-----------------|------|
| Document Reads | 500K | $0.18 |
| Document Writes | 100K | $0.54 |
| Document Deletes | 10K | $0.02 |
| Storage | 5GB | $0.90 |
| **Total** | | **~$1.64/month** |

### Scaling (50 users, 5000 customers):

| Operation | Monthly Estimate | Cost |
|-----------|-----------------|------|
| Document Reads | 5M | $1.80 |
| Document Writes | 1M | $5.40 |
| Document Deletes | 50K | $0.10 |
| Storage | 50GB | $9.00 |
| **Total** | | **~$16.30/month** |

*Note: Firebase has a generous free tier that covers initial development*

---

## Summary

This database schema provides:

✅ **Multi-tenancy** with complete data isolation  
✅ **Scalable structure** for 200-500 customers initially, scalable to thousands  
✅ **Efficient querying** with proper indexes  
✅ **Security** with Firestore security rules  
✅ **Flexibility** with custom fields and extensible design  
✅ **Real-time capabilities** for collaborative features  
✅ **Audit trail** for compliance  
✅ **Support for all 11 features** in the PRD

The schema is optimized for Firebase Firestore's strengths (real-time, scalability, security) while working around its limitations (no joins, limited queries) through strategic denormalization and proper indexing.
