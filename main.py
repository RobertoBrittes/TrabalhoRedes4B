import streamlit as st

def validar_mascara(mascara: str):
    if mascara.startswith("/"):
        prefixo_str = mascara[1:]
        
        if prefixo_str.isdigit():
            prefixo = int(prefixo_str)
            if 0 <= prefixo <= 32:
                return True, f"Prefixo válido ({mascara})"
        
        return False, "Prefixo inválido (deve ser entre /0 e /32)"

st.title("<< Trabalho de Máscara de Rede >>")

ip = st.text_input("Insira o endereço IP:")
netmask = st.text_input("Insira a Máscara de Rede: ")

splitedIp = ip.split(".")

if (len(splitedIp) != 4 and validar_mascara(netmask)):
    st.text("Formato de endereço inválido! Ex: (255.255.1.1)")
else:
    # IP em binário
    ip_binario = ".".join(format(int(o), "08b") for o in splitedIp)
    st.text("IP em binário: " + ip_binario)

    #Máscara em binário