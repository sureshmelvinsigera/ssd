from django.template.loader import render_to_string
from accounts.views import login
from pyvows import Vows, expect
from django_pyvows.context import DjangoHTTPContext

# We would need to export an .env variable to start testing
# env PYTHONPATH=$$PYTHONPATH:sssd/ pyvows infrastructure/testing/pyvows_login_test.py

DjangoHTTPContext.start_environment("ssd.settings")


@Vows.batch  # Sets the batch that PyVows is going to run
class LoginVows(DjangoHTTPContext):

    def topic(self):
        self.start_server()  # Start PyVows service

    class LoginURL(DjangoHTTPContext):  # Checks that URL works correctly

        def topic(self):
            return self.url("^index/$")

        def url_map(self, topic):
            expect(topic).to_match_view(login)

    class LoginView(DjangoHTTPContext):  # Checks that login returns a valid HTTP response

        def topic(self):
            return login(self.request())

        def valid_HTTP_Response(self, topic):
            expect(topic).to_be_http_response()

        def return_login(self, topic):
            loginTemplate = render_to_string("index.html")
            expect(topic.content.decode()).to_equal(loginTemplate)
