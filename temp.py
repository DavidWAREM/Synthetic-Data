import subprocess


file_path = "C:\\Users\\d.muehlfeld\\weitere Daten\\Leitungen.CSV"
comand = ("C:\\Program Files\\STANET\\BIN\\stanet64.exe" +
          " /R" +
          " /Y=Export_Hydranten" +
          " /E="+file_path+"export_K.txt")
comand_temp = ("C:\\Program Files\\STANET\\BIN\\stanet64.exe" +
          " /R")
subprocess.run(comand_temp)
