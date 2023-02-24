from view.home_view import HomeView
from controller.home_controller import HomeController
from model.home_model import HomeModel


def main() -> None:
    home_view = HomeView()
    home_model = HomeModel()
    home_controller = HomeController(home_view, home_model)
    home_controller.run()


if __name__ == "__main__":
    main()