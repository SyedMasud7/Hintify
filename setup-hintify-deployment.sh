#!/bin/bash

echo "🚀 Setting up Hintify for deployment..."
echo ""

# Check if Hintify directory exists
if [ ! -d "../Hintify" ]; then
    echo "❌ Error: Hintify directory not found at ../Hintify"
    echo "Please make sure your Hintify project is in the parent directory."
    exit 1
fi

echo "✅ Found Hintify directory"
echo ""

# Copy deployment files
echo "📦 Copying deployment files..."
cp hintify-render.yaml ../Hintify/render.yaml
cp hintify-Procfile ../Hintify/Procfile
cp hintify-railway.json ../Hintify/railway.json
cp hintify-runtime.txt ../Hintify/runtime.txt

echo "✅ Deployment files copied successfully!"
echo ""

echo "📝 Files created in Hintify directory:"
echo "   - render.yaml (for Render.com)"
echo "   - Procfile (for Heroku/Railway)"
echo "   - railway.json (for Railway.app)"
echo "   - runtime.txt (Python version)"
echo ""

echo "🎯 Next Steps:"
echo ""
echo "1. Go to Hintify directory:"
echo "   cd ../Hintify"
echo ""
echo "2. Commit the changes:"
echo "   git add ."
echo "   git commit -m 'Add deployment configuration'"
echo "   git push origin main"
echo ""
echo "3. Deploy on Render.com:"
echo "   - Go to https://render.com"
echo "   - Sign up with GitHub"
echo "   - Click 'New +' → 'Blueprint'"
echo "   - Select your Hintify repository"
echo "   - Click 'Apply'"
echo ""
echo "4. Add environment variables in Render dashboard:"
echo "   - OPENAI_API_KEY"
echo "   - DEEPSEEK_API_KEY (optional)"
echo ""
echo "5. Wait 5-10 minutes for deployment"
echo ""
echo "🎉 Your Hintify will be live and accessible to everyone!"
echo ""
echo "📖 For detailed instructions, read: DEPLOY_HINTIFY_NOW.md"
