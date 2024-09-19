# Script: Principles for Good Functions

## Why functions are important slide

Make one example for each point:

- Help to re-use code and avoid duplication -> example of not writing out the formula
  for CRRA utility multiple times
- Help to structure code and reduce cognitive load -> You can forget the formula for
  CRRA utility when you are done implementing the function and and function calls are
  much more readable than looking at the formula
- Make individual code snippets testable -> Can make sure it returns the right thing in
  known circumstances

## Pass all variables slide

- Mention that both alternatives to global variables are ok.
- Which one to use depends on whether the variable is just needed in one place or in
  multiple places.
