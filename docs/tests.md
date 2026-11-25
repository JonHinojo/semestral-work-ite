# Test plan

I wrote the tests with unittest. They are in the file tests/test_password_checker.py.
To run all of them, I run test_main.py from the main folder of the project.

## What I test

Length:
- "abc" has less than 8 characters, so it should get 0 points and the reason "shorter than 8 characters".
- "abcdefgh" has exactly 8 characters, so it should get 1 point.
- "abcdefghijkl" has exactly 12 characters, so it should get 2 points.

Character types:
- "hello" only has lowercase letters, so it should get 1 point and say that it has no uppercase letters, no digits and no symbols.
- "Tr0pical!Sun" has all the types, so it should get 4 points and no reasons.

Common passwords:
- "password" is in the list, so it should be found.
- "PASSWORD" should also be found, because the check does not care about uppercase or lowercase.
- "Tr0pical!Sun" is not in the list.

Score to level:
- 2 points should be Weak, 3 points should be Medium and 5 points should be Strong. These are the limits between the levels.

Final result:
- "Tr0pical!Sun" should be Strong.
- "SummerTime" should be Medium, because it has no digits and no symbols.
- "password" should be Weak, because it is a common password.
- An empty password should give an error.
- A password with only spaces should also give an error.

## Why I chose these cases

I tried to test each rule on its own, and also the limits like 8 and 12 characters,
because that is where it is easy to make mistakes.

The "SummerTime" test is important for me. While I was programming, I swapped the
uppercase check and the digit check by mistake. When I tested with "Summer2024" I
did not notice it, because that password has uppercase letters and digits at the
same time. "SummerTime" has uppercase letters but no digits, so with this password
the mistake appeared straight away. That is why I added it as a test.