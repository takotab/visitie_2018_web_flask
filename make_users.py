from visitatie import create_app
import config
import pandas as pd


def main():
    df = pd.read_csv("fake_users.csv")
    lst_of_users = []
    for index, row in df.iterrows():
        lst_of_users.append(row.to_dict())

    app = create_app(config, users=lst_of_users)


if __name__ == "__main__":
    main()
