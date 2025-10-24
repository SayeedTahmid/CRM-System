# Phase 1: Core MVP - 2-Week Sprint Plan

**Timeline:** Days 1-14 (2 weeks)  
**Team:** 2-3 full-stack developers  
**Goal:** Ship functional CRM with customer & log management

---

## 🎯 Sprint Goal

Deliver a working CRM where users can:
1. Register/Login (multi-tenant)
2. Add and manage customers
3. Log customer interactions (calls, notes, meetings)
4. Search for customers
5. View customer timeline

---

## 👥 Team Structure (Recommended)

**If 2 developers:**
- **Dev 1:** Backend + Database (Python/Firebase)
- **Dev 2:** Frontend (React/TailwindCSS)
- **Overlap:** Both contribute to critical path items

**If 3 developers:**
- **Dev 1:** Backend APIs (Python/FastAPI)
- **Dev 2:** Frontend Core (React components)
- **Dev 3:** Frontend Features + Integration

---

## 📅 Week 1: Foundation (Days 1-7)

### Day 1: Project Setup & Authentication (Backend Focus)

**Backend (Dev 1):**
- [ ] Create Firebase project (Firestore, Auth, Storage, Hosting)
- [ ] Set up Python project structure:
  ```
  /backend
    /api
      __init__.py
      auth.py
      customers.py
      logs.py
    /models
      user.py
      customer.py
      log.py
    /services
      firebase_service.py
      auth_service.py
    /utils
      validators.py
    main.py
    requirements.txt
  ```
- [ ] Install dependencies: `fastapi`, `uvicorn`, `firebase-admin`, `python-jose`, `passlib`
- [ ] Configure Firebase Admin SDK (service account JSON)
- [ ] Create `/auth/register` endpoint (email/password)
- [ ] Create `/auth/login` endpoint (returns JWT token)
- [ ] JWT middleware for protected routes

**Frontend (Dev 2):**
- [ ] Create React project with Vite: `npm create vite@latest crm-frontend -- --template react`
- [ ] Install dependencies: `tailwindcss`, `react-router-dom`, `axios`, `firebase`
- [ ] Set up TailwindCSS with dark mode configuration
- [ ] Configure Firebase SDK (web config)
- [ ] Create folder structure:
  ```
  /src
    /components
      /auth
      /customers
      /logs
      /common
    /pages
      LoginPage.jsx
      DashboardPage.jsx
      CustomersPage.jsx
    /services
      api.js
      auth.js
    /hooks
    /utils
    App.jsx
    main.jsx
  ```
- [ ] Create Login page UI (form with email/password)
- [ ] Create Register page UI
- [ ] Implement Firebase authentication (register/login)
- [ ] Set up protected routes (React Router)

**End of Day 1 Checkpoint:**
- [ ] Backend API running on `localhost:8000`
- [ ] Frontend running on `localhost:5173`
- [ ] Can register new user and login
- [ ] JWT token stored in localStorage

---

### Day 2: Multi-Tenancy & User Management

**Backend (Dev 1):**
- [ ] Create Tenant model:
  ```javascript
  {
    id: string,
    companyName: string,
    subdomain: string,
    createdAt: timestamp,
    adminUserId: string
  }
  ```
- [ ] Create User model:
  ```javascript
  {
    id: string,
    tenantId: string,
    email: string,
    displayName: string,
    role: 'admin' | 'user',
    createdAt: timestamp
  }
  ```
- [ ] Modify `/auth/register` to create tenant for first user
- [ ] Add tenantId to JWT token payload
- [ ] Create middleware to extract tenantId from JWT
- [ ] Create `/users` endpoints (list, invite, deactivate)
- [ ] Implement Firestore security rules (tenant isolation)

**Frontend (Dev 2):**
- [ ] Create dashboard layout (sidebar, header, main content)
- [ ] Implement dark theme (TailwindCSS dark classes)
- [ ] Add purple accent colors (#6C63FF)
- [ ] Create user profile dropdown (logout, settings)
- [ ] Create Users page (admin only)
- [ ] User list table
- [ ] Invite user modal (send email invite)

**End of Day 2 Checkpoint:**
- [ ] Multi-tenant architecture working
- [ ] Users belong to specific tenant
- [ ] Tenant data completely isolated (test with 2 tenants)
- [ ] Admin can invite users

---

### Day 3: Customer Management - Backend

**Backend (Dev 1):**
- [ ] Create Customer model:
  ```javascript
  {
    id: string,
    tenantId: string,
    companyName: string,
    contactPerson: {
      firstName: string,
      lastName: string,
      email: string,
      phone: string,
      role: string
    },
    address: {
      street: string,
      city: string,
      state: string,
      zip: string,
      country: string
    },
    tags: string[],
    status: 'active' | 'inactive' | 'prospect',
    assignedTo: string,
    createdAt: timestamp,
    updatedAt: timestamp,
    createdBy: string
  }
  ```
- [ ] Create `/customers` endpoints:
  - `GET /customers` - List with pagination (limit, offset)
  - `GET /customers/:id` - Get single customer
  - `POST /customers` - Create customer
  - `PUT /customers/:id` - Update customer
  - `DELETE /customers/:id` - Soft delete
  - `GET /customers/search?q=query` - Search by name, email, company
- [ ] Add validation (email format, phone format, required fields)
- [ ] Automatically set tenantId from JWT
- [ ] Firestore indexes for search queries

**Frontend (Dev 2):**
- [ ] Create Customer service (`/services/customerService.js`)
- [ ] Create API client with axios (base URL, interceptors for auth token)
- [ ] Create Customers page route

**End of Day 3 Checkpoint:**
- [ ] Customer CRUD API fully working
- [ ] Can test with Postman/Insomnia
- [ ] Tenant isolation verified

---

### Day 4: Customer Management - Frontend List

**Backend (Dev 1):**
- [ ] Test and fix customer endpoints
- [ ] Add sorting (by name, created date)
- [ ] Add filtering (by status, assigned user)
- [ ] Optimize queries (add indexes)

**Frontend (Dev 2):**
- [ ] Create Customers page UI:
  - Header with "Add Customer" button
  - Search bar
  - Filter dropdowns (status, assigned to)
  - Sort dropdown
- [ ] Create customer list table:
  - Columns: Company, Contact, Email, Phone, Status, Actions
  - Pagination controls (prev, next, page numbers)
  - Row click → navigate to detail page
- [ ] Create "Add Customer" modal/form:
  - Company name (required)
  - Contact: First name, Last name, Email (required), Phone
  - Address fields (optional)
  - Status dropdown
  - Tags input (comma-separated)
- [ ] Form validation (required fields, email format)
- [ ] Submit → POST to API → refresh list

**End of Day 4 Checkpoint:**
- [ ] Customer list displays correctly
- [ ] Pagination works
- [ ] Can create new customer via modal
- [ ] Validation works

---

### Day 5: Customer Management - Detail & Edit

**Backend (Dev 1):**
- [ ] Start working on Logs backend (prep for Day 6)
- [ ] Create Log model
- [ ] Start log endpoints

**Frontend (Dev 2):**
- [ ] Create Customer Detail page:
  - Customer info card (editable)
  - Tabs: Timeline, Details, Files
  - Quick actions: Edit, Delete, Add Log
- [ ] Edit customer functionality:
  - Inline editing or modal
  - PUT request to API
  - Show success toast
- [ ] Delete customer:
  - Confirmation dialog
  - Soft delete (status = inactive)
- [ ] Loading states (skeletons or spinners)
- [ ] Error handling (display error messages)

**End of Day 5 Checkpoint:**
- [ ] Customer detail page works
- [ ] Can edit customer info
- [ ] Can delete (soft delete) customer
- [ ] Error handling in place

---

### Day 6: Logging System - Backend

**Backend (Dev 1):**
- [ ] Finalize Log model:
  ```javascript
  {
    id: string,
    tenantId: string,
    customerId: string,
    type: 'call' | 'email' | 'meeting' | 'note' | 'sample' | 'other',
    subject: string,
    description: string,
    attachments: [{
      filename: string,
      url: string,
      size: number,
      type: string
    }],
    tags: string[],
    createdAt: timestamp,
    createdBy: string,
    updatedAt: timestamp
  }
  ```
- [ ] Create `/logs` endpoints:
  - `GET /logs?customerId=xxx` - List logs for customer
  - `GET /logs/:id` - Get single log
  - `POST /logs` - Create log
  - `PUT /logs/:id` - Update log (within 24h)
  - `DELETE /logs/:id` - Delete log
- [ ] Create `/logs/:id/attachments` endpoint (file upload)
- [ ] Integrate Firebase Storage for attachments
- [ ] Handle file upload (max 10MB, allowed types: PDF, images, docs)
- [ ] Generate signed URLs for file download

**Frontend (Dev 2):**
- [ ] Create Log service (`/services/logService.js`)
- [ ] Create "Add Log" modal:
  - Select log type (dropdown with icons)
  - Subject field (required, max 200 chars)
  - Description textarea (optional, rich text - basic)
  - File upload (drag-and-drop or file picker)
  - Tags input
  - Date/time picker (default: now)
- [ ] File upload UI:
  - Show selected files
  - Upload progress bar
  - Remove file option

**End of Day 6 Checkpoint:**
- [ ] Log CRUD API working
- [ ] File upload to Firebase Storage works
- [ ] Can create log via Postman

---

### Day 7: Logging System - Frontend & Timeline

**Backend (Dev 1):**
- [ ] Optimize log queries (indexes)
- [ ] Add log search endpoint
- [ ] Add filter by type, date range

**Frontend (Dev 2):**
- [ ] Implement "Add Log" modal functionality:
  - POST log data to API
  - Upload files to backend
  - Show success message
  - Refresh timeline
- [ ] Create Customer Timeline component (in Customer Detail):
  - Chronological list of logs (newest first)
  - Each log item:
    - Type icon (colored)
    - Subject (clickable to expand)
    - Creator and timestamp
    - Preview of description (truncated)
    - Attachments list
  - Expand/collapse log details
  - Filter by log type (checkboxes at top)
- [ ] Display attachments:
  - Show filename with icon
  - Click to download
  - Preview images inline (thumbnail)

**End of Day 7 Checkpoint:**
- [ ] Can create logs from customer detail page
- [ ] Timeline displays all logs chronologically
- [ ] Attachments upload and download works
- [ ] Filter by log type works
- [ ] **Week 1 complete! 🎉**

---

## 📅 Week 2: Search, Polish & Deploy (Days 8-14)

### Day 8: Basic Search

**Backend (Dev 1):**
- [ ] Implement customer search:
  - `/customers/search?q=query`
  - Search in: companyName, contactPerson.firstName, contactPerson.lastName, contactPerson.email
  - Return customers matching query (case-insensitive)
  - Limit results to 20
- [ ] Add indexes for search fields:
  - Composite index: tenantId + companyNameLower
  - Composite index: tenantId + email

**Frontend (Dev 2):**
- [ ] Create global search bar (in header):
  - Input with search icon
  - Debounced search (300ms)
  - Dropdown results as user types
- [ ] Search results dropdown:
  - Show matching customers (name, email)
  - Click result → navigate to customer detail
  - "View all results" link if > 10 matches
- [ ] Keyboard navigation (arrow keys, enter)

**End of Day 8 Checkpoint:**
- [ ] Global search works
- [ ] Results appear as user types
- [ ] Can navigate to customer from search

---

### Day 9: Tags & Basic Filters

**Backend (Dev 1):**
- [ ] Add tag-based filtering:
  - `/customers?tags=VIP,Enterprise`
  - Return customers with any of the specified tags
- [ ] Add status filtering:
  - `/customers?status=active`

**Frontend (Dev 2):**
- [ ] Implement tags functionality:
  - Add tags to customer (chips/badges)
  - Remove tags (click X)
  - Tag autocomplete (from existing tags)
- [ ] Add filter controls to customer list:
  - Status dropdown (All, Active, Inactive, Prospect)
  - Tags multi-select dropdown
  - Apply filters → refresh customer list
- [ ] Display active filters (chips with X to remove)

**End of Day 9 Checkpoint:**
- [ ] Tags work on customers
- [ ] Can filter customers by status and tags
- [ ] Filters persist in URL (query params)

---

### Day 10: UI Polish & Responsive Design

**Backend (Dev 1):**
- [ ] Comprehensive testing of all endpoints
- [ ] Fix any bugs found
- [ ] Add error handling (try-catch, meaningful error messages)
- [ ] Add logging (structured logs for debugging)

**Frontend (Dev 2):**
- [ ] Dark theme refinement:
  - Ensure all components use dark theme colors
  - Test light mode (toggle in settings)
- [ ] Purple accent color (#6C63FF) applied consistently:
  - Buttons, links, active states
  - Focus rings
  - Progress indicators
- [ ] Responsive design:
  - Mobile breakpoints (< 768px)
  - Tablet breakpoints (768px - 1024px)
  - Desktop (> 1024px)
- [ ] Mobile navigation (hamburger menu)
- [ ] Touch-friendly buttons (min 44px tap target)

**End of Day 10 Checkpoint:**
- [ ] UI looks polished
- [ ] Dark theme consistent
- [ ] Works well on mobile and tablet
- [ ] No obvious visual bugs

---

### Day 11: Error Handling & Loading States

**Backend (Dev 1):**
- [ ] Standardize error responses:
  ```json
  {
    "error": {
      "code": "CUSTOMER_NOT_FOUND",
      "message": "Customer with ID xxx not found",
      "details": {}
    }
  }
  ```
- [ ] Add input validation errors (400 Bad Request)
- [ ] Add auth errors (401 Unauthorized, 403 Forbidden)
- [ ] Add rate limiting (optional, if time permits)

**Frontend (Dev 2):**
- [ ] Implement error handling:
  - Display error toasts/notifications
  - Inline form errors (field-level)
  - Error pages (404, 500)
- [ ] Loading states:
  - Skeleton loaders for customer list
  - Spinners for buttons during submit
  - Progress bars for file uploads
- [ ] Empty states:
  - "No customers yet" with CTA to add first customer
  - "No logs yet" with CTA to add first log
- [ ] Success notifications (toasts)

**End of Day 11 Checkpoint:**
- [ ] All error scenarios handled gracefully
- [ ] Loading states provide feedback
- [ ] Empty states guide users

---

### Day 12: Testing & Bug Fixes

**All Developers:**
- [ ] Create testing checklist (spreadsheet or doc)
- [ ] Test all features:
  - **Auth:** Register, login, logout, session persistence
  - **Customers:** Create, read, update, delete, search, filter
  - **Logs:** Create, view timeline, attachments, filter by type
  - **Tags:** Add, remove, filter by tags
  - **Multi-tenancy:** Create 2 tenants, verify data isolation
  - **Permissions:** Admin can do everything, user has limited access
- [ ] Cross-browser testing:
  - Chrome ✅
  - Firefox ✅
  - Safari ✅
  - Edge ✅
- [ ] Mobile testing:
  - iOS Safari ✅
  - Android Chrome ✅
- [ ] Bug triage:
  - Critical (blocks usage) → fix immediately
  - High (affects experience) → fix today
  - Medium/Low → backlog
- [ ] Fix critical and high-priority bugs

**End of Day 12 Checkpoint:**
- [ ] All critical bugs fixed
- [ ] Testing checklist complete
- [ ] App stable and usable

---

### Day 13: Deployment & Documentation

**Backend (Dev 1):**
- [ ] Prepare for deployment:
  - Environment variables (.env file)
  - Production Firebase config (separate project)
  - CORS configuration (allow frontend domain)
- [ ] Deploy backend:
  - Option 1: Firebase Functions (serverless)
  - Option 2: Google Cloud Run (containerized)
  - Option 3: Heroku, Railway, or similar
- [ ] Set up production Firestore:
  - Copy security rules
  - Create indexes
- [ ] Test production API (Postman)

**Frontend (Dev 2):**
- [ ] Update API base URL to production
- [ ] Build production bundle: `npm run build`
- [ ] Deploy to Firebase Hosting:
  - `firebase init hosting`
  - `firebase deploy --only hosting`
- [ ] Test production app (all features)
- [ ] Set up custom domain (optional)

**Both:**
- [ ] Write basic documentation:
  - **README:** How to run locally
  - **DEPLOYMENT:** How to deploy
  - **USER_GUIDE:** How to use the CRM
    - How to add a customer
    - How to log an interaction
    - How to search
- [ ] Create screenshots for user guide

**End of Day 13 Checkpoint:**
- [ ] Production environment deployed
- [ ] App accessible via public URL
- [ ] Basic documentation written

---

### Day 14: Final Testing, Demo Prep & Launch

**All Developers:**
- [ ] Final smoke testing in production:
  - Register new user
  - Create customers
  - Add logs with attachments
  - Search and filter
  - Test on mobile
- [ ] Performance check:
  - Page load times (Lighthouse)
  - API response times
  - File upload speed
- [ ] Security check:
  - Firestore security rules active
  - Tenant isolation verified
  - No API keys exposed in frontend
- [ ] Prepare demo:
  - Seed demo data (5-10 customers, 20+ logs)
  - Demo script (what to show)
  - Talking points (features, benefits)
- [ ] Create demo video (optional, 2-3 minutes)
- [ ] Invite pilot users:
  - Send invitations to 3-5 users
  - Provide login instructions
  - Set up support email/channel

**End of Day 14 Checkpoint:**
- [ ] Production app fully tested
- [ ] Demo ready
- [ ] Pilot users invited
- [ ] **Phase 1 COMPLETE! 🚀🎉**

---

## ✅ Phase 1 Success Criteria

At the end of 2 weeks, you should have:

### Functional Requirements
- [x] User registration and login working
- [x] Multi-tenant architecture (data completely isolated)
- [x] Customer CRUD (create, read, update, delete)
- [x] Customer list with pagination (50 per page)
- [x] Customer detail page with full info
- [x] Log CRUD (create, view, edit within 24h, delete)
- [x] Customer timeline (chronological logs)
- [x] File attachments (upload, download, max 10MB)
- [x] Basic search (customers by name, email, company)
- [x] Tags (add, remove, filter)
- [x] Filter by status
- [x] Responsive UI (desktop, tablet, mobile)
- [x] Dark theme with purple accents

### Non-Functional Requirements
- [x] Page load < 3 seconds
- [x] No critical bugs
- [x] Works in Chrome, Firefox, Safari, Edge
- [x] Works on iOS and Android (responsive web)
- [x] Deployed to production (public URL)
- [x] Basic documentation written

### Deliverables
- [x] Working production app
- [x] Source code in Git repository
- [x] Basic documentation (README, USER_GUIDE)
- [x] 3-5 pilot users can access and use the system
- [x] Demo-ready for stakeholders

---

## 🚨 Risk Mitigation

### If You Fall Behind Schedule

**End of Week 1 (Day 7) - Not on track?**
- **Cut scope immediately:**
  - Remove "nice-to-have" features (tags, advanced filters)
  - Focus on core CRUD (customers, logs)
  - Simplify UI (basic styling, skip dark theme)

**Day 10 - Still behind?**
- **Minimal MVP:**
  - Customers: Add, list, view only (no edit/delete)
  - Logs: Add, view only
  - Skip: Search, tags, filters, file attachments
  - Ship something working

**Day 12 - Critical bugs?**
- **Triage ruthlessly:**
  - Fix only critical (app-breaking) bugs
  - Document known issues for Phase 2
  - Focus on stable core features

### Contingency Plan

**If one developer unavailable:**
- Remaining dev focuses on backend + basic frontend
- Use Firebase UI library for quick frontend (compromise on design)

**If integration issues (Firebase, etc.):**
- Have backup plans (e.g., local JSON file for dev)
- Escalate immediately to get help

---

## 📊 Daily Standup Questions

**Every morning (15 minutes):**

1. **Yesterday:** What did I complete?
2. **Today:** What will I complete?
3. **Blockers:** Anything blocking me?

**Track progress:**
- Checkboxes in this document
- Burndown chart (tasks remaining vs. days left)

**Celebrate wins:**
- Every feature completed
- Milestone reached
- Bug fixed

---

## 🎉 End of Phase 1

**After Day 14:**
- Demo to stakeholders ✅
- Collect pilot user feedback ✅
- Identify Phase 2 priorities ✅
- Take a day off (seriously, you earned it!) ✅

**Then jump into Phase 2 (Email Integration)** 🚀

---

## 📝 Notes & Lessons Learned

Use this space to document:
- What went well
- What didn't go well
- What to do differently in Phase 2
- Technical debt accumulated
- Feature ideas from users

---

**Good luck! You've got this! 💪🚀**
