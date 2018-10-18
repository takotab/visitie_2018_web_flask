from visitatie import create_app
import config


def main():
    with open('Results 2017 - Fake.csv') as f:
        for line in f:
            print(line)

    lst_of_users = [('takotabak' + str(i), 'takotabak_' + str(i)) for i in range(5)]
    app = create_app(config, users = lst_of_users)


if __name__ == '__main__':
    main()
