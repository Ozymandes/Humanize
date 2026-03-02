# Text Humanizer Web App 🎭

A beautiful, cloud-ready web application that transforms AI-generated text into natural, human-sounding prose. **Supports PDF, Word (.docx), and plain text files** with proper formatting preservation.

## ✨ Features

- **Multiple File Formats**: Upload .txt, .pdf, or .docx files
- **Format Preservation**: Returns files in the same format as uploaded
- **Dual Input Methods**: Upload files or paste text directly
- **Drag & Drop Upload**: Intuitive file upload with drag-and-drop support
- **Real-time Processing**: Fast text humanization with immediate results
- **Beautiful UI**: Modern, responsive design with smooth animations
- **Shareable Link**: Deploy to cloud and share with anyone
- **Customizable Seeds**: Optional seed parameter for reproducible results

## 🔧 What It Does

The humanizer adds natural human characteristics to text:
- **Natural Typos**: Adds realistic, minor typos (≈1.5% of words)
- **Conversations**: Includes contractions (don't, can't, it's, etc.)
- **Filler Words**: Adds natural conversation starters (And, But, Actually, etc.)
- **Personal Asides**: Inserts personal phrases (I think, I believe, etc.)
- **Varied Structure**: Mixes up sentence length and structure

## 🚀 Quick Start - Local

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the app**:
   ```bash
   python app.py
   ```

3. **Open your browser**:
   Navigate to `http://localhost:5000`

## ☁️ Deploy to Cloud (Shareable Link)

### Option 1: Render (Recommended - Free & Easy)

1. **Create a GitHub repository** with your files
2. **Go to [render.com](https://render.com)**
3. **Click "New +" → "Web Service"**
4. **Connect your GitHub repository**
5. **Render will automatically detect the Python app**
6. **Click "Deploy"** - that's it!

Your app will be live at: `https://your-app-name.onrender.com`

### Option 2: PythonAnywhere (Free Tier)

1. **Sign up at [pythonanywhere.com](https://www.pythonanywhere.com)**
2. **Create a new Web app**
3. **Choose "Flask" as the framework**
4. **Upload your files or connect to GitHub**
5. **PythonAnywhere will configure everything automatically**

Your app will be live at: `https://yourusername.pythonanywhere.com`

### Option 3: Heroku (Free Tier Available)

1. **Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)**
2. **Login to Heroku**:
   ```bash
   heroku login
   ```
3. **Create a new app**:
   ```bash
   heroku create your-app-name
   ```
4. **Deploy**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   heroku git:remote -a your-app-name
   git push heroku main
   ```

Your app will be live at: `https://your-app-name.herokuapp.com`

### Option 4: Railway (Simple & Free)

1. **Go to [railway.app](https://railway.app)**
2. **Click "New Project" → "Deploy from GitHub repo"**
3. **Connect your repository**
4. **Railway will auto-detect Python and deploy**

## 📖 Usage

### Upload a File
1. Click on the "Upload File" tab
2. Drag and drop your file (.txt, .pdf, or .docx)
3. Optionally add a seed number for reproducible results
4. Click "Humanize File"
5. Download your humanized file in the same format!

### Paste Text
1. Click on the "Paste Text" tab
2. Paste your AI-generated text into the text area
3. Optionally add a seed number for reproducible results
4. Click "Humanize Text"
5. Copy or download your humanized text!

## 🌐 Sharing with Friends

Once deployed to the cloud:
1. **Copy your app's URL** (e.g., `https://text-humanizer.onrender.com`)
2. **Share the link** with anyone
3. **They can use it immediately** - no installation needed!

### Local Network Sharing
For local sharing (same WiFi network):
1. **Find your local IP**:
   - Windows: `ipconfig` (look for IPv4 Address)
   - Mac/Linux: `ifconfig` or `ip addr show`
2. **Share the URL**: `http://YOUR-LOCAL-IP:5000`
3. **Make sure port 5000 is allowed** in your firewall

## 🛠️ Technical Details

- **Backend**: Flask (Python)
- **Frontend**: Vanilla HTML/CSS/JavaScript
- **File Processing**:
  - PDF: PyMuPDF (fitz) for reading, ReportLab for writing
  - Word: python-docx for reading and writing
  - Text: Built-in Python file handling
- **File Size Limit**: 50MB
- **Supported Formats**: .txt, .pdf, .docx
- **Default Port**: 5000

## 💡 Tips for Best Results

- Works best with AI-generated text that feels too perfect
- The seed parameter is great for testing different variations
- Longer texts show more noticeable humanization effects
- Run multiple times with different seeds for variations
- PDF/Word files preserve original formatting

## 🔒 Privacy & Security

- All processing happens on the server
- Files are automatically deleted after processing
- No data is stored permanently
- Safe to use with sensitive content
- For maximum privacy, use local deployment

## 📋 File Format Support

| Format | Read | Write | Formatting |
|--------|------|-------|------------|
| .txt   | ✅   | ✅    | Plain text |
| .pdf   | ✅   | ✅    | Preserved |
| .docx  | ✅   | ✅    | Preserved |

## 🐛 Troubleshooting

**App won't start?**
- Make sure all dependencies are installed: `pip install -r requirements.txt`
- Check if port 5000 is already in use
- Try running on a different port: `PORT=8000 python app.py`

**PDF/Word upload fails?**
- Ensure files are not corrupted
- Check file size is under 50MB
- Verify the files are not password-protected

**Missing dependencies error?**
```bash
pip install --upgrade -r requirements.txt
```

**Can't access from other devices?**
- Make sure your firewall allows connections on port 5000
- Use your local IP address, not localhost
- For cloud deployment, check your service's security settings

## 📦 Dependencies

- **Flask**: Web framework
- **python-docx**: Word document processing
- **PyMuPDF**: PDF reading
- **ReportLab**: PDF generation
- **Werkzeug**: WSGI utility library

## 💻 Command Line Usage

You can also use the original Python script directly:

```bash
python noisy_humanize.py your_text.txt
# Output: your_text_clean.txt
```

With a seed for reproducible results:
```bash
python noisy_humanize.py your_text.txt --seed 42
```

## 🎯 Use Cases

- **Students**: Make AI-assisted writing feel more natural
- **Content Creators**: Add human touch to AI-generated content
- **Writers**: Break up uniform AI writing patterns
- **Researchers**: Humanize literature reviews or summaries
- **Professionals**: Make AI-written emails feel more personal

## 🚀 Deployment Platforms Tested

✅ Render (Recommended)
✅ PythonAnywhere
✅ Heroku
✅ Railway
✅ Replit

## 📄 License

Free to use and share. Enjoy making AI text feel more human!

## 🙏 Credits

Built with ❤️ using Flask and vanilla JavaScript. The humanization algorithm adds subtle human touches while preserving meaning and formatting.

---

**Made with ❤️ for better human-AI collaboration**

**Need help?** The app is designed to be self-explanatory. Just upload your file and click "Humanize"!
