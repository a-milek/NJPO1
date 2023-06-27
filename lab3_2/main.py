# Zaimplementuj wzorzec projektowy łańcuch odpowiedzialności
# Na przykładzie obsługi żądania _http_ (symulacja), w którym przed faktycznym kodem obsługi
# błędu ma zostać sprawdzone
# czy użytkownik może wysłać danego typu żądanie,
# czy żądanie nie dotyczy pliku,
# czy liczba żądań na minutę nie jest przekroczona,
# czy liczba żądań na minutę nie jest przekroczona dla zalogowanego użytkownika,
# czy przesłany formularz nie jest próbą `sql incjection`.

# Chain of responsibility pattern: https://refactoring.guru/pl/design-patterns/chain-of-responsibility

class HandlerInterface:
    @staticmethod
    def handle_request(request):
        pass


class CanSendRequestHandler(HandlerInterface):
    @staticmethod
    def handle_request(request):
        if can_send_request(request):
            return IsRequestAboutFileHandler().handle_request(request)
        else:
            return False


class IsRequestAboutFileHandler(HandlerInterface):
    @staticmethod
    def handle_request(request):
        if is_request_about_file(request):
            return IsNumberOfRequestsPerMinuteExceededHandler().handle_request(request)
        else:
            return False


class IsNumberOfRequestsPerMinuteExceededHandler(HandlerInterface):
    @staticmethod
    def handle_request(request):
        if is_number_of_requests_per_minute_exceeded(request):
            return IsNumberOfRequestsPerMinuteExceededForLoggedUserHandler().handle_request(
                request)
        else:
            return False


class IsNumberOfRequestsPerMinuteExceededForLoggedUserHandler(HandlerInterface):
    @staticmethod
    def handle_request(request):
        if is_number_of_requests_per_minute_exceeded_for_logged_user(request):
            return IsFormDataSqlInjectionHandler().handle_request(request)
        else:
            return False


class IsFormDataSqlInjectionHandler(HandlerInterface):
    @staticmethod
    def handle_request(request):
        if is_form_data_sql_injection(request):
            return True
        else:
            return False


# Can user send this type of request
def can_send_request(request):
    # Implementation
    return True


# Is request about file
def is_request_about_file(request):
    # Implementation
    return True


# Is number of requests per minute exceeded
def is_number_of_requests_per_minute_exceeded(request):
    # Implementation
    return True


# Is number of requests per minute exceeded for logged user
def is_number_of_requests_per_minute_exceeded_for_logged_user(request):
    # Implementation
    return True


# Is form data sql injection
def is_form_data_sql_injection(request):
    # Implementation
    return True


class Chain:
    @staticmethod
    def process(request):
        return CanSendRequestHandler().handle_request(request)


# Example case
if __name__ == '__main__':
    chain = Chain()
    request = 'GET'
    print(chain.process(request))