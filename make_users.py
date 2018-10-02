from visitatie import create_app
import config


def main():
    app = create_app(config, users = ['123', 'tako234'])


if __name__ == '__main__':
    main()
