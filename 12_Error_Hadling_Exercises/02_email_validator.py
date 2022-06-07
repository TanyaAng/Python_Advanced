import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


pattern = r"(?P<email_name>\w+)@(?P<host_name>\w+).(?P<domain>\w+)"

while True:
    command = input()
    if command == 'End':
        break
    email = command
    match = re.match(pattern, email)
    if match == None:
        raise MustContainAtSymbolError(f"Email must contain @")
    else:
        match_dict = [match_obj.groupdict() for match_obj in re.finditer(pattern, email)]
        for data in match_dict:
            if len(data['email_name']) <= 4:
                raise NameTooShortError("Name must be more than 4 characters")
            elif data["domain"] not in ['com', 'bg', 'org', 'net']:
                raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
            else:
                print("Email is valid")
