#!/bin/bash
set +e

echo "======================================"
echo "F2P Checker - LOCAL PR Demo"
echo "======================================"
echo ""

CURRENT_BRANCH=$(git branch --show-current)

echo "Testing on MAIN branch (with bug)..."
git checkout main -q
python3 -m pytest test_calculator.py -v 2>&1 | tee /tmp/base.txt
BASE_PASSED=$(grep -c "PASSED" /tmp/base.txt || echo "0")
BASE_FAILED=$(grep -c "FAILED" /tmp/base.txt || echo "0")
echo "Main: $BASE_PASSED passed, $BASE_FAILED failed"
echo ""

echo "Testing on fix-subtract-bug branch..."
git checkout fix-subtract-bug -q
python3 -m pytest test_calculator.py -v 2>&1 | tee /tmp/pr.txt
PR_PASSED=$(grep -c "PASSED" /tmp/pr.txt || echo "0")
PR_FAILED=$(grep -c "FAILED" /tmp/pr.txt || echo "0")
echo "Fix: $PR_PASSED passed, $PR_FAILED failed"
echo ""

git checkout $CURRENT_BRANCH -q

F2P=$((PR_PASSED - BASE_PASSED))
echo "=== Results ==="
echo "F2P Tests: $F2P (tests that now pass after the fix)"
echo "Total: $((BASE_PASSED + BASE_FAILED)) tests"
