"""
Hey there! How have you been? I've been great! I just learned
about this really cool type of cipher called a Caesar Cipher. 
Here's how it works: You take your message, something like 
"hello" and then you shift all of the letters by a certain offset. 
For example, if I chose an offset of 3 and a message of "hello",
I would encode my message by shifting each letter 3 places to
the left with respect to the alphabet. So "h" becomes "e", "e"
becomes "b", "l" becomes "i", and "o" becomes "l". Then I have
my encoded message, "ebiil"! Now I can send you my message and
the offset and you can decode it by shifting each letter
3 places to the right. The best thing is that Julius Caesar
himself used this cipher, that's why it's called the Caesar
Cipher! Isn't that so cool! Okay, now I'm going to send you 
a longer encoded message that you have to decode yourself! 
xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek
qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu
iqcu evviuj!
This message has an offset of 10. Can you decode it?
"""

alphabet = "abcdefghijklmnopqrstuvwxyz"
mensage = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"


def caesar_decode(code, offset):
    decoded_mensage = ""
    for letter in code:
        if not (letter in alphabet):
            decoded_mensage += letter
        else:
            letter_position = alphabet.find(letter)
            lp_new = letter_position - offset
            decoded_letter = alphabet[lp_new]
            decoded_mensage += decoded_letter
    return decoded_mensage


def caesar_encode(code, offset):
    decoded_mensage = ""
    for letter in code:
        if not (letter in alphabet):
            decoded_mensage += letter
        else:
            letter_position = alphabet.find(letter)
            lp_new = letter_position - offset
            decoded_letter = alphabet[lp_new]
            decoded_mensage += decoded_letter
    return decoded_mensage


my_message = "hello, are you ok?"

print(caesar_decode(mensage, 16))

print(caesar_encode(my_message, 10))
'''
You're getting the hang of this! Okay here are two more messages, the first one
is coded just like before with an offset of ten, and it contains a hint for
decoding the second message!
First message:
jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.
Second message:
bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!
'''

mensage1 = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."
mensage2 = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"

print(caesar_decode(mensage1, 16))
print(caesar_decode(mensage2, 12))

'''
Hello again friend! I knew you would love the Caesar Cipher, it's a cool,
simple way to encrypt messages. Did you know that back in Caesar's time, it was
considered a very secure way of communication and it took a lot of effort to
crack if you were unaware of the value of the shift? That's all changed with
computers! Now we can brute force these kinds of ciphers very quickly, as I'm
sure you can imagine.
To test your cryptography skills, this next coded message is going to be harder
than the last couple to crack. It's still going to be coded with a Caesar
Cipher but this time I'm not going to tell you the value of the shift. You'll
have to brute force it yourself.
Here's the coded message:
vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.
Good luck!
'''

mensage3 = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."

for i in range(len(alphabet)):
    print(str(i + 1) + " " + caesar_decode(mensage3, i+1))

'''
Salutations! As you can see, technology has made brute forcing simple ciphers
like the Caesar Cipher extremely easy, and us crypto-enthusiasts have had to
get more creative and use more complicated ciphers. This next cipher I'm going
to teach you is the Vigenère Cipher, invented by an Italian cryptologist named
Giovan Battista Bellaso (cool name eh?) in the 16th century, but named after
another cryptologist from the 16th century, Blaise de Vigenère.
The Vigenère Cipher is a polyalphabetic substitution cipher, as opposed to the
Caesar Cipher which was a monoalphabetic substitution cipher. What this means
is that opposed to having a single shift that is applied to every letter, the
Vigenère Cipher has a different shift for each individual letter. The value of
the shift for each letter is determined by a given keyword.
Consider the message:
barry is the spy
If we want to code this message, first we choose a keyword. For this example,
we'll use the keyword
dog
Now we repeat the keyword over and over to generate a keyword phrase that is
the same length as the message we want to code. So if we want to code the
message "barry is the spy" our keyword phrase is "dogdo gd ogd ogd". Now we are
ready to start coding our message. We shift each letter of our message by the
place value of the corresponding letter in the keyword phrase, assuming that
"a" has a place value of 0, "b" has a place value of 1, and so forth.
               message:    b  a  r  r  y    i  s    t  h  e    s  p  y
        keyword phrase:    d  o  g  d  o    g  d    o  g  d    o  g  d
 resulting place value:    4 14 15 12 16   24  11   21 25 22   22 17 5
So we shift "b", which has an index of 1, by the index of "d", which is 3. This
gives us an place value of 24, which is "y". Remember to loop back around when
we reach either end of the alphabet! Then continue the trend: we shift "a" by
the place value of "o", 14, and get "m", we shift "r" by the place value of 
"g", 15, and get "l", shift the next "r" by 4 places and get "o", and so forth.
Once we complete all the shifts we end up with our coded message:
eoxum ov hnh gvb
As you can imagine, this is a lot harder to crack without knowing the keyword!
So now comes the hard part. I'll give you a message and the keyword, and you'll
see if you can figure out how to crack it! Ready? Okay here's my message:
dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!
and the keyword to decode my message is 
friends
Because that's what we are! Good luck friend!
'''


def vigenere_decode(code, key):
    new_key = ''
    code_words = code.split()
    key_words = []
    n_code_words = []
    n_key_words = []
    final_numbers = []
    decoded_mensage_raw = ''
    decoded_mensage = ''
    trash = ''
    x = 0
    z = 0
    for word in code_words:
        new_key = ''
        code_letter_position = ''

        for letter in word:
            if not (letter in alphabet):
                trash += letter
            else:
                if x < len(key):
                    new_key += key[x]
                    key_letter_position = str(alphabet.find(key[x]))
                    n_key_words.append(key_letter_position)
                    x += 1
                    if x >= len(key):
                        x = 0
                code_letter_position = str(alphabet.find(letter))
                n_code_words.append(code_letter_position)
        key_words.append(new_key)

    for i in range(0, len(n_code_words)):
        final_numbers.append(int(n_code_words[i]) - int(n_key_words[i]))

    for number in final_numbers:
        decoded_mensage_raw += alphabet[number]

    for letter in code:
        if not (letter in alphabet):
            decoded_mensage += letter
        else:
            decoded_mensage += decoded_mensage_raw[z]
            z += 1
    return decoded_mensage


def vigenere_encode(code, key):
    new_key = ''
    code_words = code.split()
    key_words = []
    n_code_words = []
    n_key_words = []
    final_numbers = []
    decoded_mensage_raw = ''
    decoded_mensage = ''
    trash = ''
    x = 0
    z = 0
    for word in code_words:
        new_key = ''
        code_letter_position = ''

        for letter in word:
            if not (letter in alphabet):
                trash += letter
            else:
                if x < len(key):
                    new_key += key[x]
                    key_letter_position = str(alphabet.find(key[x]))
                    n_key_words.append(key_letter_position)
                    x += 1
                    if x >= len(key):
                        x = 0
                code_letter_position = str(alphabet.find(letter))
                n_code_words.append(code_letter_position)
        key_words.append(new_key)

    for i in range(0, len(n_code_words)):
            x = 0
            x = int(n_code_words[i]) + int(n_key_words[i])
            if x > 25:
                x -= 26
                final_numbers.append(x)
            else:
                final_numbers.append(x)

    for number in final_numbers:
        decoded_mensage_raw += alphabet[number]

    for letter in code:
        if not (letter in alphabet):
            decoded_mensage += letter
        else:
            decoded_mensage += decoded_mensage_raw[z]
            z += 1
    return decoded_mensage


key = 'friends'
mensage4 = 'dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!'

key1 = 'friends'
mensage5 = 'you were able to decode this? nice work! you are becoming quite the expert at crytography!'

print(vigenere_decode(mensage4, key))
print(vigenere_encode(mensage5, key1))
