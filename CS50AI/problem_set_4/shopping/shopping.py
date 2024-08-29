import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    data_list = []
    with open("shopping.csv") as file:
        data = csv.DictReader(file)
        for row in data:
            data_list.append(row)

    def visitor_converter(visitor):
        if visitor == 'Returning_Visitor':
            return 1
        return 0

    def weekend_converter(weekend):
        if weekend == 'TRUE':
            return 1
        return 0

    def month_converter(month):
        month_dict = {
            'Jan': 0, 'Feb': 1, 'Mar': 2, 'Apr': 3, 'May': 4, 'June': 5,
            'Jul': 6, 'Aug': 7, 'Sep': 8, 'Oct': 9, 'Nov': 10, 'Dec': 11
        }
        return month_dict[month]

    def revenue_converter(revenue):
        if revenue == 'TRUE':
            return 1
        return 0

    int_list = ['Administrative', 'Informational', 'ProductRelated', 'OperatingSystems', 'Browser', 'Region',
                'TrafficType']
    float_list = ['Administrative_Duration', 'Informational_Duration', 'ProductRelated_Duration', 'BounceRates',
                  'ExitRates', 'PageValues', 'SpecialDay']

    evidence = []
    labels = []

    for i in range(len(data_list)):
        temp_evidence = []
        data_list[i]["Month"] = month_converter(data_list[i]["Month"])
        data_list[i]["Weekend"] = weekend_converter(data_list[i]["Weekend"])
        data_list[i]["VisitorType"] = visitor_converter(data_list[i]["VisitorType"])
        data_list[i]["Revenue"] = revenue_converter(data_list[i]["Revenue"])
        for item in data_list[i]:
            if item == "Revenue":
                labels.append(data_list[i][item])
            else:
                if item in int_list:
                    data_list[i][item] = int(data_list[i][item])
                elif item in float_list:
                    data_list[i][item] = float(data_list[i][item])
                temp_evidence.append(data_list[i][item])
        evidence.append(temp_evidence)
    return evidence, labels


def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    model = KNeighborsClassifier(n_neighbors=1)
    return model.fit(evidence, labels)


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificity).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    data_len = len(labels)
    pos_correct = 0
    pos_len = 0
    neg_correct = 0
    neg_len = 0
    for i in range(len(labels)):
        if labels[i] == 0:
            neg_len += 1
            if labels[i] == predictions[i]:
                neg_correct += 1
        else:
            pos_len += 1
            if labels[i] == predictions[i]:
                pos_correct += 1
    sensitivity = pos_correct / pos_len
    specificity = neg_correct / neg_len
    return sensitivity, specificity


if __name__ == "__main__":
    main()
