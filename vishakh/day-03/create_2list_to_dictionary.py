'''

III. Created two lists and combined both to create a dict as asked.
fields = ["wo_id","work_order_date","work_order_details"]
data = [{"WO-01","2022-05-06","Identify what needs to be done to resolve a maintenance issue."},
{"WO-02","2022-05-07","Complete a work order request form to authorize maintenance tasks."},
{"WO-03","2022-05-08","Maintenance management decides if there is a legitimate need."}]

1. create below dict as given below.
[{"wo_id": <WO-01> "work_order_date":<>"work_order_details":<>},
{"wo_id": <WO-02> "work_order_date":<>"work_order_details":<>},
{"wo_id": <WO-03> "work_order_date":<>"work_order_details":<>}]

2. create a dict as given below format
[{"WO-01": {
"work_order_details" : <"work_order_details">,
"wo_date": <>
},
{"WO-02": {
"work_order_details" : <"work_order_details">,
"wo_date": <>
}
}]





'''

#create two list

fields = ["wo_id","work_order_date","work_order_details"]

data = [{"WO-01","2022-05-06","Identify what needs to be done to resolve a maintenance issue."},
{"WO-02","2022-05-07","Complete a work order request form to authorize maintenance tasks."},
{"WO-03","2022-05-08","Maintenance management decides if there is a legitimate need."}]
# new_list=[]
# for values in fields:
#     for items in data:
#         if data[0]==items:
#             new_list.append({values:items})
#             print(new_list)
for values in data:
    for item in values:
        print("before if",item)
        if "WO" in item:
            print(item)





