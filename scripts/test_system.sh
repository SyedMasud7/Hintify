#!/bin/bash

# Hintify Professional - System Test Script
# Tests all major functionality

echo "🧪 Testing Hintify Professional System"
echo "========================================"
echo ""

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Test counter
PASSED=0
FAILED=0

# Function to test endpoint
test_endpoint() {
    local name=$1
    local url=$2
    local expected=$3
    
    echo -n "Testing $name... "
    
    response=$(curl -s "$url" 2>/dev/null)
    
    if echo "$response" | grep -q "$expected"; then
        echo -e "${GREEN}✓ PASSED${NC}"
        ((PASSED++))
        return 0
    else
        echo -e "${RED}✗ FAILED${NC}"
        echo "  Expected: $expected"
        echo "  Got: $response"
        ((FAILED++))
        return 1
    fi
}

# Test 1: Health Check
test_endpoint "Health Check" \
    "http://localhost:8000/api/health" \
    "healthy"

# Test 2: Subjects API
test_endpoint "Subjects API" \
    "http://localhost:8000/api/subjects/" \
    "Technology"

# Test 3: Questions API
test_endpoint "Questions API" \
    "http://localhost:8000/api/questions/?subject_id=1&difficulty=EASY&limit=1" \
    "question_text"

# Test 4: Frontend
test_endpoint "Frontend HTML" \
    "http://localhost:8000/" \
    "Hintify"

# Test 5: API Documentation
test_endpoint "API Docs" \
    "http://localhost:8000/docs" \
    "Hintify Professional API"

# Test 6: Count subjects
echo -n "Testing Subject Count... "
subject_count=$(curl -s "http://localhost:8000/api/subjects/" | python3 -c "import sys, json; print(len(json.load(sys.stdin)))" 2>/dev/null)
if [ "$subject_count" = "4" ]; then
    echo -e "${GREEN}✓ PASSED${NC} (4 subjects)"
    ((PASSED++))
else
    echo -e "${RED}✗ FAILED${NC} (Expected 4, got $subject_count)"
    ((FAILED++))
fi

# Test 7: Count questions (API returns max 50 per request, so we'll check if we get 50)
echo -n "Testing Question Count... "
question_count=$(curl -s "http://localhost:8000/api/questions/?subject_id=1&difficulty=EASY&limit=50" | python3 -c "import sys, json; print(len(json.load(sys.stdin)))" 2>/dev/null)
if [ "$question_count" = "15" ]; then
    echo -e "${GREEN}✓ PASSED${NC} (15 easy tech questions)"
    ((PASSED++))
else
    echo -e "${RED}✗ FAILED${NC} (Expected 15, got $question_count)"
    ((FAILED++))
fi

# Test 8: Verify each subject has questions (API limit is 50, so we check for 15 per difficulty)
echo -n "Testing Question Distribution... "
tech_easy=$(curl -s "http://localhost:8000/api/questions/?subject_id=1&difficulty=EASY&limit=50" | python3 -c "import sys, json; print(len(json.load(sys.stdin)))" 2>/dev/null)
science_easy=$(curl -s "http://localhost:8000/api/questions/?subject_id=2&difficulty=EASY&limit=50" | python3 -c "import sys, json; print(len(json.load(sys.stdin)))" 2>/dev/null)
geo_easy=$(curl -s "http://localhost:8000/api/questions/?subject_id=3&difficulty=EASY&limit=50" | python3 -c "import sys, json; print(len(json.load(sys.stdin)))" 2>/dev/null)
gk_easy=$(curl -s "http://localhost:8000/api/questions/?subject_id=4&difficulty=EASY&limit=50" | python3 -c "import sys, json; print(len(json.load(sys.stdin)))" 2>/dev/null)

if [ "$tech_easy" = "15" ] && [ "$science_easy" = "15" ] && [ "$geo_easy" = "15" ] && [ "$gk_easy" = "15" ]; then
    echo -e "${GREEN}✓ PASSED${NC} (15 easy per subject)"
    ((PASSED++))
else
    echo -e "${RED}✗ FAILED${NC}"
    echo "  Technology: $tech_easy (expected 15)"
    echo "  Science: $science_easy (expected 15)"
    echo "  Geography: $geo_easy (expected 15)"
    echo "  General Knowledge: $gk_easy (expected 15)"
    ((FAILED++))
fi

# Test 9: Verify difficulty distribution (API returns max 50, so we check for that)
echo -n "Testing Difficulty Distribution... "
easy_count=$(curl -s "http://localhost:8000/api/questions/?subject_id=1&difficulty=EASY&limit=50" | python3 -c "import sys, json; print(len(json.load(sys.stdin)))" 2>/dev/null)
medium_count=$(curl -s "http://localhost:8000/api/questions/?subject_id=1&difficulty=MEDIUM&limit=50" | python3 -c "import sys, json; print(len(json.load(sys.stdin)))" 2>/dev/null)
hard_count=$(curl -s "http://localhost:8000/api/questions/?subject_id=1&difficulty=HARD&limit=50" | python3 -c "import sys, json; print(len(json.load(sys.stdin)))" 2>/dev/null)

if [ "$easy_count" = "15" ] && [ "$medium_count" = "15" ] && [ "$hard_count" = "15" ]; then
    echo -e "${GREEN}✓ PASSED${NC} (15 per difficulty for Technology)"
    ((PASSED++))
else
    echo -e "${RED}✗ FAILED${NC}"
    echo "  Easy: $easy_count (expected 15)"
    echo "  Medium: $medium_count (expected 15)"
    echo "  Hard: $hard_count (expected 15)"
    ((FAILED++))
fi

# Summary
echo ""
echo "========================================"
echo "Test Results"
echo "========================================"
echo -e "Passed: ${GREEN}$PASSED${NC}"
echo -e "Failed: ${RED}$FAILED${NC}"
echo "Total: $((PASSED + FAILED))"
echo ""

if [ $FAILED -eq 0 ]; then
    echo -e "${GREEN}🎉 All tests passed! System is working perfectly!${NC}"
    exit 0
else
    echo -e "${RED}❌ Some tests failed. Please check the output above.${NC}"
    exit 1
fi
