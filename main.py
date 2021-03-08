import json
from contextlib import redirect_stdout



# Open json file
with open('contacts.json') as json_file:
    data = json.load(json_file)

# Sort data
orderedEmail = sorted(data, key=lambda k: k["Email"])

# loop through data
for x in range(0, len(orderedEmail) - 1):
    if orderedEmail[x]["Email"] == orderedEmail[x + 1]["Email"] and orderedEmail[x]["Email"] != "":

        # Updating number of contacts
        orderedEmail[x + 1]["Contacts"] += orderedEmail[x]["Contacts"]

        # Adding all the Id's
        if orderedEmail[x + 1]["Id"] != "" and orderedEmail[x]["Id"] != "" and orderedEmail[x]["Id"] != \
                orderedEmail[x + 1]["Id"]:
            if isinstance(orderedEmail[x]["Id"], int):
                orderedEmail[x]["Id"] = [orderedEmail[x]["Id"]]
            if isinstance(orderedEmail[x + 1]["Id"], int):
                orderedEmail[x + 1]["Id"] = [orderedEmail[x + 1]["Id"]]

            (orderedEmail[x + 1]["Id"]).extend(orderedEmail[x]["Id"])
            orderedEmail[x]["Id"] = -1

        # Adding all the emails
        if orderedEmail[x + 1]["Email"] != "" and orderedEmail[x]["Email"] != "" and orderedEmail[x]["Email"] != \
                orderedEmail[x + 1]["Email"]:
            if isinstance(orderedEmail[x]["Email"], str):
                orderedEmail[x]["Email"] = [orderedEmail[x]["Email"]]
            if isinstance(orderedEmail[x + 1]["Email"], str):
                orderedEmail[x + 1]["Email"] = [orderedEmail[x + 1]["Email"]]

            (orderedEmail[x + 1]["Email"]).extend(orderedEmail[x]["Email"])
            orderedEmail[x]["Id"] = "-"

        # Adding other phone numbers
        if orderedEmail[x + 1]["Phone"] != "" and orderedEmail[x]["Phone"] != "" and orderedEmail[x]["Phone"] != \
                orderedEmail[x + 1]["Phone"]:
            if isinstance(orderedEmail[x]["Phone"], str):
                orderedEmail[x]["Phone"] = [orderedEmail[x]["Phone"]]
            if isinstance(orderedEmail[x + 1]["Phone"], str):
                orderedEmail[x + 1]["Phone"] = [orderedEmail[x + 1]["Phone"]]

            (orderedEmail[x + 1]["Phone"]).extend(orderedEmail[x]["Phone"])
            orderedEmail[x]["Phone"] = "-"

        # Adding all the OrderId's
        if orderedEmail[x + 1]["OrderId"] != "" and orderedEmail[x]["OrderId"] != "" and orderedEmail[x]["OrderId"] != \
                orderedEmail[x + 1]["OrderId"]:
            if isinstance(orderedEmail[x]["OrderId"], str):
                orderedEmail[x]["OrderId"] = [orderedEmail[x]["OrderId"]]
            if isinstance(orderedEmail[x + 1]["OrderId"], str):
                orderedEmail[x + 1]["OrderId"] = [orderedEmail[x + 1]["OrderId"]]

            (orderedEmail[x + 1]["OrderId"]).extend(orderedEmail[x]["OrderId"])
            orderedEmail[x]["OrderId"] = "-"

# _______________________________________________________________________________________________________________________________________________________________

# Sort data
orderedPhone = sorted(orderedEmail, key=lambda k: k["Phone"])

# loop through data
for x in range(0, len(orderedPhone) - 1):
    if orderedPhone[x]["Phone"] == orderedPhone[x + 1]["Phone"] and orderedPhone[x]["Phone"] != "" and orderedPhone[x][
        "Phone"] != -1 and orderedPhone[x + 1]["Phone"] != -1:

        # Updating number of contacts
        orderedPhone[x + 1]["Contacts"] += orderedPhone[x]["Contacts"]

        # Adding all the Id's
        if orderedPhone[x + 1]["Id"] != "" and orderedPhone[x]["Id"] != "" and orderedPhone[x]["Id"] != \
                orderedPhone[x + 1]["Id"]:
            if isinstance(orderedPhone[x]["Id"], int):
                orderedPhone[x]["Id"] = [orderedPhone[x]["Id"]]
            if isinstance(orderedPhone[x + 1]["Id"], int):
                orderedPhone[x + 1]["Id"] = [orderedPhone[x + 1]["Id"]]

            (orderedPhone[x + 1]["Id"]).extend(orderedPhone[x]["Id"])
            orderedPhone[x]["Id"] = -1

        # Adding all the emails
        if orderedPhone[x + 1]["Email"] != "" and orderedPhone[x]["Email"] != "" and orderedPhone[x]["Email"] != \
                orderedPhone[x + 1]["Email"]:
            if isinstance(orderedPhone[x]["Email"], str):
                orderedPhone[x]["Email"] = [orderedPhone[x]["Email"]]
            if isinstance(orderedPhone[x + 1]["Email"], str):
                orderedPhone[x + 1]["Email"] = [orderedPhone[x + 1]["Email"]]

            (orderedPhone[x + 1]["Email"]).extend(orderedPhone[x]["Email"])
            orderedPhone[x]["Id"] = "-"

        # Adding other phone numbers
        if orderedPhone[x + 1]["Phone"] != "" and orderedPhone[x]["Phone"] != "" and orderedPhone[x]["Phone"] != \
                orderedPhone[x + 1]["Phone"]:
            if isinstance(orderedPhone[x]["Phone"], str):
                orderedPhone[x]["Phone"] = [orderedPhone[x]["Phone"]]
            if isinstance(orderedPhone[x + 1]["Phone"], str):
                orderedPhone[x + 1]["Phone"] = [orderedPhone[x + 1]["Phone"]]

            (orderedPhone[x + 1]["Phone"]).extend(orderedPhone[x]["Phone"])
            orderedPhone[x]["Phone"] = "-"

        # Adding all the OrderId's
        if orderedPhone[x + 1]["OrderId"] != "" and orderedPhone[x]["OrderId"] != "" and orderedPhone[x]["OrderId"] != \
                orderedPhone[x + 1]["OrderId"]:
            if isinstance(orderedPhone[x]["OrderId"], str):
                orderedPhone[x]["OrderId"] = [orderedPhone[x]["OrderId"]]
            if isinstance(orderedPhone[x + 1]["OrderId"], str):
                orderedPhone[x + 1]["OrderId"] = [orderedPhone[x + 1]["OrderId"]]

            (orderedPhone[x + 1]["OrderId"]).extend(orderedPhone[x]["OrderId"])
            orderedPhone[x]["OrderId"] = "-"

# _______________________________________________________________________________________________________________________________________________________________

# Sort data
orderedOID = sorted(orderedPhone, key=lambda k: k["OrderId"])

# loop through data
for x in range(0, len(orderedOID) - 1):
    if orderedOID[x]["OrderId"] == orderedOID[x + 1]["OrderId"] and orderedOID[x]["OrderId"] != "" and orderedOID[x][
        "OrderId"] != "-" and orderedOID[x + 1]["OrderId"] != "-":

        # Updating number of contacts
        orderedOID[x + 1]["Contacts"] += orderedOID[x]["Contacts"]

        # Adding all the Id's
        if orderedOID[x + 1]["Id"] != "" and orderedOID[x]["Id"] != "" and orderedOID[x]["Id"] != orderedOID[x + 1][
            "Id"]:
            if isinstance(orderedOID[x]["Id"], int):
                orderedOID[x]["Id"] = [orderedOID[x]["Id"]]
            if isinstance(orderedOID[x + 1]["Id"], int):
                orderedOID[x + 1]["Id"] = [orderedOID[x + 1]["Id"]]

            (orderedOID[x + 1]["Id"]).extend(orderedOID[x]["Id"])
            orderedOID[x]["Id"] = -1

        # Adding all the emails
        if orderedOID[x + 1]["Email"] != "" and orderedOID[x]["Email"] != "" and orderedOID[x]["Email"] != \
                orderedOID[x + 1]["Email"]:
            if isinstance(orderedOID[x]["Email"], str):
                orderedOID[x]["Email"] = [orderedOID[x]["Email"]]
            if isinstance(orderedOID[x + 1]["Email"], str):
                orderedOID[x + 1]["Email"] = [orderedOID[x + 1]["Email"]]

            (orderedOID[x + 1]["Email"]).extend(orderedOID[x]["Email"])
            orderedOID[x]["Id"] = "-"

        # Adding other phone numbers
        if orderedOID[x + 1]["Phone"] != "" and orderedOID[x]["Phone"] != "" and orderedOID[x]["Phone"] != \
                orderedOID[x + 1]["Phone"]:
            if isinstance(orderedOID[x]["Phone"], str):
                orderedOID[x]["Phone"] = [orderedOID[x]["Phone"]]
            if isinstance(orderedOID[x + 1]["Phone"], str):
                orderedOID[x + 1]["Phone"] = [orderedOID[x + 1]["Phone"]]

            (orderedOID[x + 1]["Phone"]).extend(orderedOID[x]["Phone"])
            orderedOID[x]["Phone"] = "-"

        # Adding all the OrderId's
        if orderedOID[x + 1]["OrderId"] != "" and orderedOID[x]["OrderId"] != "" and orderedOID[x]["OrderId"] != \
                orderedOID[x + 1]["OrderId"]:
            if isinstance(orderedOID[x]["OrderId"], str):
                orderedOID[x]["OrderId"] = [orderedOID[x]["OrderId"]]
            if isinstance(orderedOID[x + 1]["OrderId"], str):
                orderedOID[x + 1]["OrderId"] = [orderedOID[x + 1]["OrderId"]]

            (orderedOID[x + 1]["OrderId"]).extend(orderedOID[x]["OrderId"])
            orderedOID[x]["OrderId"] = "-"

# Sort data
orderedId = sorted(orderedOID, key=lambda k: k["Id"])

# loop through data
for x in range(0, len(orderedId) - 1):
    # Writing to text file
    with open('out.txt', 'a') as f:
        with redirect_stdout(f):
            print("Updated Contact Data:")
            print("Id: {}".format(orderedEmail[x]["Id"]))
            print("Email: {}".format(orderedEmail[x]["Email"]))
            print("Phone: {}".format(orderedEmail[x]["Phone"]))
            print("Contacts: {}".format(orderedEmail[x]["Contacts"]))
            print("OrderId: {} \n".format(orderedEmail[x]["OrderId"]))
    f.close()
