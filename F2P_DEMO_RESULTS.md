# F2P (Fail-to-Pass) Demo Results

## Repository Created
Location: `/Users/abhishek/test-f2p-demo`

## What We Built

### 1. **Initial Code (main branch)** - WITH BUG
```python
def subtract(a, b):
    return a + b  # BUG: Should be a - b
```

### 2. **Fixed Code (fix-subtract-bug branch)** - BUG FIXED
```python
def subtract(a, b):
    return a - b  # FIXED!
```

### 3. **Test Suite**
Created 9 tests:
- 5 tests specifically for `subtract()` function
- 4 tests for other unchanged functions (`add`, `multiply`, `divide`)

## F2P Test Results

### On MAIN Branch (with bug):
```
✅ test_add_positive_numbers PASSED
✅ test_multiply_numbers PASSED
✅ test_divide_normal PASSED
✅ test_divide_by_zero_raises_error PASSED
❌ test_subtract_correct_result FAILED (returned 8 instead of 2)
❌ test_subtract_negative_result FAILED (returned 8 instead of -2)
❌ test_subtract_with_zero FAILED (returned 10 instead of -10)
❌ test_subtract_same_numbers FAILED (returned 10 instead of 0)
❌ test_subtract_negative_numbers FAILED (returned -8 instead of -2)

Result: 4 passed, 5 failed
```

### On fix-subtract-bug Branch (bug fixed):
```
✅ test_add_positive_numbers PASSED
✅ test_multiply_numbers PASSED
✅ test_divide_normal PASSED
✅ test_divide_by_zero_raises_error PASSED
✅ test_subtract_correct_result PASSED
✅ test_subtract_negative_result PASSED
✅ test_subtract_with_zero PASSED
✅ test_subtract_same_numbers PASSED
✅ test_subtract_negative_numbers PASSED

Result: 9 passed, 0 failed
```

## F2P Analysis

### F2P Tests: **5 out of 9 (55.6%)** ✅

**F2P Tests (failed on main, passed on fix):**
1. `test_subtract_correct_result` ✅ F2P
2. `test_subtract_negative_result` ✅ F2P
3. `test_subtract_with_zero` ✅ F2P
4. `test_subtract_same_numbers` ✅ F2P
5. `test_subtract_negative_numbers` ✅ F2P

**Pass-to-Pass Tests (passed on both):**
1. `test_add_positive_numbers`
2. `test_multiply_numbers`
3. `test_divide_normal`
4. `test_divide_by_zero_raises_error`

**Regressions (pass-to-fail):** 0 ✅

## Interpretation

✅ **Excellent F2P Rate!** 55.6% of tests are F2P
- This means 5 out of 9 tests specifically caught the bug
- The tests effectively validate the fix
- No regressions detected

✅ **Good Test Design**
- F2P tests target the changed function (`subtract`)
- P2P tests verify unchanged functionality still works
- Tests are comprehensive and well-balanced

## How to Test This Yourself

```bash
cd /Users/abhishek/test-f2p-demo

# Test on main branch (with bug)
git checkout main
/opt/homebrew/opt/python@3.13/bin/python3.13 -m pytest test_calculator.py -v

# Test on fix branch (bug fixed)
git checkout fix-subtract-bug
/opt/homebrew/opt/python@3.13/bin/python3.13 -m pytest test_calculator.py -v
```

## Next Steps: Push to GitHub

To use this with the F2P checker tool:

1. **Create GitHub repository:**
   ```bash
   gh repo create test-f2p-demo --public --source=. --remote=origin
   ```

2. **Push code:**
   ```bash
   git push -u origin main
   git push origin fix-subtract-bug
   ```

3. **Create Pull Request:**
   ```bash
   gh pr create --title "Fix subtract bug" \
                --body "Fixes subtract function that was adding instead of subtracting" \
                --base main \
                --head fix-subtract-bug
   ```

4. **Use F2P Checker Tool:**
   ```xml
   <function=check_f2p>
   <parameter name="pr_url">https://github.com/YOUR_USERNAME/test-f2p-demo/pull/1</parameter>
   <parameter name="test_file">test_calculator.py</parameter>
   <parameter name="security_risk">low</parameter>
   </function>
   ```

