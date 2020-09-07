from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
sense.set_rotation(270)
n=[0,0,255]
b=[0,0,0]
w=[233,232,231]
r=[212,33,61]
y=[255,255,0]
c=[0,255,255]
baloon =[
    b, b, n, n, n, b, b, b,
    b, n, n, n, n, n, b, b,
    b, n, n, n, n, n, b, b,
    b, b, n, n, n, b, b, b,
    b, b, n, n, n, b, b, b,
    b, b, b, n, b, b, b, b,
    b, b, b, n, b, b, b, b,
    b, b, n, n, n, b, b, b]
star=[
    c, b, c, b, b, c, b, c,
    b, c, b, b, b, b, c, b,
    c, b, c, b, b, c, b, c,
    b, b, b, c, c, b, b, b,
    b, b, b, c, c, b, b, b,
    c, b, c, b, b, c, b, c,
    b, c, b, b, b, b, c, b,
    c, b, c, b, b, c, b, c]
sunshine=[
    y, b, b, y, b, b, b, y,
    b, y, b, y, b, b, y, b,
    b, b, y, y, b, y, b, b,
    b, b, b, y, y, y, y, y,
    y, y, y, y, y, b, b, b,
    b, b, y, b, y, y, b, b,
    b, y, b, b, y, b, y, b,
    y, b, b, b, y, b, b, y]
thermometer=[
    b, b, w, n, w, b, b, b,
    b, b, w, n, w, b, b, b,
    b, b, w, n, w, b, b, b,
    b, b, w, n, w, b, b, b,
    b, b, w, n, w, b, b, b,
    b, w, n, n, n, w, b, b,
    b, w, n, n, n, w, b, b,
    b, b, w, w, w, b, b, b]
kropla = [
    b, b, b, b, n, b, b, b,
    b, b, b, n, n, n, b, b,
    b, b, b, n, n, n, b, b,
    b, b, n, n, n, n, n, b,
    b, n, n, n, n, n, n, n,
    b, n, n, n, n, n, n, n,
    b, n, n, n, n, n, n, n,
    b, b, n, n, n, n, n, b]
while True:
  sense.set_pixels(thermometer)
  sleep(1)
  temperature=sense.get_temperature()
  if temperature >= 22:
    sense.set_pixels(sunshine)
  else:
    sense.set_pixels(star)
  sleep(1)
  temperature=round(temperature)
  temperature=str(temperature)
  sense.show_message(temperature + "'C", text_colour=w, scroll_speed=0.105)
  sleep(0.02)
  for x in range(12):
      sleep(0.05)
      sense.clear()
      sleep(0.005 + 1/(3*(1+x)))
      sense.set_pixels(baloon)
      sleep(0.5/(3*(1+x)))
  sense.set_pixels(baloon)
  sleep(0.3)
  pressure= round(sense.get_pressure())
  sense.show_message(str(pressure) + "HPa", text_colour=w, scroll_speed=0.105)
  sense.set_pixels(kropla)
  sleep(1)
  humidity = round (sense.get_humidity())
  sense.show_message(str(humidity) + "%", text_colour= w, scroll_speed= 0.105)
  sleep(1)
  for x in range(16):
    kolumna = (7-x)
    if x<=7:
      for x in range(8):
        if x<=3:
          sense.set_pixel(kolumna, x, w)
        else:
          sense.set_pixel(kolumna, x, r)
      sleep(0.1)
    else:
      kolumna = (15-x)
      for x in range(8):
        sense.set_pixel(kolumna, x, b)
      sleep(0.1)
  sense.clear()
  sense.show_message("Poland greets", text_colour=r ,scroll_speed=0.08)