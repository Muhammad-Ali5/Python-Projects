# Test Plan

## Overview
This document outlines the testing strategy for the Simple Login System.

## Test Scope
- **Functionality**: `login(username, password)`
- **Types of Tests**:
  - Unit Tests: Verify individual cases (4 positive, 2 negative).
  - Integration Tests: Verify the flow of continuous login attempts.

## Test Cases

### Unit Tests
| ID | Description | Type | Expected Result |
|----|-------------|------|-----------------|
| TC01 | Login as standard user | Positive | True |
| TC02 | Login as admin user | Positive | True |
| TC03 | Login as guest user | Positive | True |
| TC04 | Login as test user | Positive | True |
| TC05 | Invalid username | Negative | False |
| TC06 | Invalid password | Negative | False |

### Integration Tests
- **Flow**: Attempt valid login -> Attempt invalid login -> Attempt unknown user.
- **Goal**: Ensure system handles a sequence of calls correctly.
