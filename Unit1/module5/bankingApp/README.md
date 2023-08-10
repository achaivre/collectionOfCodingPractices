## Practice 2
The second practice will mimic the first, except we will be modeling our "Banking App".

### The Brief:
1. Should utilize input helper functions
2. Type Annotations
3. Utilize a dataclass
4. At least one function besides the main.
5. When the user begins the program for the first time, it should prompt the user to create a password.
6. After the password is set, it should prompt the user to type in the correct password.
7. After three wrong attempts at the password, the user should be locked out and prompted to contact support.
8. When the correct password is given, the user should be able to deposit, withdraw, reset password or logout.
9. Once a correct password is given the wrong attempts should reset.
10. A user should not be able to withdraw more money than what is currently in the account.
11. The user should start with no money in their account.
12. The user should be able to quit the program at any time.
13. The current screen should be printed after every input.

### Example:
- Welcome to Alyx's Banking App, where we steal your money.
- Set your password > boogawooga
- Screen: Password
- Input password: no
- Invalid password, please put in correct password.
- Screen: Password
- Input password: boogawooga
- Screen: Banking
- Balance: $0.00
- Do you want to [deposit], [withdraw], [reset] password, [logout], or [quit]? dePoSit
- How much are you depositing? 100.52
- Screen: Banking
- Balance: $100.52
- Do you want to [deposit], [withdraw], [reset] password, [logout], or [quit]? withdraw
- How much are you withdrawing? 200
- You do not have enough in your account, pick a new value.
- How much are you withdrawing? 50
- Screen: Banking
- Balance: $50.52
- Do you want to [deposit], [withdraw], [reset] password, [logout], or [quit]? reset
- Set your password > never
- Screen: Banking
- Balance: $50.52
- Do you want to [deposit], [withdraw], [reset] password, [logout], or [quit]? logout
- Screen: Password
- Input password: nope
- Invalid password, please put in correct password.
- Screen: Password
- Input password: yip yip
- Invalid password, please put in correct password.
- Screen: Password:
- Input password: NEVER
- Your account has been locked. Please contact support to unlock it. > no
- Your account has been locked. Please contact support to unlock it. > no
- Your account has been locked. Please contact support to unlock it. > no
- Your account has been locked. Please contact support to unlock it. > no
- Your account has been locked. Please contact support to unlock it. > no
- Your account has been locked. Please contact support to unlock it. > quit