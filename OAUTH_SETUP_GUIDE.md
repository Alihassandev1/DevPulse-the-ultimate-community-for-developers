# OAuth Setup Guide for DevPulse

This guide will walk you through setting up Google and GitHub OAuth authentication for your DevPulse application.

## Prerequisites
- Your Django app must be running
- You need admin access to your Django admin panel
- You'll need accounts on Google Cloud Console and GitHub

---

## Part 1: Setup Google OAuth

### Step 1: Create Google OAuth Credentials

1. **Go to Google Cloud Console**
   - Visit: https://console.cloud.google.com/
   - Sign in with your Google account

2. **Create a New Project** (or select existing)
   - Click the project dropdown at the top
   - Click "NEW PROJECT"
   - Name it "DevPulse" (or your preferred name)
   - Click "CREATE"

3. **Enable Google+ API**
   - In the left sidebar, go to "APIs & Services" > "Library"
   - Search for "Google+ API"
   - Click on it and click "ENABLE"

4. **Create OAuth Credentials**
   - Go to "APIs & Services" > "Credentials"
   - Click "CREATE CREDENTIALS" > "OAuth client ID"
   - If prompted, configure the OAuth consent screen:
     - User Type: External
     - App name: DevPulse
     - User support email: your email
     - Developer contact: your email
     - Click "SAVE AND CONTINUE"
     - Scopes: Skip (click "SAVE AND CONTINUE")
     - Test users: Add your email for testing
     - Click "SAVE AND CONTINUE"

5. **Configure OAuth Client**
   - Application type: "Web application"
   - Name: "DevPulse Web Client"
   - Authorized JavaScript origins:
     - `http://localhost:8000`
     - `http://127.0.0.1:8000`
   - Authorized redirect URIs:
     - `http://localhost:8000/accounts/google/login/callback/`
     - `http://127.0.0.1:8000/accounts/google/login/callback/`
   - Click "CREATE"

6. **Save Your Credentials**
   - Copy the **Client ID** (looks like: `xxxxx.apps.googleusercontent.com`)
   - Copy the **Client Secret**
   - Keep these safe! You'll need them soon

---

## Part 2: Setup GitHub OAuth

### Step 1: Create GitHub OAuth App

1. **Go to GitHub Settings**
   - Visit: https://github.com/settings/developers
   - Or: GitHub Profile > Settings > Developer settings > OAuth Apps

2. **Create New OAuth App**
   - Click "New OAuth App"
   - Fill in the details:
     - **Application name**: DevPulse
     - **Homepage URL**: `http://localhost:8000`
     - **Application description**: DevPulse web application (optional)
     - **Authorization callback URL**: `http://127.0.0.1:8000/accounts/github/login/callback/`
   - Click "Register application"

3. **Generate Client Secret**
   - After registration, you'll see your **Client ID**
   - Click "Generate a new client secret"
   - Copy the **Client Secret** (you won't be able to see it again!)

4. **Save Your Credentials**
   - Copy the **Client ID**
   - Copy the **Client Secret**
   - Keep these safe!

---

## Part 3: Configure Django Admin

### Step 1: Access Django Admin

1. **Start your Django server** (if not running):
   ```powershell
   uv run python manage.py runserver
   ```

2. **Go to Django Admin**:
   - Visit: http://127.0.0.1:8000/admin/
   - Login with your superuser credentials

3. **If you don't have a superuser**, create one:
   ```powershell
   uv run python manage.py createsuperuser
   ```
   - Enter username, email, and password

### Step 2: Add Google Social App

1. **Navigate to Social Applications**:
   - In Django admin, find "Sites" > "Social applications"
   - Click "Add Social Application"

2. **Fill in Google Details**:
   - **Provider**: Google
   - **Name**: Google (or any name you prefer)
   - **Client id**: Paste your Google Client ID
   - **Secret key**: Paste your Google Client Secret
   - **Key**: Leave empty
   - **Sites**: Select "example.com" and click the arrow to move it to "Chosen sites"
   - Click "SAVE"

### Step 3: Add GitHub Social App

1. **Add Another Social Application**:
   - Click "Add Social Application" again

2. **Fill in GitHub Details**:
   - **Provider**: GitHub
   - **Name**: GitHub (or any name you prefer)
   - **Client id**: Paste your GitHub Client ID
   - **Secret key**: Paste your GitHub Client Secret
   - **Key**: Leave empty
   - **Sites**: Select "example.com" and move to "Chosen sites"
   - Click "SAVE"

---

## Part 4: Test Your Setup

### Test Google Login

1. **Navigate to Signup Page**:
   - Visit: http://127.0.0.1:8000/user/signup/

2. **Click "Continue with Google"**:
   - You should be redirected to Google's login page
   - Select your Google account
   - Grant permissions
   - You should be redirected back to your app and logged in!

### Test GitHub Login

1. **Navigate to Signup Page** (or logout first):
   - Visit: http://127.0.0.1:8000/user/signup/

2. **Click "Continue with GitHub"**:
   - You should be redirected to GitHub's authorization page
   - Click "Authorize"
   - You should be redirected back and logged in!

---

## Troubleshooting

### Common Issues:

1. **"SocialApp.DoesNotExist" error**:
   - Make sure you've added both social apps in Django admin
   - Check that you've selected the correct site in "Chosen sites"

2. **"Redirect URI mismatch" error**:
   - Double-check your callback URLs match exactly:
     - Google: `http://127.0.0.1:8000/accounts/google/login/callback/`
     - GitHub: `http://127.0.0.1:8000/accounts/github/login/callback/`
   - Make sure there are no trailing slashes missing

3. **Google shows "This app isn't verified"**:
   - This is normal for development
   - Click "Advanced" > "Go to DevPulse (unsafe)" to continue
   - For production, you'll need to verify your app

4. **Can't access Django admin**:
   - Create a superuser: `uv run python manage.py createsuperuser`
   - Make sure your server is running

---

## For Production Deployment

When deploying to production (e.g., Heroku, AWS, etc.):

1. **Update OAuth Settings**:
   - Add your production domain to authorized origins/redirect URIs
   - Example: `https://devpulse.com/accounts/google/login/callback/`

2. **Update Django Sites Framework**:
   - In Django admin, update the site domain from "example.com" to your actual domain

3. **Verify Google App**:
   - Submit your app for verification in Google Cloud Console
   - This removes the "unverified app" warning

4. **Use Environment Variables**:
   - Don't hardcode Client IDs/Secrets
   - Store them in environment variables

---

## Need Help?

If you're still having issues:
1. Check the Django server logs for detailed error messages
2. Verify all credentials are copied correctly (no extra spaces)
3. Make sure the callback URLs match exactly (including http:// and trailing slashes)

Happy coding! 🚀
