import shutil

original = r"C:\Users\s2383\OneDrive\Desktop\CMI_DB\cmi_cfl.db" # to change for specified PC
target = r"C:\Users\s2383\OneDrive\Desktop\CMI_DB\db backup\cmi_cfl.db" # to change for specified PC

shutil.copyfile(original, target)

