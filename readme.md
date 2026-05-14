# ContractorBoard — Django Job Board & Lead Marketplace

A full-stack two-sided marketplace connecting homeowners with verified 
HVAC, Plumbing, Roofing, and Electrical contractors.

## 🌐 Live Demo
[Coming soon after deployment]

---

## 📌 What It Does

ContractorBoard allows homeowners to post jobs and contractors to browse, 
filter, and send inquiries. Both sides get dedicated dashboards to manage 
their activity.

**Homeowners can:**
- Post jobs with budget, location, and niche
- Receive inquiries from contractors
- Browse and review verified contractors

**Contractors can:**
- Browse and search open jobs
- Filter by niche, location, and budget
- Send inquiries directly to homeowners
- Build a public profile with reviews and ratings

---

## ✨ Key Features

- Custom User Model with Contractor and Homeowner roles
- Full-text job search using Django Q objects
- Multi-field filters — niche, location, budget
- Pagination on job listings
- Inquiry system with automated email notifications
- Contractor profiles with star rating and review system
- Verified contractor badge (managed via Django Admin)
- Role-based access control throughout
- Responsive UI built with Bootstrap 4 (Jobboard template)
- PostgreSQL database
- Deployed on Railway

---

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django 6.0 |
| Database | PostgreSQL |
| Frontend | Bootstrap 4 |
| Auth | Django Auth + Custom User Model |
| Email | Gmail SMTP |
| Static Files | Whitenoise |
| Deployment | Railway |

---

## ⚙️ Local Setup

**1 — Clone the repo**