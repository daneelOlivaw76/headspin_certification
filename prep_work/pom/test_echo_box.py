from views.home_view import HomeView
from views.echo_view import EchoView


def test_echo_box(driver):
    message = 'Hello'

    home = HomeView(driver)
    home.nav_to_echo_box()

    echo_box = EchoView(driver)
    echo_box.save_message(message)
    assert echo_box.read_message() == message
    echo_box.nav_back()

    home.nav_to_echo_box()
    assert echo_box.read_message() == message
