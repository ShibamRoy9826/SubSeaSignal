from django.shortcuts import render
# import joblib
import numpy
from django.http import HttpResponse
# import os
import pickle


# model=joblib.load("/home/SubSeaSignal/SubSeaSignal/rockVSmine.joblib")
with open('/home/SubSeaSignal/SubSeaSignal/rockVSmine.pickle', 'rb') as f:
     model = pickle.load(f)
# Create your views here.
def index(request):
    return render(request,"index.html")

def User(request):
    try:
        name=request.GET["Name"]
        inpData=request.GET['dimensions']
        data={"Name":name,"mine":False}
        if " " in inpData:
            inpData=inpData.replace(" ","")
        inpData=inpData.split(",")
        inpData=[float(i) for i in inpData]
        if len(inpData)<60:
            last = inpData[-1]
            inpData.extend([last] * (60 - len(inpData)))
        elif len(inpData)>60:
            inpData=inpData[:60]
        inpData=numpy.asarray(tuple(inpData))

        inpData=inpData.reshape(1,-1)

        res=model.predict(inpData)
        # res=['R']
        if res[0]=='M':
            data["mine"]=True

        return render(request,"result.html",data)
    except:
        return HttpResponse("Sorry, but Some issue occured, please check if your input was correct")

    # return HttpResponse(os.getcwd())