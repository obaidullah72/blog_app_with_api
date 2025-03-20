# 📝 BlogSphere

**BlogSphere** is a minimalistic and elegant **blogging platform** built with **Django** and **Django REST Framework (DRF)**. The platform allows users to create, read, update, and delete blog posts. It also includes a commenting system, user authentication, and RESTful API endpoints to interact with blog data programmatically.

---

## 🚀 Features

- 🔐 **User Authentication** (Login & Logout)
- ✍️ **Create, Read, Update, Delete (CRUD)** blog posts (authenticated users only)
- 💬 **Commenting System** (supports authenticated and anonymous users)
- 📄 **Pagination** on the blog post listing page
- 🔗 **REST API Endpoints** for BlogPosts and Comments
- 🔒 **Permissions & Access Control**
- 🖥️ **Basic Frontend Templates** with Django Templating Language (DTL)
  
---

## 🛠️ Tech Stack

- **Backend**: Django 4+, Django REST Framework
- **Database**: SQLite (default, can be changed)
- **Frontend**: HTML, CSS (Bootstrap optional)
- **Authentication**: Django's built-in user system

---

## 📂 Project Structure

```
BlogSphere/
├── blog/                  # Django app: views, models, serializers, templates
│   ├── migrations/
│   ├── templates/
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── blog_detail.html
│   │   ├── blog_create.html
│   │   ├── blog_update.html
│   │   └── blog_delete.html
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
├── BlogSphereProject/     # Django project settings and URLs
├── manage.py
└── README.md
```

---

## 🔑 User Authentication

| Function   | URL        | Description                    |
|------------|------------|--------------------------------|
| Login      | `/login/`  | Authenticates a user and redirects to the blog list |
| Logout     | `/logout/` | Logs out the user and redirects to the blog list |

---

## 📝 Blog Post Functionality

| Function        | URL                        | Access             | Description                                           |
|-----------------|----------------------------|--------------------|-------------------------------------------------------|
| List Posts      | `/`                        | Public             | Lists all blog posts with pagination (5 per page)     |
| View Post       | `/blog/<pk>/`              | Public             | Displays a single post and its comments               |
| Create Post     | `/blog/create/`            | Authenticated User | Allows creating a new blog post                       |
| Update Post     | `/blog/update/<pk>/`       | Author Only        | Allows the author to update their blog post           |
| Delete Post     | `/blog/delete/<pk>/`       | Author Only        | Allows the author to delete their blog post           |

---

## 💬 Commenting System

- Comment on blog posts directly from the detail page.
- Authenticated users have their comments linked to their accounts.
- Anonymous users can also comment (author remains `None`).

---

## 📡 RESTful API Endpoints

| Endpoint                | Methods | Description                         |
|-------------------------|---------|-------------------------------------|
| `/api/blogposts/`       | GET     | List all blog posts                 |
| `/api/blogposts/`       | POST    | Create a new post (authenticated users only) |
| `/api/blogposts/<pk>/`  | GET     | Retrieve a blog post                |
| `/api/blogposts/<pk>/`  | PUT     | Update a blog post (author only)    |
| `/api/blogposts/<pk>/`  | DELETE  | Delete a blog post (author only)    |
| `/api/comments/`        | GET     | List all comments                   |
| `/api/comments/`        | POST    | Create a new comment (authenticated users only) |

---

## 🔒 Permissions and Access Control

- Only authenticated users can:
  - Create blog posts
  - Edit or delete their own posts
  - Comment via API endpoints
- Anonymous users can:
  - View blog posts
  - Comment via the frontend (no author)

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/obaidullah72/BlogSphere.git
cd BlogSphere
```

### 2. Create and activate a virtual environment
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install the dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply migrations
```bash
python manage.py migrate
```

### 5. Create a superuser (optional, for admin access)
```bash
python manage.py createsuperuser
```

### 6. Run the server
```bash
python manage.py runserver
```

---

## 🖼️ Templates Overview

| Template           | Purpose                               |
|--------------------|---------------------------------------|
| `index.html`       | Lists paginated blog posts            |
| `login.html`       | User login page                       |
| `blog_detail.html` | Displays post details and comment form |
| `blog_create.html` | Form for creating a new post          |
| `blog_update.html` | Form for editing an existing post     |
| `blog_delete.html` | Confirmation page for deleting a post |

---

## 🛠️ Example API Usage (via `curl` or Postman)

### Get Blog Posts
```http
GET /api/blogposts/
```

### Create Blog Post (Authenticated)
```http
POST /api/blogposts/
Authorization: Token <your_token>

{
  "title": "My New Blog Post",
  "content": "This is the content of the blog post."
}
```

---

## 📌 Upcoming Features (TODO)

- ✅ User registration and profile management
- ✅ Like/Dislike feature on posts
- ✅ JWT Authentication for APIs
- ✅ UI enhancements with Bootstrap/Tailwind CSS
- ✅ Image upload functionality for posts
- ✅ Search and filter posts by category/tags

---

## 🙌 Contribution Guidelines

Contributions are welcome!  
1. Fork the repository  
2. Create your feature branch: `git checkout -b feature/your-feature`  
3. Commit your changes: `git commit -m 'Add your feature'`  
4. Push to the branch: `git push origin feature/your-feature`  
5. Open a pull request  

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).

---

## 📬 Contact & Support

- GitHub: [obaidullah72](https://github.com/obaidullah72)
- LinkedIn: [obaidullah72](https://www.linkedin.com/in/obaidullah72/)
- Email: obaidullah3372@gmail.com

---

[![Visitor Count](https://visitcount.itsvg.in/api?id=obaidullah72&label=Project%20Views&color=6&icon=2&pretty=true)](https://visitcount.itsvg.in)
