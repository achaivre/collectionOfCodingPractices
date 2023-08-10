# README

## Practice 1:
The first practice activity we will be working on is modeling our phone states.

Specifically, we will model the passcode feature of our phone.

### The brief is this:
1. We should use a dataclass to model the states of the phone.
2. We should utilize at least one function besides the main.
3. We should have input helper functions and type annotations.
4. When a user begins the program, they should be able to set a passcode.
5. Once the passcode is set, the phone should start "LOCKED" and "CLOSED".
6. If the phone is "LOCKED", the user should only be able to type in the passcode to unlock it.
7. The phone cannot be opened while locked.
8. After three wrong attempts, the phone should "HARDLOCK", meaning the user should only be able to quit the program.
9. The attempt counter should reset after every successful unlock.
10. If the user puts in the correct passcode, it should "UNLOCK" the phone. While unlocked the user should be able to "OPEN" the phone.
11. While the phone is both unlocked and open, they should be able to reset the passcode and close the phone.
12. They should not be able to relock while it's unlocked unless the phone is "CLOSED".
13. The state of the phone being open or closed, and locked, unlocked, or hardlocked should print after every input.


### Example:

- Code? 1234
- STATE: LOCKED
- PHONE: CLOSED
- Input Code: 12
- Please put in the correct code.
- STATE: LOCKED
- PHONE: CLOSED
- Input Code: 1234
- STATE: UNLOCKED
- PHONE: CLOSED
- Do you want to [lock], [open], or [quit]? open
- STATE: UNLOCKED
- PHONE: OPEN
- Do you want to [reset] your passcode, [close], or [quit]? rEsEt
- Code? abcd
- STATE: UNLOCKED
- PHONE: OPEN
- Do you want to [reset] your passcode, [close], or [quit]? lock
- Invalid Input.
- STATE: UNLOCKED
- PHONE: OPEN
- Do you want to [reset] your passcode, [close], or [quit]? close
- STATE: UNLOCKED
- PHONE: CLOSED
- Do you want to [lock], [open], or [quit]? lock
- STATE: LOCKED
- PHONE: CLOSED
- Input Code: 1
- Please put in correct code.
- STATE: LOCKED
- PHONE: CLOSED
- Input Code: 3
- Please put in correct code.
- STATE: LOCKED
- PHONE: CLOSED
- Input Code: alkz
- STATE: HARDLOCKED
- quit? no
- STATE: HARDLOCKED
- quit? no
- STATE: HARDLOCKED
- quit? quit