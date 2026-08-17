def calculate_risk(temperature, pressure, worker_experience):
    score=temperature*0.4 + pressure*0.4 + worker_experience*0.2
    return score
machine = {
    "name":"Boiler A",
    "temperature":95,
    "pressure":85,
    "worker_experience":60
}
risk_score=calculate_risk(machine["temperature"],machine["pressure"],machine["worker_experience"])
machine["risk_score"]=risk_score
if risk_score>=80:
    machine["status"]="Danger"
else:
    machine["status"]="Safe"
print(machine)