# Django News Publishing Platform

A simple yet powerful web application to publish, manage, and display news articles, built using Django. It supports user login, admin control, and role-based permissions with a clean and professional frontend.

---

## Highlights

-  **Django Authentication**: Secure login/logout using Django's built-in auth system
-  **Role-Based Access**:
  - Admins can view, edit, and delete all articles
  - Regular users can view and manage only their own articles
-  **Form-Based Article Management**: Create, edit, and delete articles via clean HTML forms
-  **Clean UI**: Styled entirely with internal CSS — no external CSS or JavaScript required
-  **Auto-Publishing**: Articles are automatically published with the current timestamp
-  **Custom Access Control**: Edit/Delete buttons shown only to admin users

---

## Features

- User login/logout with Django authentication
- Create, edit, delete news articles via form interface
- Articles include title, content, and publish date
- Admin sees all articles; users see only their own
- Only admins can edit or delete any article
- Internal CSS makes the frontend look clean and professional

---

## Tech Stack Used

- **Backend**: Django (Python)
- **Frontend**: HTML & Internal CSS
- **Database**: SQLite (default Django DB)
- **Authentication**: Django’s built-in User model

---

## How to Use

1. **Clone the Repository**  
   `git clone https://github.com/your-username/news-platform.git`

2. **Create Virtual Environment**  
   `python -m venv venv && source venv/bin/activate`  
   _(On Windows: `venv\Scripts\activate`)_

3. **Install Requirements**  
   `pip install -r requirements.txt`

4. **Apply Migrations**  
   `python manage.py migrate`

5. **Create Superuser**  
   `python manage.py createsuperuser`

6. **Run Server**  
   `python manage.py runserver`  
   Open [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Conclusion
This Django News Publishing Platform is a secure, clean, and customizable solution for managing news articles with user-level access control. Whether you're an admin managing public content or a user writing personal articles, the system is designed to be simple and effective.

> **Project developed by Mushafina R** as part of a Django learning and development project.

---
