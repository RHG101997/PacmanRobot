import Encoder


enc = Encoder.Encoder(20,21)
enc2 = Encoder.Encoder(5,6)
while True:
    print("left: ",  end = "")
    print(enc.read())
    print("right: ", end = "")
    print(enc2.read())