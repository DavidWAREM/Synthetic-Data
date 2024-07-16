import subprocess


path_model = "C:\\Users\\mueda\\Desktop\\Rechennetzmodell_Wasser\\Netz\\EO_1.STA"
path_config = "C:\\Users\\mueda\\Desktop\\"
# N: Startet mit dem angegeben Netz
N = " /N=" + path_model
# Lädt alle Einstellungen aus einer STANET-Konfigurationsdatei.
K = " /K=" + path_config
# Berechnung des Netzes
B= " /B"
# Arbeitsverzeichnis CONFIG
D = " /D" + path_config
# Name der importdefinition
X = " /X=Import_L"
# Pfad der zu importierenden Textdatei.
#F = " /F=" + path_stafiles + "Import_Lei.csv"
# Medium des netzes
M = " /M=W"
# Zusätzliche Werte in existierendes Netz einlesen. Bewirkt,
# dass ein mit /X /F angegebener Import in ein bestehendes
# Netz vorgenommen wird. Hierbei muss das mit dem
# Kommandozeilenparameter /N angegebene Zielnetz bereits existieren.
A = " /A"
# Letzte Datei laden. Bewirkt, dass beim Programmstart das zuletzt
# geöffnete Netz wieder geladen wird.
# R=" /R"
# Name der Exportdefinition
# Y=" /Y=Export_Knoten"
Y = " /Y=Export_Knoten"
# Pfad und Name der Datei, in die geschrieben werden soll; nur
# zusammen mit /Y.
# E=" /E="+path_stafiles+"export_L.txt"
#E = " /E=" + path_stafiles + "export_K.txt"
# print(E)

start = "start "
# Stanet Pfad kann sich je nach Benutzer oder PC ändern
kommando = "C:\\Program Files\\STANET\\BIN\\" + "stanet64" + " /NoUserConfig" + ' /T=2' + " /NoStartDlogs" + B
# print(kommando)
# print(E)
subprocess.run(kommando)