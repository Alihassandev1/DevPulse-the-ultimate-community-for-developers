# DevPulse 🚀

DevPulse is a community-driven platform built for developers to share insights, tutorials, and experiences. It's a space where developers can connect, learn, and grow together.

![DevPulse Homepage](https://raw.githubusercontent.com/Alihassandev1/DevPulse-the-ultimate-community-for-developers/main/screenshots/homepage.png)

## 🎯 About

DevPulse aims to create a clean, focused environment where developers can:
- Share technical tutorials and guides
- Post insights and learnings from their projects
- Connect with other developers
- Build a portfolio of their knowledge contributions
- Stay updated with trending topics in the dev community

## ✨ Features

- **User Authentication**: Secure signup, login, and profile management
- **Post Creation**: Share tutorials, insights, and experiences with rich text and media support
- **Image Uploads**: Attach images to your posts for better explanations
- **User Profiles**: Personalized profiles for each developer
- **Trending Topics**: Stay updated with what developers are talking about
- **Topic Tags**: Categorize posts with tags like Python, DevOps, Frontend, etc.
- **Modern UI**: Clean, dark-themed interface with a focus on content and readability
- **Responsive Design**: Works seamlessly across devices

![DevPulse Posts Feed](https://raw.githubusercontent.com/Alihassandev1/DevPulse-the-ultimate-community-for-developers/main/screenshots/posts-feed.png)

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS
- **Database**: SQLite (default Django DB)
- **Package Manager**: UV (modern Python package manager)

## 📦 Installation

### Prerequisites
- Python 3.8+
- UV package manager (recommended) or pip

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/Alihassandev1/DevPulse-the-ultimate-community-for-developers.git
cd DevPulse-the-ultimate-community-for-developers
```

2. **Install dependencies**

Using UV (recommended):
```bash
uv sync
```

Or using pip:
```bash
pip install -r requirements.txt
```

3. **Run migrations**
```bash
python manage.py migrate
```

4. **Create a superuser (optional)**
```bash
python manage.py createsuperuser
```

5. **Run the development server**
```bash
python manage.py runserver
```

6. **Access the application**
Open your browser and navigate to `http://127.0.0.1:8000`

## 📁 Project Structure

```
DevPulse/
├── DevPulse/          # Main project settings
├── post/              # Post app (create, read posts)
├── user/              # User app (authentication, profiles)
├── templates/         # HTML templates
├── static/            # CSS, JS, images
├── media/             # User uploaded content
├── manage.py          # Django management script
└── pyproject.toml     # Project dependencies
```

## 🚀 Usage

1. **Register an account** or login if you already have one
2. **Create posts** to share your insights, tutorials, or experiences
3. **Upload images** to make your posts more engaging
4. **Browse content** from other developers in the community
5. **Follow trending topics** to stay updated with the latest discussions

## 📸 Screenshots

### Homepage
![DevPulse Homepage](https://raw.githubusercontent.com/Alihassandev1/DevPulse-the-ultimate-community-for-developers/main/screenshots/homepage.png)

### Posts Feed
![Posts Feed](https://raw.githubusercontent.com/Alihassandev1/DevPulse-the-ultimate-community-for-developers/main/screenshots/posts-feed.png)

## 🤝 Contributing

Contributions are welcome! This project is in active development, and there's plenty of room for improvement.

### How to contribute:
1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some feature'`)
5. Push to the branch (`git push origin feature/your-feature`)
6. Open a Pull Request

## 📝 Roadmap

- [ ] Create interactive user profiles
- [ ] Add feature to customize new posts using [ckeditor](https://ckeditor.com/)
- [ ] Add commenting and likes system
- [ ] User follow/following system
- [ ] Markdown support for posts
- [ ] Code syntax highlighting
- [ ] Notifications

## 🐛 Known Issues

This project is in active development. If you encounter any bugs or have suggestions, please open an issue on GitHub.

## 📄 License

This project is open source and available.

## 👤 Author

**Ali Hassan**
- GitHub: [@Alihassandev1](https://github.com/Alihassandev1)

## 🙏 Acknowledgments

Built with passion for the developer community. Special thanks to everyone who contributes and provides feedback.

---

⭐ If you find this project useful, consider giving it a star on GitHub!

**DevPulse** - *Where developers connect and grow together*