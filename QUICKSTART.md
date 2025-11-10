# 🚀 Hintify Professional - Quick Start Guide

## ⚡ 30-Second Start

```bash
cd hintify-professional
./start.sh
```

Then open: **http://localhost:8000**

---

## 🎯 What You Can Do

### 1. Take a Test (Curated Questions)
- Click **"Take Test"**
- Choose subject: Technology, Science, Geography, or General Knowledge
- Select difficulty: Easy, Medium, or Hard
- Answer 15 questions
- Get hints when stuck
- See immediate feedback

### 2. Upload Documents (Generate Questions)
- Click **"Upload"**
- Select a subject
- Upload PDF, DOCX, or PPTX file
- System generates **45 questions** automatically:
  - 15 Easy
  - 15 Medium
  - 15 Hard
- Each with hints and explanations

---

## 📊 What's Available

**Curated Questions:**
- 💻 Technology: 45 questions
- 🔬 Science: 45 questions
- 🌍 Geography: 45 questions
- 📚 General Knowledge: 45 questions

**Total: 180 questions ready to use!**

---

## 🌐 URLs

| What | URL |
|------|-----|
| **App** | http://localhost:8000 |
| **API Docs** | http://localhost:8000/docs |
| **Health** | http://localhost:8000/api/health |

---

## ⌨️ Keyboard Shortcuts

While taking a test:
- `N` - Next question
- `P` - Previous question
- `S` - Submit answer
- `H` - Get hint
- `1-4` - Select option A-D

---

## 🎨 Features

- ✅ Glassmorphism UI
- ✅ Animated particle background
- ✅ Dark/Light theme toggle
- ✅ Drag & drop file upload
- ✅ Responsive design
- ✅ AI-powered hints
- ✅ Instant feedback

---

## 🔧 Commands

```bash
# Start server
./start.sh
# or
make dev

# Run tests
./test_system.sh

# Reset database
make reset-db

# Seed database
make seed
```

---

## 📖 Documentation

- `README.md` - Full setup guide
- `SUCCESS.md` - Build summary
- `COMPLETE.md` - Feature list
- `FINAL_STATUS.md` - Detailed status

---

## 🤖 AI Configuration (Optional)

Edit `backend/.env`:

```bash
# Use fallback (no API key needed)
AI_PROVIDER=fallback

# Or use OpenAI
AI_PROVIDER=openai
AI_API_KEY=your-key-here
AI_MODEL=gpt-3.5-turbo

# Or use DeepSeek
AI_PROVIDER=deepseek
AI_API_KEY=your-key-here
AI_MODEL=deepseek-chat
```

**Default: Fallback provider (works without API key!)**

---

## 🎓 Example Use Cases

### Student
1. Open app
2. Select "Technology" → "Easy"
3. Answer 15 questions
4. Use hints when stuck
5. Learn from explanations

### Teacher
1. Open app
2. Click "Upload"
3. Upload course material PDF
4. Get 45 auto-generated questions
5. Review and use in class

### Self-Learner
1. Upload study materials
2. Generate practice questions
3. Test yourself
4. Track progress

---

## ✅ System Status

**All Tests Passing: 9/9**

```
✓ Health Check
✓ Subjects API
✓ Questions API
✓ Frontend HTML
✓ API Documentation
✓ Subject Count
✓ Question Count
✓ Question Distribution
✓ Difficulty Distribution
```

---

## 🎉 You're Ready!

**Hintify Professional is running and ready to use!**

Open http://localhost:8000 and start learning! 🚀

---

**Version**: 2.0.0  
**Status**: ✅ Production Ready  
**Last Updated**: November 7, 2025
