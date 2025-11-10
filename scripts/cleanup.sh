#!/bin/bash

echo "🧹 Hintify Folder Cleanup & Restructuring"
echo "=========================================="
echo ""

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Get the parent directory (Desktop/Hintify)
PARENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )/.." && pwd )"
CURRENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

echo "Parent directory: $PARENT_DIR"
echo "Current directory: $CURRENT_DIR"
echo ""

# Confirm before proceeding
read -p "This will reorganize your Hintify folder. Continue? (y/n) " -n 1 -r
echo ""
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    echo "Cleanup cancelled."
    exit 1
fi

echo ""
echo "Step 1: Removing old Hintify folder..."
if [ -d "$PARENT_DIR/Hintify" ]; then
    rm -rf "$PARENT_DIR/Hintify"
    echo -e "${GREEN}✓${NC} Old Hintify folder removed"
else
    echo -e "${YELLOW}⚠${NC} Old Hintify folder not found (already removed?)"
fi

echo ""
echo "Step 2: Removing test files..."
rm -f "$CURRENT_DIR/test_upload.txt"
echo -e "${GREEN}✓${NC} Test files removed"

echo ""
echo "Step 3: Removing backup files..."
rm -f "$CURRENT_DIR/frontend/index.html.backup"*
rm -f "$CURRENT_DIR/frontend/index.html.v"*
echo -e "${GREEN}✓${NC} Backup files removed"

echo ""
echo "Step 4: Cleaning uploads folder..."
rm -rf "$CURRENT_DIR/backend/uploads"/*
mkdir -p "$CURRENT_DIR/backend/uploads"
echo -e "${GREEN}✓${NC} Uploads folder cleaned"

echo ""
echo "Step 5: Removing .DS_Store files..."
find "$CURRENT_DIR" -name ".DS_Store" -delete
echo -e "${GREEN}✓${NC} .DS_Store files removed"

echo ""
echo "Step 6: Creating organized folder structure..."
mkdir -p "$CURRENT_DIR/docs/setup"
mkdir -p "$CURRENT_DIR/docs/features"
mkdir -p "$CURRENT_DIR/docs/archive"
mkdir -p "$CURRENT_DIR/examples"
mkdir -p "$CURRENT_DIR/scripts"
echo -e "${GREEN}✓${NC} Folder structure created"

echo ""
echo "Step 7: Moving documentation files..."
[ -f "$CURRENT_DIR/ACCEPTANCE_CRITERIA_VERIFICATION.md" ] && mv "$CURRENT_DIR/ACCEPTANCE_CRITERIA_VERIFICATION.md" "$CURRENT_DIR/docs/setup/"
[ -f "$CURRENT_DIR/IMPLEMENTATION_SUMMARY.md" ] && mv "$CURRENT_DIR/IMPLEMENTATION_SUMMARY.md" "$CURRENT_DIR/docs/setup/"
[ -f "$CURRENT_DIR/PROJECT_STATUS.md" ] && mv "$CURRENT_DIR/PROJECT_STATUS.md" "$CURRENT_DIR/docs/setup/"
[ -f "$CURRENT_DIR/ANALYTICS_IMPROVEMENTS.md" ] && mv "$CURRENT_DIR/ANALYTICS_IMPROVEMENTS.md" "$CURRENT_DIR/docs/features/"
[ -f "$CURRENT_DIR/UPLOAD_TESTING_GUIDE.md" ] && mv "$CURRENT_DIR/UPLOAD_TESTING_GUIDE.md" "$CURRENT_DIR/docs/features/"
[ -f "$CURRENT_DIR/UPLOAD_FIX_SUMMARY.md" ] && mv "$CURRENT_DIR/UPLOAD_FIX_SUMMARY.md" "$CURRENT_DIR/docs/features/"
[ -f "$CURRENT_DIR/UPLOADED_QUESTIONS_FIX.md" ] && mv "$CURRENT_DIR/UPLOADED_QUESTIONS_FIX.md" "$CURRENT_DIR/docs/features/"
[ -f "$CURRENT_DIR/CLEANUP_PLAN.md" ] && mv "$CURRENT_DIR/CLEANUP_PLAN.md" "$CURRENT_DIR/docs/"
echo -e "${GREEN}✓${NC} Documentation organized"

echo ""
echo "Step 8: Moving example files..."
[ -f "$CURRENT_DIR/test_document.docx" ] && mv "$CURRENT_DIR/test_document.docx" "$CURRENT_DIR/examples/"
[ -f "$CURRENT_DIR/science_study_guide.docx" ] && mv "$CURRENT_DIR/science_study_guide.docx" "$CURRENT_DIR/examples/"
echo -e "${GREEN}✓${NC} Example files moved"

echo ""
echo "Step 9: Moving scripts..."
[ -f "$CURRENT_DIR/start.sh" ] && mv "$CURRENT_DIR/start.sh" "$CURRENT_DIR/scripts/"
[ -f "$CURRENT_DIR/test_system.sh" ] && mv "$CURRENT_DIR/test_system.sh" "$CURRENT_DIR/scripts/"
[ -f "$CURRENT_DIR/cleanup.sh" ] && cp "$CURRENT_DIR/cleanup.sh" "$CURRENT_DIR/scripts/"
echo -e "${GREEN}✓${NC} Scripts organized"

echo ""
echo "Step 10: Renaming folder to Hintify..."
if [ "$CURRENT_DIR" != "$PARENT_DIR/Hintify" ]; then
    mv "$CURRENT_DIR" "$PARENT_DIR/Hintify"
    echo -e "${GREEN}✓${NC} Folder renamed to Hintify"
    NEW_PATH="$PARENT_DIR/Hintify"
else
    echo -e "${YELLOW}⚠${NC} Already named Hintify"
    NEW_PATH="$CURRENT_DIR"
fi

echo ""
echo "=========================================="
echo -e "${GREEN}✅ Cleanup Complete!${NC}"
echo "=========================================="
echo ""
echo "New structure:"
echo "📁 $NEW_PATH/"
echo "   ├── 📁 backend/          (Backend application)"
echo "   ├── 📁 frontend/         (Frontend application)"
echo "   ├── 📁 docs/             (Documentation)"
echo "   │   ├── 📁 setup/        (Setup docs)"
echo "   │   ├── 📁 features/     (Feature docs)"
echo "   │   └── 📁 archive/      (Old docs)"
echo "   ├── 📁 examples/         (Example files)"
echo "   ├── 📁 scripts/          (Utility scripts)"
echo "   ├── 📁 .venv/            (Python environment)"
echo "   ├── 📄 README.md"
echo "   ├── 📄 QUICKSTART.md"
echo "   ├── 📄 USER_GUIDE.md"
echo "   └── 📄 Makefile"
echo ""
echo "To start the application:"
echo "  cd $NEW_PATH"
echo "  make dev"
echo ""
echo "Then open: http://localhost:8000"
echo ""
