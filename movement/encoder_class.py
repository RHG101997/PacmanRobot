import Encoder

enc = Encoder.Encoder(21,20)
enc2 = Encoder.Encoder(5,6)
print("left: " + int(enc.read()) + "right: " + int(enc2.read()))