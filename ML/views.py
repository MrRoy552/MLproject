
from django.http import HttpResponse
from django.shortcuts import render
import pickle
from pathlib import Path
file_dir=Path(__file__).resolve().parent.parent

# Create your views here.
def home(request):
    # return HttpResponse("welcome")
    return render(request,"index.html")

def predict(request):
    loaded_model=pickle.load(open(str(file_dir) + "\\Finalized_model.sav", "rb"))
    num_preg=float(request.POST["num_preg"])
    diastolic_bp=float(request.POST["diastolic_bp"])
    insulin=float(request.POST["insulin"])
    bmi=float(request.POST["bmi"])
    diab_pred=float(request.POST["diab_pred"])
    age=float(request.POST["age"])
    thickness=float(request.POST["thickness"])
    glucose_conc=float(request.POST["glucose_conc"])
    result=loaded_model.predict([[num_preg,glucose_conc,diab_pred,insulin,diastolic_bp,bmi,age,thickness]])
    print(result)
    if result==0:
        message="congrates your are Non Diabetic"
    else:
        message="Sorry you are diabetic"
    print(result)
    # dict={num_preg,glucose_conc,diab_pred,insulin,diastolic_bp,bmi,age,thickness,}
    return render(request,"diabetes.html",{"message":message})






