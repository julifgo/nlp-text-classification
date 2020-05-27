from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from lightgbm import LGBMClassifier
from xgboost import XGBClassifier
import functions as utils


def simple_evaluate(titles_vectors, titles_vectors_test, y_train, y_test):
    clfs = [
        LogisticRegression(), 
        RandomForestClassifier(max_depth=6, class_weight="balanced_subsample"), 
        XGBClassifier(max_depth=7, n_estimators=500, eta=0.2, booster='dart'),
        LGBMClassifier(max_depth=7, n_estimators=250, learning_rate=0.1, boosting_type='dart'),
    ]

    @utils.time_decorator
    def evaluate_model(clf):
        print(clf.__class__.__name__)
        
        if index in [2]:
            clf.fit(
                titles_vectors, y_train, 
                eval_set=[(titles_vectors_test, y_test)],
                early_stopping_rounds=10,
                verbose=False)
        else:
            clf.fit(titles_vectors, y_train)

        from sklearn.metrics import classification_report
        print(classification_report(y_train, clf.predict(titles_vectors)))
        print("Test")
        print(classification_report(y_test, clf.predict(titles_vectors_test)))
        

    for index, clf in enumerate(clfs): 
        evaluate_model(clf) 
        
    