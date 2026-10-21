# Password Strength Checker

**Purpose**  
A command line tool that tells the user whether a password is weak, medium or strong, and explains why.

**Input**  
One password typed in the terminal.

**Output**  
A strength level (weak, medium or strong) and the reasons behind it.  
Example: `Weak: shorter than 8 characters and no symbols`

**Logic**

1. If the input is empty or only spaces, show an error and ask again.
2. If the password is shorter than 8 characters, it is Weak.
3. If the password is in the common password list, it is Weak.
4. Otherwise, add points for length and character types.
5. Translate the final score into a level.
6. Show the level and the reasons for any missing points.

**Structure**  
One function per rule and one function that combines the scores. The flow is shown with a UML activity diagram.

**Tests**

|Input|Expected output|
|---|---|
|`abc`|Weak|
|`password`|Weak (found in the common password list)|
|`Tr0pical!Sun`|Strong|
|Empty input|Clear error message|

## Scoring rules

### Length

- Less than 8 characters: always Weak (see Logic)
- 8 to 11 characters:1 point
- 12 or more characters: 2 points


### Character types
- Contains lowercase letters: 1 point
- Contains uppercase letters: 1 point
- Contains digits: 1point
- Contains symbols: 1 point

- Which are considered symbols?
    - ```! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~```

### Common passwords

- if the password is in the common password list, it is always Weak
- The check ignores uppercase and lowercase (PASSWORD = password)

### Score to level

- Maximum score: 6 points (2 for length + 4 for character types)
- 0 to 2 points: Weak
- 3 to 4 points: Medium
- 5 to 6 points: Strong
- A password shorter than 8 characters is always Weak

## Edge cases

- empty input: the program shows an error message and assks again
- only spaces; treated the same as empty input