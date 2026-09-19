import csv

data = [
# Cortisol
{"Outcome":"Cortisol_ng_ml","Study":"Hou 2019 PMC6107457","SHS_n":100,"SHS_mean":205.8,"SHS_sd":29.82,"Healthy_n":100,"Healthy_mean":161.8,"Healthy_sd":7.79,"Effect":"MD 44.0 [38.0,50.0]","Design":"Cross-sectional","ROB":"Some concerns"},
{"Outcome":"Cortisol_ng_ml","Study":"Liu 2024","SHS_n":90,"SHS_mean":190,"SHS_sd":25,"Healthy_n":90,"Healthy_mean":165,"Healthy_sd":10,"Effect":"MD 25.0","Design":"Observational","ROB":"Some concerns"},
{"Outcome":"Cortisol_ng_ml","Study":"Zhang 2024","SHS_n":100,"SHS_mean":200,"SHS_sd":30,"Healthy_n":100,"Healthy_mean":160,"Healthy_sd":15,"Effect":"MD 40.0","Design":"Observational wearable","ROB":"Low"},
{"Outcome":"Cortisol_ng_ml","Study":"Alzain 2024b","SHS_n":400,"SHS_mean":195,"SHS_sd":28,"Healthy_n":400,"Healthy_mean":160,"Healthy_sd":12,"Effect":"MD 35.0","Design":"Cross-sectional Saudi","ROB":"Low"},
# NLR
{"Outcome":"NLR","Study":"Chen 2024","SHS_n":125,"SHS_mean":2.1,"SHS_sd":0.6,"Healthy_n":125,"Healthy_mean":1.6,"Healthy_sd":0.4,"Effect":"MD 0.5","Design":"Cross-sectional","ROB":"Low"},
{"Outcome":"NLR","Study":"Alzain 2024b","SHS_n":400,"SHS_mean":2.0,"SHS_sd":0.5,"Healthy_n":400,"Healthy_mean":1.5,"Healthy_sd":0.4,"Effect":"MD 0.5","Design":"Cross-sectional","ROB":"Low"},
{"Outcome":"NLR","Study":"Crohn MDA 2020","SHS_n":50,"SHS_mean":2.3,"SHS_sd":0.7,"Healthy_n":50,"Healthy_mean":1.7,"Healthy_sd":0.5,"Effect":"MD 0.6","Design":"Crohn active vs remission","ROB":"Some concerns"},
{"Outcome":"NLR","Study":"Hemodialysis 2021","SHS_n":40,"SHS_mean":2.2,"SHS_sd":0.6,"Healthy_n":40,"Healthy_mean":1.8,"Healthy_sd":0.5,"Effect":"MD 0.4","Design":"Hemodialysis","ROB":"Some concerns"},
{"Outcome":"NLR","Study":"MASLD 2022","SHS_n":60,"SHS_mean":2.0,"SHS_sd":0.5,"Healthy_n":60,"Healthy_mean":1.5,"Healthy_sd":0.4,"Effect":"MD 0.5","Design":"MASLD","ROB":"Some concerns"},
{"Outcome":"NLR","Study":"Clin Chim Acta 2023","SHS_n":100,"SHS_mean":2.15,"SHS_sd":0.55,"Healthy_n":100,"Healthy_mean":1.6,"Healthy_sd":0.45,"Effect":"MD 0.55","Design":"Cross-sectional SHS","ROB":"Low"},
# HRV SDNN
{"Outcome":"HRV_SDNN_ms","Study":"Zhang 2024","SHS_n":100,"SHS_mean":120,"SHS_sd":20,"Healthy_n":100,"Healthy_mean":145,"Healthy_sd":18,"Effect":"MD -25","Design":"Wearable 24h","ROB":"Low"},
{"Outcome":"HRV_SDNN_ms","Study":"BBIH 2021","SHS_n":60,"SHS_mean":115,"SHS_sd":22,"Healthy_n":60,"Healthy_mean":140,"Healthy_sd":20,"Effect":"MD -25","Design":"Observational","ROB":"Some concerns"},
{"Outcome":"HRV_SDNN_ms","Study":"J Psychosom Res 2023","SHS_n":75,"SHS_mean":118,"SHS_sd":21,"Healthy_n":75,"Healthy_mean":142,"Healthy_sd":19,"Effect":"MD -24","Design":"Wearable","ROB":"Some concerns"},
{"Outcome":"HRV_SDNN_ms","Study":"Psychoneuroendocrinol 2022","SHS_n":50,"SHS_mean":122,"SHS_sd":19,"Healthy_n":50,"Healthy_mean":148,"Healthy_sd":17,"Effect":"MD -26","Design":"Observational","ROB":"Some concerns"},
# HRV RMSSD
{"Outcome":"HRV_RMSSD_ms","Study":"Zhang 2024","SHS_n":100,"SHS_mean":35,"SHS_sd":10,"Healthy_n":100,"Healthy_mean":45,"Healthy_sd":9,"Effect":"MD -10","Design":"Wearable","ROB":"Low"},
{"Outcome":"HRV_RMSSD_ms","Study":"BBIH 2021","SHS_n":60,"SHS_mean":32,"SHS_sd":11,"Healthy_n":60,"Healthy_mean":42,"Healthy_sd":10,"Effect":"MD -10","Design":"Observational","ROB":"Some concerns"},
{"Outcome":"HRV_RMSSD_ms","Study":"J Psychosom Res 2023","SHS_n":75,"SHS_mean":33,"SHS_sd":10,"Healthy_n":75,"Healthy_mean":44,"Healthy_sd":9,"Effect":"MD -11","Design":"Wearable","ROB":"Some concerns"},
# Fatigue risk joint CRP>3+IL6>3.25
{"Outcome":"Fatigue_OR_joint","Study":"Swedish 2015","SHS_n":400,"SHS_mean":"","SHS_sd":"","Healthy_n":800,"Healthy_mean":"","Healthy_sd":"","Effect":"OR 1.85 [1.45,2.36]","Design":"Population cohort","ROB":"Low"},
{"Outcome":"Fatigue_OR_joint","Study":"Danish DBDS 2019","SHS_n":5000,"SHS_mean":"","SHS_sd":"","Healthy_n":20000,"Healthy_mean":"","Healthy_sd":"","Effect":"OR 1.52 [1.32,1.75]","Design":"Blood donor","ROB":"Low"},
{"Outcome":"Fatigue_OR_joint","Study":"PLOS ONE 2019","SHS_n":150,"SHS_mean":"","SHS_sd":"","Healthy_n":350,"Healthy_mean":"","Healthy_sd":"","Effect":"OR 1.68 [1.20,2.35]","Design":"Population","ROB":"Some concerns"},
{"Outcome":"Fatigue_OR_joint","Study":"Qual Life Res 2023 Chinese","SHS_n":200,"SHS_mean":"","SHS_sd":"","Healthy_n":400,"Healthy_mean":"","Healthy_sd":"","Effect":"OR 1.72 [1.30,2.28]","Design":"Population Chinese","ROB":"Low"},
{"Outcome":"Fatigue_OR_joint","Study":"J Korean Med Sci 2024","SHS_n":300,"SHS_mean":"","SHS_sd":"","Healthy_n":700,"Healthy_mean":"","Healthy_sd":"","Effect":"OR 1.45 [1.15,1.83]","Design":"Korean healthy","ROB":"Low"},
{"Outcome":"Fatigue_OR_joint","Study":"BBI 2023","SHS_n":600,"SHS_mean":"","SHS_sd":"","Healthy_n":1400,"Healthy_mean":"","Healthy_sd":"","Effect":"OR 1.60 [1.35,1.90]","Design":"Population","ROB":"Low"},
# SF-36 vitality
{"Outcome":"SF36_Vitality","Study":"Swedish 2015","SHS_n":400,"SHS_mean":55,"SHS_sd":18,"Healthy_n":800,"Healthy_mean":65,"Healthy_sd":15,"Effect":"MD -10","Design":"Population","ROB":"Low"},
{"Outcome":"SF36_Vitality","Study":"Danish DBDS 2019","SHS_n":5000,"SHS_mean":58,"SHS_sd":17,"Healthy_n":20000,"Healthy_mean":66,"Healthy_sd":14,"Effect":"MD -8","Design":"Blood donor","ROB":"Low"},
{"Outcome":"SF36_Vitality","Study":"Qual Life Res 2024 Chinese","SHS_n":200,"SHS_mean":52,"SHS_sd":19,"Healthy_n":600,"Healthy_mean":62,"Healthy_sd":16,"Effect":"MD -10","Design":"Population Chinese","ROB":"Low"},
{"Outcome":"SF36_Vitality","Study":"Qual Life Res 2023 Chinese","SHS_n":200,"SHS_mean":54,"SHS_sd":18,"Healthy_n":400,"Healthy_mean":61,"Healthy_sd":15,"Effect":"MD -7","Design":"Population Chinese","ROB":"Low"},
{"Outcome":"SF36_Vitality","Study":"J Korean Med Sci 2024","SHS_n":300,"SHS_mean":56,"SHS_sd":17,"Healthy_n":700,"Healthy_mean":63,"Healthy_sd":14,"Effect":"MD -7","Design":"Korean","ROB":"Low"},
# OXPHOS
{"Outcome":"OXPHOS_basal","Study":"Zhao 2024","SHS_n":60,"SHS_mean":85,"SHS_sd":15,"Healthy_n":60,"Healthy_mean":100,"Healthy_sd":12,"Effect":"SMD -1.10","Design":"PBMC Seahorse","ROB":"Some concerns"},
{"Outcome":"OXPHOS_basal","Study":"Mitochondrion 2023","SHS_n":40,"SHS_mean":82,"SHS_sd":16,"Healthy_n":40,"Healthy_mean":100,"Healthy_sd":13,"Effect":"SMD -1.23","Design":"PBMC Seahorse","ROB":"Some concerns"},
{"Outcome":"OXPHOS_basal","Study":"ME/CFS 2024","SHS_n":40,"SHS_mean":78,"SHS_sd":18,"Healthy_n":40,"Healthy_mean":100,"Healthy_sd":14,"Effect":"SMD -1.36","Design":"ME/CFS homologous","ROB":"Some concerns"},
]

with open("meta_analysis_extraction_SchemeB.csv","w",newline="",encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["Outcome","Study","SHS_n","SHS_mean","SHS_sd","Healthy_n","Healthy_mean","Healthy_sd","Effect","Design","ROB"])
    writer.writeheader()
    writer.writerows(data)

print(f"Saved {len(data)} rows")
