import bcrypt

"""
    TODO: Use a more secure hashing algorithm like Argon2 or PBKDF2 for 
    password hashing.The current implementation uses bcrypt, which is secure, 
    but Argon2 and PBKDF2 are considered more secure and resistant to certain
    types of attacks.
"""


class PasswordHasher:
    """
    A class for hashing and verifying passwords using bcrypt.
    """

    @staticmethod
    def hash_password(password: str) -> str:
        """
        Hashes a password using a secure hashing algorithm.

        Args:
            password (str): The plaintext password to hash.

        Returns:
            str: The hashed password.
        """
        return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """
        Verifies a plaintext password against a hashed password.

        Args:
            plain_password (str): The plaintext password to verify.
            hashed_password (str): The hashed password to compare against.

        Returns:
            bool: True if the passwords match, False otherwise.
        """
        return bcrypt.checkpw(
            plain_password.encode("utf-8"), hashed_password.encode("utf-8")
        )
