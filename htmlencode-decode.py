import html
print("""
--------------------------------
          HAWK DEFACER 
--------------------------------
1 - HTML ENCODE 
2 - HTML DECODE 
""")
hawk = input(" Seçim yap => ")
if hawk == "1" : 
    a_string = input("Html Karakterlerini giriniz örnek '&lt;body&gt;' =>> ")
    decoded_string = html.unescape(a_string)
    print(decoded_string)
elif hawk == "2" : 
    b_string = input("Html Karakterlerini giriniz örnek '<body>' =>>")
    encoded_string = html.escape(b_string)
    print(encoded_string)

