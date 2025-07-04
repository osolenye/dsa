states_needed = set(["mt", "wa", "or", "id", "nv", "ut","са","az"])

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "са"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_statios = set()

best_station = None
states_covered = set()
for station, states_for_station in stations.items():
    covered = states_needed & states_covered
    if len(covered) > len(states_covered):
        best_station = station
        states_covered = covered