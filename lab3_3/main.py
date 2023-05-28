# Zadanie 3. Za pomocą dowolnego wzorca projektowego zaimplementuj mechanizm sprawdzający poprawność wyrażenia postaci:
# a + b = c (poprawne)
# (a + b = c (niepoprawne)
# a + = c (niepoprawne)

# Used design pattern: strategy
# Source: https://refactoring.guru/design-patterns/strategy

import re


# interface for strategies
class StringValidator:
    def validate(self, string):
        pass


# concrete strategies
class ValidateAgainstRegex(StringValidator):
    # regex for a + b = c
    regex = r"^[a-zA-Z0-9]+(\s\+\s[a-zA-Z0-9]+)*\s=\s[a-zA-Z0-9]+$"

    def validate(self, string):
        return re.match(self.regex, string) is not None


# ... other strategies if needed


if __name__ == '__main__':
    string_1 = "a + b = c"
    string_2 = "(a + b = c"
    string_3 = "a + = c"

    validator = ValidateAgainstRegex()
    print(validator.validate(string_1))
    print(validator.validate(string_2))
    print(validator.validate(string_3))
