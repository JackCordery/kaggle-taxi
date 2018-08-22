from config import PATHS, VARIABLES
from etl import prepare_data
from model import model_linear, evaluate
import pandas as pd


def main():
    sample_path = PATHS["sample"]
    label_name = VARIABLES["label_name"]
    random_seed = VARIABLES["random_seed"]
    train_test_ratio = VARIABLES["train_test_ratio"]
    df = pd.read_csv(sample_path)
    print(df.head())

    print("The dataframe has the following shape: {}".format(df.shape))
    df.dropna(inplace=True)
    print("The dataframe has the following shape: {}".format(df.shape))
    data = prepare_data(df, label_name, train_test_ratio, random_seed)

    print(data["X_train"].head())
    print(data["y_train"].head())

    model = model_linear(data)
    evaluate_scores = evaluate(data, model)
    print(evaluate_scores)

    return


if __name__ == '__main__':
    main()
