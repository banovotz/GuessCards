from config import config
from sklearn import tree
import pickledb
import random


cards_and_dimensions_db = pickledb.load(config.CARDS_AND_DIMENSIONS_PICKLE_DB, False)

class Predict():
    def predict_bool(self):
        x=[]
        y=[]

        for i in cards_and_dimensions_db.getall():
            #print cards_and_dimensions_db.dgetall(i)
            x.append([i, cards_and_dimensions_db.dgetall(i)["dimension_value"]])
            if cards_and_dimensions_db.dgetall((i))["rule_bool"]=="true":
                y.append(1)
            else:
                y.append(0)


        clf = tree.DecisionTreeRegressor()
        clf = clf.fit(x, y)

        for z in range(50):
            random_number= random.randint(1,25)
            a=str(random_number)
            if int(clf.predict([[float(z), float(random_number)]])[0])==1:
                b = "true"
            else:
                b = "false"
            print("zbroj karata je " + a + ",a zakljucak je " + b)


