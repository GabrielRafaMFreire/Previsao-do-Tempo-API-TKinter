import requests
import json
import datetime
from tkinter import *

def pegar_clima():
    api_key = "ef6b0477788c72ad63b84891fd67fc8a"

    cidade = entrada.get()
    linkapi = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&lang=pt_br"

    requisicao = requests.get(linkapi)
    requisicao_dic = requisicao.json()

    descricao = requisicao_dic['weather'][0]['description']
    temperatura = requisicao_dic['main']['temp'] - 273.15
    nascer_do_sol = requisicao_dic ['sys']['sunrise']
    por_do_sol = requisicao_dic ['sys']['sunset']

 # Converter timestamps para horário humano (UTC)
    horario_nascer_do_sol = datetime.datetime.utcfromtimestamp(nascer_do_sol).strftime('%H:%M:%S')
    horario_por_do_sol = datetime.datetime.utcfromtimestamp(por_do_sol).strftime('%H:%M:%S')

    texto = f'''
    No momento = {descricao}
    Temperatura = {temperatura:.1f}°C
    Nascer do Sol = {horario_nascer_do_sol} 
    Pôr do Sol = {horario_por_do_sol} '''


    texto_tempo["text"] = texto

#parte gráfica 

window = Tk()
window.title("Previsão do tempo")
window.geometry("330x200")

#texto
text_orientation = Label(window, text = "Digite uma cidade para exibir o tempo:", wraplength=310)
text_orientation.grid(column=0, row = 0, padx= 10, pady=10)

#input cidade que o usuario vai digitar 
entrada = Entry(window, width=40) #linha que permite o usuario inserir o texto
entrada.grid(column=0, row=1, padx=10, pady=10)

#botao
bt = Button(window, text = "Clique aqui", command = pegar_clima)
bt.grid(column=0, row=2, padx= 10, pady=10)


#print texto

texto_tempo = Label(window, text="")
texto_tempo.grid(column=0, row=2, padx= 10, pady=10)


window.mainloop()
   

   #Rafáaa
