import pandas as pd


# copy-pasta from Pedro's tutorial setup script
def kgtk_to_dataframe(kgtk):
    columns = kgtk[0].split("\t")
    data = []
    for line in kgtk[1:]:
        data.append(line.encode('utf-8').decode('utf-8').split("\t"))
    return pd.DataFrame(data, columns=columns)