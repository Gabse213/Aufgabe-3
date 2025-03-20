from main_functions import estimate_max_hr
from main_functions import build_experiment
from main_functions import build_person
max_hr = estimate_max_hr(24, "male")
person = build_person("Gabriel", "Schwarz","male",24)
experiment = build_experiment("Test","20.03.25", "Gabriel","Ernst")
if __name__ == "__main__":
    print("Die richtige Datei wurde aufgerufen und es wird nur der ausgewählte Code Verwendet")
print(person)
print(experiment)
