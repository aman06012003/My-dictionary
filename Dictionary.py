import webbrowsers
print('Welcome to my dictionary')

dic1 = {'abacus':'A frame of wire with rowsof wires along which beads are slid', 'abandon': 'give up','abase': 'humiliate or degrade', 'abashed': 'embarrassed'}

try:
  word = input('Enter the word : ').lower()

   print(dic1[word])
 except Exception:
    webbrowser.open(f'{word} meaning in english')
