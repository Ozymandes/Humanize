# 🚀 Quick Deployment Guide

## Option 1: Share with Friends (Easiest - Render.com)

### Step 1: Push to GitHub
```bash
git init
git add .
git commit -m "Initial commit"
# Create a new repo on GitHub first, then:
git remote add origin https://github.com/YOUR_USERNAME/text-humanizer.git
git push -u origin main
```

### Step 2: Deploy to Render (5 minutes, FREE)
1. Go to https://render.com
2. Sign up/login (GitHub login works best)
3. Click "New +" → "Web Service"
4. Connect your GitHub repo
5. Click "Deploy Web Service"
6. That's it! Your app will be live in 2-3 minutes

Your shareable link: `https://text-humanizer.onrender.com`

---

## Option 2: Share on Local Network

1. **Find your local IP**:
   - Windows: Open Command Prompt, type `ipconfig`
   - Look for "IPv4 Address" (e.g., 192.168.1.6)

2. **Share the link**:
   - `http://YOUR-IP:5000`
   - Example: `http://192.168.1.6:5000`

3. **Make sure firewall allows port 5000**:
   - Windows Settings → Update & Security → Windows Security
   - → Firewall & network protection → Advanced settings
   - → Inbound Rules → New Rule → Port → 5000

---

## Option 3: Quick Test (Local Only)

### Windows:
Double-click `run.bat`

### Or manually:
```bash
python app.py
```

Then open: http://localhost:5000

---

## ✅ Your App Features

- ✅ Upload .txt, .pdf, or .docx files
- ✅ Returns same format (PDF in, PDF out)
- ✅ Preserves formatting
- ✅ Beautiful drag-and-drop interface
- ✅ No installation needed for users (when deployed)
- ✅ Works on mobile devices
- ✅ Shareable link

---

## 🎯 Quick Test

1. Open http://localhost:5000
2. Upload any document
3. Click "Humanize File"
4. Download your humanized document!

---

## 📱 Share Your App

Once deployed to Render:
1. Copy your app's URL
2. Share with anyone
3. They can use it immediately!
4. Works on any device with a browser

---

## 🔧 Troubleshooting

**Port 5000 already in use?**
```bash
# Windows - Find and kill process
netstat -ano | findstr :5000
taskkill /PID <PID_NUMBER> /F
```

**Dependencies missing?**
```bash
pip install -r requirements.txt
```

**Firewall blocking?**
- Temporarily disable firewall to test
- Or add rule for port 5000

---

## 💡 Tips

- **First deployment to Render takes 2-3 minutes**
- **Subsequent deployments take ~1 minute**
- **Render free tier includes:**
  - 750 hours/month
  - 512 MB RAM
  - Enough for personal use and sharing with friends!

---

**Made with ❤️ - Your app is ready to share!**
