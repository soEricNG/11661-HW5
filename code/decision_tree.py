import pandas as pd
from sklearn import tree
import graphviz
from sklearn.externals.six import StringIO
import pydot

# METRICS = ['Unigram pareto', 'Bigram pareto', 'Trigram Pareto', 'TTR',
#            'EOS', 'EOC', 'ALC', 'ALS', 'Perplexity Ratio']
METRICS = ['Bigram-Unigram', 'TTR', 'Perplexity Ratio']


def read_train_input(input_filepath):
    train_data_df = pd.read_csv(input_filepath, index_col='Index')
    X = []
    Y = []
    for _, row in train_data_df.iterrows():
        row_features = [row[m] for m in METRICS]
        label = row['Label']
        X.append(row_features)
        Y.append(label)
    return X, Y


def read_test_input(input_filepath):
    test_data_df = pd.read_csv(input_filepath, index_col='Index')
    X = []
    for _, row in test_data_df.iterrows():
        row_features = [row[m] for m in METRICS]
        X.append(row_features)
    return X


if __name__ == '__main__':
    features, labels = read_train_input('../data/train_data_v3.csv')
    # print(features)
    # print(labels)
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(features, labels)
    # dot_data = tree.export_graphviz(clf, out_file='tree.dot')
    # dot_data = StringIO()
    # tree.export_graphviz(clf, out_file=dot_data)
    # graph = pydot.graph_from_dot_data(dot_data.getvalue())
    # graph.write_pdf("iris.pdf")
    test_features = read_test_input('../data/test_data_v3.csv')
    predictions = clf.predict(test_features)
    for ind, label in enumerate(predictions):
        print(f'{ind+1}.txt: {label}')

