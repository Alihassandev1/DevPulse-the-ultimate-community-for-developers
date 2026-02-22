# DevPulse 🚀
**DevPulse** is a community-driven platform for developers to share tutorials, insights, and real-world experiences in a clean, distraction-free environment.

> A place where developers **connect, learn, and grow together**.

![DevPulse Homepage](https://raw.githubusercontent.com/Alihassandev1/DevPulse-the-ultimate-community-for-developers/main/screenshots/homepage.png)

---

## 🎯 Vision
DevPulse is designed to become a **knowledge hub for developers**, enabling them to:

- Share technical tutorials and practical guides  
- Document project learnings and real experiences  
- Connect with other passionate developers  
- Build a public portfolio of knowledge  
- Stay updated with trending discussions in tech  

---

## ✨ Core Features

- 🔐 **Authentication System** — Email-based signup, login, and OAuth with Google & GitHub  
- 📝 **Rich Text Posts** — Create posts with CKEditor for formatted text and rich content  
- 🖼️ **Image Uploads** — Post images and profile pictures for visual explanations  
- 👤 **Developer Profiles** — Personalized profiles with profile pictures and post history  
- 🔍 **Smart Search** — PostgreSQL trigram search to find posts and developers  
- 🌙 **Modern Dark UI** — Clean, readable, developer-friendly design  
- 📱 **Responsive Layout** — Works smoothly on desktop and mobile  

![DevPulse Feed](https://raw.githubusercontent.com/Alihassandev1/DevPulse-the-ultimate-community-for-developers/main/screenshots/feed.png)

---

## 🛠 Tech Stack

| Layer | Technology |
|-------|------------|
| **Backend** | Django 6.0 (Python) |
| **Frontend** | HTML5, CSS3, JavaScript |
| **Database** | PostgreSQL |
| **Rich Text Editor** | CKEditor 5 with file uploads |
| **Authentication** | django-allauth (Email, Google, GitHub OAuth) |
| **Search** | PostgreSQL Full-Text Search (Trigram Similarity) |
| **Package Manager** | UV (modern Python package manager) |

---

## ⚙️ Installation & Setup

### Prerequisites
- **Python** 3.14+  
- **PostgreSQL** 12+ (installed and running locally)
- **UV** package manager (recommended) or `pip`

### 1️⃣ Clone Repository
```bash
git clone https://github.com/Alihassandev1/DevPulse-the-ultimate-community-for-developers.git
cd DevPulse-the-ultimate-community-for-developers
```

### 2️⃣ Create PostgreSQL Database

Open PostgreSQL terminal and create a database:

```sql
createdb devpulse
```

### 3️⃣ Install Dependencies

Using **UV**:

```bash
uv sync
```

Or using **pip**:

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables *(Optional - for OAuth)*

Create a `.env` file in the project root with your OAuth credentials:

```env
DJANGO_SECRET_KEY=your-secret-key-here
GOOGLE_OAUTH_CLIENT_ID=your-google-client-id
GOOGLE_OAUTH_CLIENT_SECRET=your-google-secret
GITHUB_OAUTH_CLIENT_ID=your-github-client-id
GITHUB_OAUTH_CLIENT_SECRET=your-github-secret
```

See [OAUTH_SETUP_GUIDE.md](OAUTH_SETUP_GUIDE.md) for detailed OAuth setup instructions.

### 5️⃣ Apply Migrations

```bash
python manage.py migrate
```

### 6️⃣ Create Admin User *(optional but recommended)*

```bash
python manage.py createsuperuser
```

### 7️⃣ Collect Static Files

```bash
python manage.py collectstatic --noinput
```

### 8️⃣ Run Development Server

```bash
python manage.py runserver
```

### 9️⃣ Open in Browser

```
http://127.0.0.1:8000
```

Visit `http://127.0.0.1:8000/admin` to access the Django admin panel with your superuser credentials.

---

## 📁 Project Structure

```
DevPulse/
├── DevPulse/                # Django project configuration & settings
│   ├── settings.py         # Project settings (apps, auth config, database)
│   ├── urls.py            # Main URL router
│   ├── views.py           # Core views
│   └── forms.py           # Core forms
├── post/                   # Posts app (CRUD operations, search)
│   ├── models.py          # Post & database models
│   ├── views.py           # Post creation, viewing, profiles
│   ├── forms.py           # Post forms
│   └── migrations/        # Database migrations
├── user/                   # Users & Authentication app
│   ├── models.py          # User profile model
│   ├── views.py           # Signup/login views
│   ├── forms.py           # User forms
│   └── migrations/        # Database migrations
├── templates/             # HTML templates
│   ├── post/             # Post-related templates
│   ├── user/             # Auth templates
│   ├── layout/           # Base layout components
│   └── socialaccount/    # OAuth templates
├── static/               # Static files (CSS, JS, Logo)
│   ├── css/
│   ├── js/
│   └── logo/
├── media/                # User-uploaded files
│   ├── post_images/
│   └── profile_image/
├── manage.py
├── pyproject.toml        # Python project configuration
└── README.md
```

---

## 🚀 How to Use

1. **Register or Log In** — Create account with email or OAuth (Google/GitHub)
2. **Verify Email** — Check your inbox for verification link (required)
3. **Set Up Profile** — Add profile picture and complete your developer profile
4. **Create Posts** — Click "New Post" and use CKEditor to write formatted content
5. **Add Media** — Insert images directly in posts or upload post banner images
6. **Search Content** — Use the search bar to find posts by keywords or discover developers
7. **View Profiles** — Click on any post to see creator's profile and recent posts
8. **Share Knowledge** — Share tutorials, insights, and real-world experiences

---

## � Configuration

### OAuth Setup

DevPulse supports **Google** and **GitHub** OAuth for seamless authentication. 

To set up OAuth:
1. Follow [OAUTH_SETUP_GUIDE.md](OAUTH_SETUP_GUIDE.md) for detailed instructions
2. Obtain OAuth credentials from Google and GitHub developer consoles
3. Add them to `settings.py` or environment variables

### Email Configuration

Email verification is required for new signups. Configure your email backend in `settings.py`:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
```

---

## 📝 API & Admin

- **Django Admin**: `http://localhost:8000/admin` — Manage posts, users, and site content
- **Admin Credentials**: Use your superuser account created during setup

---

## �📸 Screenshots

### Homepage

![Homepage](https://raw.githubusercontent.com/Alihassandev1/DevPulse-the-ultimate-community-for-developers/main/screenshots/homepage.png)

### Posts Feed

![Feed](https://raw.githubusercontent.com/Alihassandev1/DevPulse-the-ultimate-community-for-developers/main/screenshots/feed.png)

---

## 🧭 Roadmap

**Completed** ✅
- [x] Email & OAuth authentication (Google, GitHub)
- [x] Rich text editor (CKEditor integration)
- [x] Post creation with image uploads
- [x] User profiles with images
- [x] Smart search functionality
- [x] Developer-friendly responsive design

**In Progress / Coming Soon** 🚀
- [ ] Comments & likes system
- [ ] Follow / following system
- [ ] Real-time notifications
- [ ] User activity feed
- [ ] Post trending algorithm
- [ ] Advanced content filtering

---

## 🌟 Next Steps to Make This Production-Ready

1. **Live Deployment** — Deploy to Heroku, Railway, or AWS
2. **Refined Styling** — Polish UI/UX and add light mode option
3. **Comments & Likes** — Add community engagement features
4. **Email Templates** — Design custom HTML email notifications
5. **Docker Support** — Add Dockerfile for easy deployment
6. **Automated Tests** — Implement unit and integration tests
7. **Performance Optimization** — Add caching and database indexing

---

## 🤝 Contributing

Contributions are welcome and appreciated!

**Steps:**

1. Fork the repo
2. Create a branch

   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit changes
4. Push to GitHub
5. Open a Pull Request

---

## 🐛 Issues

Found a bug or have an idea?
👉 Open an **Issue** in this repository.

---

## 👨‍💻 Author

**Ali Hassan**
GitHub → [Alihassandev1](https://github.com/Alihassandev1)

---

## ⭐ Support

If you like this project, consider **starring the repository** — it really helps!

**DevPulse**
*Where developers connect and grow together.*

