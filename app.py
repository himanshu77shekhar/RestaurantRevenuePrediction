from flask import Flask,render_template,request
import pickle
import numpy as np
app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))
@app.route('/')
def home():
    return render_template("home.html")
@app.route('/predict',methods=['POST','GET'])
def predict():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        
        to_predict_list = list(to_predict_list.values())
        
        to_predict_list[2]= (to_predict_list[2].replace('-', '/'))
        var=to_predict_list[2]
        var=var.split('/')
        var=[int(ele) for ele in var]
        to_predict_list.pop(2)
        to_predict_list.insert(4,var[1])
        to_predict_list.insert(5,var[0])
        to_predict_list.insert(6,var[2])
        print(to_predict_list)
        
        d={}
        d["Ankara"]=3
        d["Samsun"]=5
        to_predict_list[1]=d[to_predict_list[1]]
       # to_predict_list.pop(1)
        #to_predict_list.insert(1,3)
        #clean_data = [float(i) for i in to_predict_list] 
        to_predict_list = list(map(float, to_predict_list))
        to_predict = np.array(to_predict_list).reshape(1,44)
        result = model.predict(to_predict)
        output=round(result[0],2)
        return render_template('index.html',prediction_text="Revenue is Rs. {}".format(output))
        if (output>3000000):
             return render_template('index.html',prediction="you can Invent {}".format(output))
        else:
            return render_template('index.html',prediction="you can't Invent {}".format(output))
            

if __name__ == '__main__':
    app.run(debug=True)
