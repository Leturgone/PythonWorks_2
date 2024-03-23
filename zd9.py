def main(s):
    key_words = ["do let", "done;","<: "," :>", "::=", "."]
    list_of_tuples = []
    input_string = s
    input_string = input_string.replace(key_words[0],'').replace(key_words[1],'')
    input_string = input_string.replace(key_words[2],'').replace(key_words[3],'')
    input_string = input_string.replace(key_words[4],'').replace(key_words[5],'').split(' ')
    
    for i in input_string:
        if [i]!= ' ':
            
            
    # result = [(pairs[i], int(pairs[i+1])) for i in range(0, len(pairs), 2)]
    return input_string

input_string = "<: do let soat ::= 5521. done;do let isorge ::= 1596. done;do let gearxe_947 ::=-1944. done; :>"
print(main(input_string))

#[('ente', 496), ('gequ', -5474)]