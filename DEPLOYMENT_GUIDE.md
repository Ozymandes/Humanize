# 🚀 Deploy Your Humanizer App to Render (Free Hosting)

This guide will help you deploy your Text Humanizer web app so anyone can use it via a shareable link.

---

## 📋 Prerequisites

- GitHub account (free)
- Render account (free tier available)
- Your Humanizer app code

---

## 📤 Step 1: Prepare Your Code for GitHub

### 1.1 Create a `.gitignore` file
This file already exists in your project! It ensures unnecessary files aren't uploaded.

### 1.2 Create a `requirements.txt` file
This file already exists! It contains all the Python dependencies.

### 1.3 Create deployment configuration files
These files already exist in your project:
- `runtime.txt` - Specifies Python version
- `Procfile` - Tells Render how to run your app
- `render.yaml` - Render-specific configuration

**Your project is deployment-ready! ✅**

---

## 📤 Step 2: Push Your Code to GitHub

### 2.1 Create a New Repository on GitHub

1. Go to **https://github.com** and log in
2. Click the **+** icon in the top-right corner
3. Select **"New repository"**
4. Fill in the details:
   - **Repository name**: `humanizer-app` (or your preferred name)
   - **Description**: `AI Text Humanizer - Make text feel natural`
   - **Visibility**: ☑️ Private (recommended) or Public
5. **DO NOT** check any of the initialization boxes
6. Click **"Create repository"**

### 2.2 Upload Your Files to GitHub

**Option A: Using GitHub Website (Easiest)**
1. On your new repository page, click **"uploading an existing file"**
2. Drag and drop these files/folders:
   - `app.py`
   - `noisy_humanize.py`
   - `requirements.txt`
   - `runtime.txt`
   - `Procfile`
   - `render.yaml`
   - `.gitignore`
   - `templates/` folder (drag the whole folder)
   - `README.md` (if you want documentation)
3. Add commit message: `Initial commit`
4. Click **"Commit changes"**

**Option B: Using Git Command Line (More Professional)**
```bash
# Open terminal/command prompt in your project folder
cd C:\Users\yasee\OneDrive\Desktop\Humanize

# Initialize git repository
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit - Text Humanizer App"

# Rename branch to main (if needed)
git branch -M main

# Add your GitHub repository (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/humanizer-app.git

# Push to GitHub
git push -u origin main
```

---

## 🌐 Step 3: Deploy to Render

### 3.1 Sign Up/Login to Render

1. Go to **https://render.com**
2. Click **"Sign Up"** or **"Get Started"**
3. **Sign up with GitHub** (recommended - it's free and connects your account)
4. Authorize Render to access your GitHub repositories

### 3.2 Create a New Web Service

1. On Render dashboard, click **"New +"** → **"Web Service"**
2. You'll see your GitHub repositories listed
3. Find and click on your **`humanizer-app`** repository
4. Render will automatically detect your Python Flask app

### 3.3 Configure Deployment

Render will show you these settings:

**Name**: `humanizer-app` (or customize)

**Region**: Choose a region close to your users (default is fine)

**Branch**: `main` (should be selected automatically)

**Runtime**: `Python 3` (should be auto-detected)

**Build Command**: Leave as default (Render will use `pip install -r requirements.txt`)

**Start Command**: Should auto-detect as `python app.py`

**Instance Type**: **"Free"** (perfect for personal use!)

### 3.4 Deploy!

1. Click **"Create Web Service"**
2. Render will start deploying your app
3. **This takes 2-5 minutes** for the first deployment
4. You'll see a live log of the deployment process
5. Wait for the status to change to **"Live"** 🎉

---

## 🎉 Step 4: Access Your Live App!

Once deployment is complete:

1. Your app URL will be: **`https://humanizer-app.onrender.com`**
   (Or your custom name: `https://YOUR-APP-NAME.onrender.com`)

2. **Click on your app name** in the Render dashboard to see:
   - Your app's URL
   - Deployment logs
   - Status indicators
   - Metrics

---

## 📤 Step 5: Share Your App!

Now you can share your app with anyone:

**Share the link:**
```
https://humanizer-app.onrender.com
```

**Or customize your domain (optional):**
1. Go to your app settings in Render
2. Click **"Custom Domains"**
3. Add your own domain name (if you have one)

---

## 🔄 Step 6: Updating Your App

When you make changes to your code:

**Using Git (Recommended):**
```bash
cd C:\Users\yasee\OneDrive\Desktop\Humanize
git add .
git commit -m "Updated feature description"
git push
```
Render will **automatically detect changes** and redeploy!

**Manual Upload:**
1. Go to your GitHub repository
2. Click **"Add file"** → **"Upload files"**
3. Upload changed files
4. Render will auto-deploy

---

## 💰 Costs

**Render Free Tier includes:**
- ✅ 750 hours per month
- ✅ 512 MB RAM
- ✅ 0.1 CPU
- ✅ Enough for personal use and sharing with friends!

**Paid plans start at $7/month** if you need more resources.

---

## 🔧 Troubleshooting

**App won't start?**
- Check the Render logs (click your app → "Logs")
- Common issue: Missing dependencies
- Solution: Make sure `requirements.txt` includes all packages

**Can't access your app?**
- Check the deployment status in Render dashboard
- Wait 5-10 minutes after first deployment
- Try the URL in incognito mode

**Deployment failed?**
- Check the "Build Logs" in Render
- Make sure all files are uploaded correctly
- Verify `app.py` is in the repository root

---

## ✅ Deployment Checklist

- [ ] GitHub repository created
- [ ] All files uploaded (app.py, noisy_humanize.py, templates/, requirements.txt, Procfile, runtime.txt, render.yaml)
- [ ] Render account created and connected to GitHub
- [ ] Web service deployed successfully
- [ ] App URL works: `https://humanizer-app.onrender.com`
- [ ] Test the app by entering some text and clicking "Humanize"

---

## 🎯 Quick URL to Share

Once deployed, share this with your friends:

**Your Humanizer App:**
```
https://humanizer-app.onrender.com
```

They can:
- ✅ Paste text directly
- ✅ Upload .txt files (loads into editor)
- ✅ Upload .pdf/.docx files (auto-humanizes and downloads)
- ✅ Use the Clean button to remove filler words
- ✅ Copy or download humanized text
- ✅ No installation needed!

---

**🚀 Your Text Humanizer is now live and shareable!**
