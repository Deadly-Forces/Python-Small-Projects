# Encryption-Decryption Program

This is a simple encryption and decryption program written in Python. It uses a randomized substitution cipher to encrypt and decrypt messages.

## Features
- Randomized character mapping for encryption.
- Ability to encrypt and decrypt text messages.
- Uses Python's `random` and `string` modules.

## Requirements
- Python 3.x

## How It Works
1. The program generates a shuffled key mapping for encryption.
2. The user enters a message to encrypt.
3. The message is encrypted using the randomized mapping.
4. The user can then decrypt the message by providing the encrypted text.

## Usage

### Running the Program
```bash
python encrypt_decrypt.py
```

### Example
#### Encryption:
```
Enter a message to encrypt: Hello
Original message: Hello
Encrypted message: @>P_*
```

#### Decryption:
```
Enter a message to decrypt: @>P_*
Original message: @>P_*
Decrypted message: Hello
```

## Code Explanation
- The script defines a list of characters (`chars`) consisting of space, punctuation, digits, and ASCII letters.
- A copy (`key`) of this list is shuffled to create an encryption key.
- Encryption is performed by replacing each character in the input with its corresponding character in the shuffled key.
- Decryption works by finding the encrypted character in the shuffled key and mapping it back to the original character set.

## Contributing
Feel free to fork this repository and improve upon it. If you find any issues, open a pull request!



