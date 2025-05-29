import re

class EmailAddressParser:
    def __init__(self, email_addresses):
        self.email_addresses = email_addresses

    def parse(self):
        # Find all email addresses using regex pattern
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        addresses = re.findall(email_pattern, self.email_addresses)
        # Get unique addresses and sort alphabetically
        return sorted(list(set(addresses)))